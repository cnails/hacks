from collections import namedtuple

import cv2
import numpy as np

ATOM_RADIUS_FRAC = 5 * 1e-4
BOND_WIDTH_FRAC = 5 * 1e-4


class MolLabelsDrawer():
    def __init__(self, img, img_labels, draw_types, markers, colors, visualize=True):
        self.img = img.copy()
        self.h, self.w = img.shape[:2]
        self.atom_radius_frac = ATOM_RADIUS_FRAC
        self.bond_width_frac = BOND_WIDTH_FRAC
        self.mask = np.full(img.shape[:2], 0, dtype=np.uint8)
        self.img_labels = img_labels
        self.draw_types, self.markers, self.colors = draw_types, markers, colors
        self.visualize = visualize
        
        self.Node = namedtuple('Node', ['x', 'y', 'name', 'region'])
        self.ConnPoint = namedtuple('ConnPoint', ['node1', 'node2', 'name'])
        self.ConnPoly = namedtuple('ConnPoly', ['poly', 'name'])
        self.ConnLine = namedtuple('ConnLine', ['x1', 'y1', 'x2', 'y2', 'name'])
    
    def _calc_point_center(self, label):
        center = np.array([label['x'], label['y']])
        
        return center
    
    @staticmethod
    def _is_connection_type(obj_name):
        return obj_name.lower() in \
            ['single', 'double', 'triple',
             'up', 'down', 'either', 'wedge', 'dash']
                
    def process_atoms(self, img_labels):
        nodes = []
        
        for obj_name in img_labels.keys():
            if MolLabelsDrawer._is_connection_type(obj_name):
                continue
            
            for label in img_labels[obj_name]:
                if obj_name not in self.draw_types:
                    raise Exception(f'Object name doesnot exist: {obj_name}')
                
                if self.draw_types[obj_name] == 'point':
                    atom_center = self._calc_point_center(label['geometry'])
                    region = 'point'

                nodes.append(self.Node(x=atom_center[0], y=atom_center[1], name=obj_name, region=region))
        
        return nodes
    
    @staticmethod
    def _calc_scale_factor_coef(nodes):
        xs = np.array([node.x for node in nodes])
        ys = np.array([node.y for node in nodes])
        
        # Area of a box covering visible molecule
        area = (np.max(xs) - np.min(xs)) * (np.max(ys) - np.min(ys))
        
        return area / len(nodes)
    
    @staticmethod
    def get_closest_nodes(nodes, point):
        np_nodes = np.array([[node.x, node.y] for node in nodes])
        node_dists = np.apply_along_axis(lambda node: np.linalg.norm(node - point), axis=1, arr=np_nodes)
        closest_node_idxs = np.argsort(node_dists)[:2]
        closest_nodes = [nodes[closest_node_idxs[0]], nodes[closest_node_idxs[1]]]
        distances = node_dists[closest_node_idxs]

        return closest_nodes, distances
        
    def process_line_connection(self, label, obj_name):
        conns = []
        for i in range(len(label) - 1):
            x1, y1, x2, y2 = label[i]['x'], label[i]['y'], label[i + 1]['x'], label[i + 1]['y']
            conn = self.ConnLine(x1=x1, y1=y1, x2=x2, y2=y2, name=obj_name)
            conns.append(conn)
        
        return conns
    
    def process_connections(self, nodes, img_labels):
        connections = []
        
        for obj_name in img_labels.keys():
            if not MolLabelsDrawer._is_connection_type(obj_name):
                continue
            
            for label in img_labels[obj_name]:
                if len(label['geometry']) < 2:
                    continue
                
                if self.draw_types[obj_name] == 'line':
                    conns = self.process_line_connection(label['geometry'], obj_name)
                
                connections.extend(conns)
                
        return connections
    
    def draw_atom(self, node, atom_radius):
        atom_radius = int(atom_radius / 1.5) if node.name == 'C_point' else atom_radius
        
        cv2.circle(self.mask, (int(node.x), int(node.y)), atom_radius,
                  color=(self.markers[node.name],), thickness=-1)

        if self.visualize:
            cv2.circle(self.img, (int(node.x), int(node.y)), atom_radius, color=self.colors[node.name], thickness=-1)
    
    def draw_atoms(self, nodes, scale_factor_coef):
        atom_radius = int(scale_factor_coef * self.atom_radius_frac)
        
        for node in nodes:
            self.draw_atom(node, atom_radius)

    def draw_line_connection(self, conn, bond_width):
        cv2.line(self.mask, (conn.x1, conn.y1), (conn.x2, conn.y2), (self.markers[conn.name],), thickness=bond_width)
        
        if self.visualize:
            color = (min(int(self.markers[conn.name] * 70), 255),) * 3
            cv2.line(self.img, (conn.x1, conn.y1), (conn.x2, conn.y2), color=self.colors[conn.name], thickness=bond_width)
            
    def draw_connections(self, connections, scale_factor_coef):
        bond_width = int(scale_factor_coef * self.bond_width_frac)
        
        for conn in connections:
            if isinstance(conn, self.ConnLine):
                self.draw_line_connection(conn, bond_width)
    
    def draw_labels(self):
        img_labels = self.img_labels
        
        # Collect atoms coordinates
        nodes = self.process_atoms(img_labels)
        
        # Collect and draw connections
        connections = self.process_connections(nodes, img_labels)
        
        if (len(nodes) > 0) and (len(connections) > 0):
            sfc = MolLabelsDrawer._calc_scale_factor_coef(nodes)
            self.draw_connections(connections, sfc)
        
            # Draw atoms
            self.draw_atoms(nodes, sfc)
        
        return self.img, self.mask

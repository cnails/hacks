import json

def parse_labelbox_config(path_to_json):
    with open(path_to_json, 'r') as f:
        label_config = json.load(f)

    draw_types = {tool['name']: tool['tool'] for tool in label_config['tools']}
    class_markers = {tool['name']: i + 1 for i, tool in enumerate(label_config['tools'])}
    class_colors = {tool['name']: tool['color'] for tool in label_config['tools']}

    # Convert hex to RGB values
    class_colors = {name: tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) for name, c in class_colors.items()}

    return draw_types, class_markers, class_colors

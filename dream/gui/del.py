import sys, os, pprint, time
# from PySide.QtCore import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTreeView, QApplication, QAbstractItemView
# from PyQt5.QtCore import 
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# from PySide.QtGui import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = QApplication(sys.argv)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# init widgets
view = QTreeView()
# view.setSelectionBehavior(QAbstractItemView.SelectRows)
model = QStandardItemModel()
# model.setHorizontalHeaderLabels(['', '', ''])
view.setModel(model)
# view.setUniformRowHeights(True)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# populate data
directory = QtWidgets.QFileDialog.getExistingDirectory(caption = "Выберите папку")
info = {}
if directory:
    for direc in os.listdir(directory):
        info[direc]
        parent1 = QStandardItem(direc)
        if os.path.isdir(os.path.join(directory, direc)):
            for fil in os.listdir(os.path.join(directory, direc)):
                parent2 = QStandardItem(fil)
                parent1.appendRow(parent2)
                if os.path.isdir(os.path.join(os.path.join(directory, direc), fil)):
                    for fil_1 in os.listdir(os.path.join(os.path.join(directory, direc), fil)):
                        parent3 = QStandardItem(fil_1)
                        parent2.appendRow(parent3)
                        if os.path.isdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
                            for fil_2 in os.listdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
                                parent4 = QStandardItem(fil_2)
                                parent3.appendRow(parent4)
                                # if os.path.isdir(os.path.join(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1), fil_2)):
                                #     for fil_3 in os.listdir(os.path.join(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1), fil_2)):
                                #         if not os.path.isdir(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1), fil_2), fil_2)):
                                #             parent5 = QStandardItem(fil_3)
                                #             parent4.appendRow(parent5)
            # parent2 = QStandardItem(direc)
        # if os.path.isdir(os.path.join(directory, direc)):
            # parent1 = QStandardItem(direc)
            # for file in range(3):
                # child1 = QStandardItem('Child {}'.format(3+j))
                # child2 = QStandardItem('col: {}'.format(j+1))
                # child3 = QStandardItem('col: {}'.format(j+2))
                # parent2 = QStandardItem('Family {}. Some long status text for sp'.format(j))
                # parent2.appendRow([child1, child2, child3])
            # parent1.appendRow(parent2)
            # model.appendRow(parent1)
        # parent1.appendRow(parent2)
        model.appendRow(parent1)
# index = model.indexFromItem(parent1) 
view.show()
sys.exit(app.exec_()) 
    # for file_name in os.listdir(directory):
        # parent1 = QStandardItem(file_name)

sys.exit()

# for i in range(3):
#     parent1 = QStandardItem('Family {}. Some long status text for sp'.format(i))
#     for j in range(3):
#         child1 = QStandardItem('Child {}'.format(i*3+j))
#         child2 = QStandardItem('row: {}, col: {}'.format(i, j+1))
#         child3 = QStandardItem('row: {}, col: {}'.format(i, j+2))
#         parent2 = QStandardItem('Family {}. Some long status text for sp'.format(i))
#         parent2.appendRow([child1, child2, child3])
#         parent1.appendRow(parent2)
#     model.appendRow(parent1)
#     # span container columns
#     view.setFirstColumnSpanned(i, view.rootIndex(), True)
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # expand third container
# index = model.indexFromItem(parent1)
# # view.expand(index)
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # select last row
# # selmod = view.selectionModel()
# # index2 = model.indexFromItem(child1)
# # selmod.select(index1, QItemSelectionModel.Select|QItemSelectionModel.Rows)
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# view.show()
# sys.exit(app.exec_())
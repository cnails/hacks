# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 20, 93, 561))
        self.back_button.setObjectName("back_button")
        self.tree_files = QtWidgets.QTreeView(self.centralwidget)
        self.tree_files.setGeometry(QtCore.QRect(120, 50, 491, 331))
        self.tree_files.setObjectName("tree_files")
        self.push_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_file_button.setGeometry(QtCore.QRect(280, 390, 171, 71))
        self.push_file_button.setObjectName("push_file_button")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 490, 481, 41))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 470, 181, 21))
        self.label.setObjectName("label")
        self.select_dir_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_dir_button.setGeometry(QtCore.QRect(300, 540, 141, 31))
        self.select_dir_button.setObjectName("select_dir_button")
        self.pull_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.pull_file_button.setGeometry(QtCore.QRect(120, 390, 151, 71))
        self.pull_file_button.setObjectName("pull_file_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 151, 31))
        self.label_2.setObjectName("label_2")
        self.copy_to_clip_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_to_clip_button.setGeometry(QtCore.QRect(460, 390, 151, 71))
        self.copy_to_clip_button.setObjectName("copy_to_clip_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 10, 241, 31))
        self.label_3.setObjectName("label_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(620, 50, 191, 331))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.push_file_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.push_file_button_3.setGeometry(QtCore.QRect(640, 390, 161, 51))
        self.push_file_button_3.setObjectName("push_file_button_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Files"))
        self.back_button.setText(_translate("MainWindow", "Н\n"
"А\n"
"З\n"
"А\n"
"Д\n"
"<-"))
        self.push_file_button.setText(_translate("MainWindow", "Отправить файлы"))
        self.label.setText(_translate("MainWindow", "Рабочая директория:"))
        self.select_dir_button.setText(_translate("MainWindow", "Выбрать папку"))
        self.pull_file_button.setText(_translate("MainWindow", "Загрузить файлы"))
        self.label_2.setText(_translate("MainWindow", "Файлы на сервере:"))
        self.copy_to_clip_button.setText(_translate("MainWindow", "Скопировать ссылку\n"
"на файл"))
        self.label_3.setText(_translate("MainWindow", "Пользователи с доступом на запись:"))
        self.push_file_button_3.setText(_translate("MainWindow", "Сохранить"))

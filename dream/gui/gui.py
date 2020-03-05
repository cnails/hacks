# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_chat = QtWidgets.QListWidget(self.centralwidget)
        self.list_chat.setGeometry(QtCore.QRect(90, 50, 501, 411))
        self.list_chat.setObjectName("list_chat")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(90, 480, 361, 81))
        self.input_text.setObjectName("input_text")
        self.send_message_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_button.setGeometry(QtCore.QRect(480, 500, 101, 41))
        self.send_message_button.setObjectName("send_message_button")
        self.go_to_settings = QtWidgets.QPushButton(self.centralwidget)
        self.go_to_settings.setGeometry(QtCore.QRect(10, 70, 71, 61))
        self.go_to_settings.setObjectName("go_to_settings")
        self.go_to_chats = QtWidgets.QPushButton(self.centralwidget)
        self.go_to_chats.setGeometry(QtCore.QRect(10, 160, 71, 131))
        self.go_to_chats.setObjectName("go_to_chats")
        self.go_to_files = QtWidgets.QPushButton(self.centralwidget)
        self.go_to_files.setGeometry(QtCore.QRect(10, 300, 71, 131))
        self.go_to_files.setObjectName("go_to_files")
        self.list_users = QtWidgets.QListWidget(self.centralwidget)
        self.list_users.setGeometry(QtCore.QRect(610, 50, 171, 341))
        self.list_users.setObjectName("list_users")
        self.invite_button = QtWidgets.QPushButton(self.centralwidget)
        self.invite_button.setGeometry(QtCore.QRect(650, 500, 101, 41))
        self.invite_button.setObjectName("invite_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 20, 111, 16))
        self.label.setObjectName("label")
        self.name_chat = QtWidgets.QLabel(self.centralwidget)
        self.name_chat.setGeometry(QtCore.QRect(320, 5, 181, 31))
        self.name_chat.setObjectName("name_chat")
        self.invite_to_chat = QtWidgets.QTextEdit(self.centralwidget)
        self.invite_to_chat.setGeometry(QtCore.QRect(610, 410, 171, 51))
        self.invite_to_chat.setObjectName("invite_to_chat")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_message_button.setText(_translate("MainWindow", "Отправить"))
        self.go_to_settings.setText(_translate("MainWindow", "настройки"))
        self.go_to_chats.setText(_translate("MainWindow", "чаты"))
        self.go_to_files.setText(_translate("MainWindow", "файлы"))
        self.invite_button.setText(_translate("MainWindow", "Пригласить"))
        self.label.setText(_translate("MainWindow", "Участники чата"))
        self.name_chat.setText(_translate("MainWindow", "TextLabel"))

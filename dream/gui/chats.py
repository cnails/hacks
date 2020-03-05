# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_gui.ui'
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
        self.list_chats = QtWidgets.QListWidget(self.centralwidget)
        self.list_chats.setGeometry(QtCore.QRect(40, 70, 311, 251))
        self.list_chats.setObjectName("list_chats")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 61, 16))
        self.label.setObjectName("label")
        self.change_chat_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_chat_button.setGeometry(QtCore.QRect(140, 340, 111, 41))
        self.change_chat_button.setObjectName("change_chat_button")
        self.append_chat_button = QtWidgets.QPushButton(self.centralwidget)
        self.append_chat_button.setGeometry(QtCore.QRect(140, 510, 111, 41))
        self.append_chat_button.setObjectName("append_chat_button")
        self.new_chat = QtWidgets.QTextEdit(self.centralwidget)
        self.new_chat.setGeometry(QtCore.QRect(40, 430, 311, 61))
        self.new_chat.setAccessibleDescription("")
        self.new_chat.setObjectName("new_chat")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 400, 141, 16))
        self.label_2.setObjectName("label_2")
        self.list_dialogs = QtWidgets.QListView(self.centralwidget)
        self.list_dialogs.setGeometry(QtCore.QRect(430, 70, 311, 251))
        self.list_dialogs.setObjectName("list_dialogs")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 40, 111, 16))
        self.label_3.setObjectName("label_3")
        self.change_dialog = QtWidgets.QPushButton(self.centralwidget)
        self.change_dialog.setGeometry(QtCore.QRect(530, 340, 111, 41))
        self.change_dialog.setObjectName("change_dialog")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 400, 201, 16))
        self.label_4.setObjectName("label_4")
        self.new_dialog = QtWidgets.QTextEdit(self.centralwidget)
        self.new_dialog.setGeometry(QtCore.QRect(430, 430, 311, 61))
        self.new_dialog.setObjectName("new_dialog")
        self.append_dialog_button = QtWidgets.QPushButton(self.centralwidget)
        self.append_dialog_button.setGeometry(QtCore.QRect(530, 510, 111, 41))
        self.append_dialog_button.setObjectName("append_dialog_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбор чата"))
        self.label.setText(_translate("MainWindow", "Группы:"))
        self.change_chat_button.setText(_translate("MainWindow", "Перейти"))
        self.append_chat_button.setText(_translate("MainWindow", "Создать"))
        self.label_2.setText(_translate("MainWindow", "Создать новую группу:"))
        self.label_3.setText(_translate("MainWindow", "Личные диалоги:"))
        self.change_dialog.setText(_translate("MainWindow", "Перейти"))
        self.label_4.setText(_translate("MainWindow", "Начать диалог с пользователем:"))
        self.append_dialog_button.setText(_translate("MainWindow", "Создать"))

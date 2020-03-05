import sys, json, os, time
import requests as req
from PyQt5 import QtWidgets, QtCore, QtGui
import gui
import reg
import chats

url = 'http://192.168.1.56:33/'

class Chats(QtWidgets.QMainWindow, chats.Ui_MainWindow):
    def go_to_chat(self):
        self.chat = self.list_chats.selectedItems()[0].text()
        # print(self.chat)
        self.hide()
        # app = ExampleApp(self.user_id, self.chat)
        # app.show()
        self.parent.__init__(self.user_id, self.chat)
        # self.parent.download_message()
        # self.parent.chat_id = self.chat
        self.parent.show()

    def append_chat(self):
        req.get(url, data = {'append_chat': self.new_chat.toPlainText(), 'user_id': self.user_id})
        self.list_chats.clear()
        self.download_chats()

    def append_dialog(self):
        pass
    
    def download_dialogs(self):
        pass
    
    def download_chats(self):
        response = req.get(url, data = {'return_chats': self.user_id})
        # try:
        chats = response.json()
        for chat in chats:
            self.list_chats.addItem(chat)
        # except json.decoder.JSONDecodeError:
            # pass

    def __init__(self, user_id, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        try:
            self.parent.timer.stop()
        except:
            pass
        self.user_id = user_id
        self.download_chats()
        self.download_dialogs()
        self.change_chat_button.clicked.connect(self.go_to_chat)
        self.append_chat_button.clicked.connect(self.append_chat)


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):            
    def append_chat(self, chat_id):
        # with open('info.json')
        req.get(url, data={'append_to_chat': [self.user_id, self.chat_id]})

    def send_message(self):
        text = self.input_text.toPlainText()
        info = [self.user_id, self.chat_id, text]
        req.get(url, data = {'new_message': True, 'user_id': self.user_id, 'chat_id': self.chat_id, 'text': text})
        # self.list_chat.addItem(text)
        # self.list_chat.scrollToBottom()
        self.input_text.clear()
        self.download_message()

    # def download_chats(self):
        # pass

    def append_user_to_chat(self):
        response = req.get(url, data = {'append_user_to_chat': self.invite_to_chat.toPlainText(), 'chat_id': self.chat_id})
        if not response.json():
            self.invalid_user = QtWidgets.QLabel(self)
            self.invalid_user.setText('User not found')
            self.invalid_user.setObjectName('short_login')
            self.invalid_user.setGeometry(655, 470, 200, 20)
            self.invalid_user.show()
        else:
            self.invite_to_chat.clear()
            self.download_users()

    def download_users(self):
        self.list_users.clear()
        response = req.get(url, data = {'return_users': self.chat_id})
        info = response.json()
        if info:
            for user in info:
                self.list_users.addItem(user)

    def download_message(self):
        self.list_chat.clear()
        info = req.post(url, data = {'read_message': self.chat_id})
        info = info.json().get('message')
        self.name_chat.setText(str(self.chat_id))
        self.name_chat.setStyleSheet('color: red')
        self.name_chat.setStyleSheet('font: 15pt Comic Sans MS')
        if self.isActive:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.download_message)
            self.timer.start(500)
        for i, mes in enumerate(info):
            for user_id, message in mes.items():
                pass
            if user_id == self.user_id:
                self.list_chat.addItem(message)
            else:
                widgitItem = QtWidgets.QListWidgetItem()
                widget = QtWidgets.QWidget()
                widgetText = QtWidgets.QLabel(f'<span style="color:#ff0000;">{user_id}:</span><br>{message}')
                widgetLayout = QtWidgets.QHBoxLayout()
                widgetLayout.addWidget(widgetText)
                widget.setLayout(widgetLayout)
                self.list_chat.addItem(widgitItem)
                widgitItem.setSizeHint(widget.sizeHint())
                self.list_chat.setItemWidget(widgitItem, widget)
            if user_id == self.user_id:
                self.list_chat.item(i).setTextAlignment(10)
            self.list_chat.scrollToBottom()


    def change_to_chats(self):
        self.hide()
        self.isActive = False
        self.chats_window = Chats(self.user_id, self)
        self.chats_window.show()

    def __init__(self, user_id, chat_id = 0, chats = False):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        if chat_id:
            self.chat_id = chat_id
        else:
            self.chat_id = 1
        if chats:
            self.change_to_chats()
        else:
            self.isActive = True
            self.download_message()
            self.download_users()
            self.invite_button.clicked.connect(self.append_user_to_chat)
            self.send_message_button.clicked.connect(self.send_message)
            self.go_to_chats.clicked.connect(self.change_to_chats)

class Registr(QtWidgets.QMainWindow, reg.Ui_Registration):
    def check_login(self):
        # if self.login_incorrect.isVisible():
            # self.login_incorrect.hide()
        # if self.short_login.isVisible():
            # self.short_login.hide()
        self.login = self.textEdit.toPlainText()
        if len(self.login) < 3:
            self.short_login = QtWidgets.QLabel(self)
            self.short_login.setText('Too short login')
            self.short_login.setObjectName('short_login')
            self.short_login.setGeometry(350, 250, 200, 20)
            self.short_login.show()
        response = req.post(url, data = {'check_login': self.login})
        if response.json():
            with open('info.json', 'w') as fd:
                fd.write(json.dumps({'user_id': self.login}))
            req.get(url, data = {'append_user_to_chat': self.login, 'chat_id': "1"})
            self.hide()
            window = ExampleApp(self.login)
            window.show()
        else:
            self.login_incorrect = QtWidgets.QLabel(self)
            self.login_incorrect.setText('Login already taken')
            self.login_incorrect.setObjectName('login_incor')
            self.login_incorrect.setGeometry(350, 250, 200, 20)
            self.login_incorrect.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check_login)

def registr():
    app_login = QtWidgets.QApplication(sys.argv)
    window_reg = Registr()
    window_reg.show()
    sys.exit(app_login.exec_())
    if os.path.exists('info.json'):
        with open('info.json', 'r') as fd:
            user_id = json.load(fd).get('user_id')
        main(user_id, chats=True)

def main(user_id, chats = False):
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp(user_id, chats = chats)
    if not chats:
        window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if not os.path.exists('info.json'):
        registr()
    else:
        with open('info.json', 'r') as fd:
            info = json.load(fd)
        user_id = info.get('user_id')
        main(user_id, chats=True)


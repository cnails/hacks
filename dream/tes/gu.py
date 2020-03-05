import sys, json, os, time
import requests as req
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView, QApplication, QAbstractItemView
from PyQt5.Qt import QApplication, QClipboard
import gui
import reg
import chats
import tree_gui

url = 'http://192.168.1.56:33/'

class Files(QtWidgets.QMainWindow, tree_gui.Ui_MainWindow):
    def push_folder(self):
        # if 'C:' in directory:
            # name = os.path.basename(directory)
        # name = directory
        data = {'name': self.directory, 'chat_id': self.parent.chat_id}
        for fil in os.listdir(self.directory):
            if not os.path.isdir(os.path.join(self.directory, fil)):
                req.get(url, data = {'name': self.pref, 'chat_id': self.parent.chat_id})
                with open(os.path.join(self.directory, fil), 'r') as fd:
                    data[os.path.join(self.pref, fil)] = fd.read()
            else:
                self.pref = os.path.join(self.pref, os.path.basename(fil))
                self.directory = os.path.join(self.directory, fil)
                self.push_folder()
        req.post(url, data = data)
        self.make_tree()

    def make_tree(self):
        self.model = QStandardItemModel()
        self.tree_files.setModel(self.model)
        info = req.get(url, data = {'tree': self.parent.chat_id}).json()
        if info.get('parent1'):
            for direc in info.get('parent1'):
                parent1 = QStandardItem(direc)
                if direc == info.get('parent1')[-1]:

                # if os.path.isdir(os.path.join(directory, direc)):
                    for fil in info.get('parent2'):
                        parent2 = QStandardItem(fil)
                        parent1.appendRow(parent2)
                        if fil == info.get('parent2')[-1]:
                        # if os.path.isdir(os.path.join(os.path.join(directory, direc), fil)):
                            for fil_1 in info.get('parent3'):
                                parent3 = QStandardItem(fil_1)
                                parent2.appendRow(parent3)
                                # if os.path.isdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
                                    # for fil_2 in os.listdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
                                        # parent4 = QStandardItem(fil_2)
                                        # parent3.appendRow(parent4)
                self.model.appendRow(parent1)
            

    def browse_folder(self):
        # self.listWidget.clear()
            # self.directory = 
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.directory = directory
        with open('info.json', 'r') as fd:
            info = json.load(fd)
        info['dir'] = self.directory
        with open('info.json', 'w') as fd:
            fd.write(json.dumps(info))
        self.lineEdit.setText(directory)
        self.pref = os.path.basename(directory)
        # to_push = {}
        # to_push['dirs'] = []
        # to_push['fils'] = []
        # for fil in os.listdir(directory):
            # if os.path.isdir(os.path.join(directory, fil)):
                # directory_1 = os.path.join(directory, fil)
                # print(directory)
                # to_push['dirs'][fil]['fils'] = []
                # for fil_1 in os.listdir(directory_1):
                    # if os.path.isdir(os.path.join(directory_1, fil_1)):
                        # to_push['dirs'][fil]['dirs']
                    # else:
                        # to_push['dirs'][fil]['fils'].append(fil_1)
                # to_push['dirs'].append(fil)
                # new = to_push.get('dirs')
                # for fil_1 in os.listdir(directory):
            # else:
                # to_push['fils'].append(fil)
        # print(to_push)
        # if os.path.isdir()
        # print(self.parent.users)
        # for i, user in enumerate(self.parent.users):
        #     # globals()[f'self.user_{i}'] = QtWidgets.QLabel(self.formLayoutWidget)
        #     # self.user_0 = QtWidgets.QLabel(self.formLayoutWidget)
        #     # globals()[f'self.user_{i}'].setObjectName(f"user_{i}")

        #     # self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, globals()[f'self.user_{i}'])
        #     globals()[f'self.check_{i}'] = QtWidgets.QCheckBox(self.formLayoutWidget)
        #     globals()[f'self.check_{i}'].setText("")
        #     globals()[f'self.check_{i}'].setObjectName(f"check_{i}")
        #     self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, globals()[f'self.check_{i}'])
        #     globals()[f'self.check_{i}'].show()
        #     print(globals()[f'self.check_{i}'])
        # if directory:
        #     for file_name in os.listdir(directory):
        #         self.listWidget.addItem(file_name)
        #  
        # self.model = QStandardItemModel()
        # self.tree_files.setModel(self.model)
        # directory = QtWidgets.QFileDialog.getExistingDirectory(caption = "Выберите папку")
        # if directory:
        #     for direc in os.listdir(directory):
        #         parent1 = QStandardItem(direc)
        #         if os.path.isdir(os.path.join(directory, direc)):
        #             for fil in os.listdir(os.path.join(directory, direc)):
        #                 parent2 = QStandardItem(fil)
        #                 parent1.appendRow(parent2)
        #                 if os.path.isdir(os.path.join(os.path.join(directory, direc), fil)):
        #                     for fil_1 in os.listdir(os.path.join(os.path.join(directory, direc), fil)):
        #                         parent3 = QStandardItem(fil_1)
        #                         parent2.appendRow(parent3)
        #                         if os.path.isdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
        #                             for fil_2 in os.listdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
        #                                 if not os.path.isdir(os.path.join(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1), fil_2)):
        #                                     parent4 = QStandardItem(fil_2)
        #                                     parent3.appendRow(parent4)
                # self.model.appendRow(parent1)
        # self.tree_files.show()
        

    def go_to_chat(self):
        self.hide()
        self.parent.show()
        # self.chats_window.show()

    def copy_link(self):
        try:
            response = req.get(url, data = {'return_link': self.tree_files.selectedIndexes()[0].data(), 'chat_id': self.parent.chat_id})
        except:
            return
        response = response.json()
        QApplication.clipboard().setText(f'{url}{response}')

    def pull_files(self):
        response = req.get(url, data = {'pull_files': self.parent.chat_id}).json()
        print(response)
        for dir in response:
            try:
                os.mkdir(os.path.join(self.directory, dir))
            except:
                pass
            info = response.get(dir)
            for file in info:
                for fil in file:
                    print(file)
                    with open(os.path.join(self.directory, os.path.join(dir, fil)), 'w') as fd:
                        fd.write(file.get(fil))
        # for dir, file in response.items():
            # try:
                # os.mkdir(dir)
            # except:
        # print(response)
                # pass
        

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        try:
            self.parent.timer.stop()
        except:
            pass
        with open('info.json', 'r') as fd:
            info = json.load(fd)
        if info.get('dir'):
            self.directory = info.get('dir')
            self.pref = os.path.basename(self.directory)
            self.lineEdit.setText(info.get('dir'))
        self.make_tree()
        # self.user_0.hide()
        # self.check_0.hide()
        # print(self.parent.users)
        for i, user in enumerate(self.parent.users):
            if i == 0 and user == self.parent.user_id:
                # if user == self.parent.user_id:
                continue
            elif i == 0 and not user == self.parent.user_id:
                self.label_3.hide()
                self.push_file_button_3.hide()
                break
            globals()[f'self.user_{i}'] = QtWidgets.QLabel(self.formLayoutWidget)
            # self.user_0 = QtWidgets.QLabel(self.formLayoutWidget)
            globals()[f'self.user_{i}'].setObjectName(f"user_{i}")
            globals()[f'self.user_{i}'].setText(user) 
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, globals()[f'self.user_{i}'])
            globals()[f'self.check_{i}'] = QtWidgets.QCheckBox(self.formLayoutWidget)
            globals()[f'self.check_{i}'].setText("")
            globals()[f'self.check_{i}'].setObjectName(f"check_{i}")
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, globals()[f'self.check_{i}'])
            # globals()[f'self.check_{i}'].show()
            # print(globals()[f'self.check_{i}'])
        self.user_id = self.parent.user_id
        self.isAlive = True
        # self.download_chats()
        # self.download_dialogs()
        self.select_dir_button.clicked.connect(self.browse_folder)
        self.back_button.clicked.connect(self.go_to_chat)
        self.push_file_button.clicked.connect(self.push_folder)
        self.copy_to_clip_button.clicked.connect(self.copy_link)
        self.pull_file_button.clicked.connect(self.pull_files)


class Chats(QtWidgets.QMainWindow, chats.Ui_MainWindow):
    def go_to_chat(self):
        try:
            self.chat = self.list_chats.selectedItems()[0].text()
            # print(self.chat)
            self.hide()
            # app = ExampleApp(self.user_id, self.chat)
            # app.show()
            self.isActive = False
            self.timer.stop()
            self.parent.__init__(self.user_id, self.chat)
            # self.parent.download_message()
            # self.parent.chat_id = self.chat
            self.parent.show()
        except:
            pass

    def append_chat(self):
        req.get(url, data = {'append_chat': self.new_chat.toPlainText(), 'user_id': self.user_id})
        self.list_chats.clear()
        self.new_chat.clear()
        self.download_chats()

    def append_dialog(self):
        pass
    
    def download_dialogs(self):
        pass
    
    def download_chats(self, reload = False):
        # self.list_chats.clear()
        if reload:
            self.list_chats.clear()
        response = req.get(url, data = {'return_chats': self.user_id})
        # try:
        chats = response.json()
        if not reload:
            for index, chat in enumerate(chats):
                try:
                    print(f'chat - {chat}, list_chat - {self.list_chats.item(index).text()}')
                    if not chat == self.list_chats.item(index).text():
                        self.download_chats(True)
                except:
                    self.download_chats(True)
        if reload:
            for chat in chats:
                self.list_chats.addItem(chat)
        if self.isActive:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.download_chats)
            self.timer.start(2000)
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
        # text = QApplication.clipboard().text()
        # print(text)
        # QApplication.clipboard().setText('hello')
        # self.b.insertPlainText(text + '\n')
        self.isActive = True
        self.download_chats(True)
        self.download_dialogs()
        self.change_chat_button.clicked.connect(self.go_to_chat)
        self.append_chat_button.clicked.connect(self.append_chat)
        # self


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
            self.users = info
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
            self.timer.start(1000)
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

    def change_to_files(self):
        self.hide()
        self.timer.stop()
        self.file_window = Files(self)
        self.file_window.show()

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
            self.go_to_files.clicked.connect(self.change_to_files)

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


import zipfile
from flask import Flask, jsonify, request, make_response, send_from_directory
import os
from json import dumps
import json, time
import telebot


app = Flask(__name__)

bot = telebot.TeleBot('1040052141:AAEH4aSf_s9k-Tx3i_-w8phuPUZWiSakvAQ')

PAUSE = time.time()

def all_files():
	return (os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), "files")))

# def check_files(files, hash_sum):
# 	with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files/' + files), 'r') as fd:
# 		text_file = fd.read()
# 		hash_file = hashlib.md5(text_file.encode('utf-8')).hexdigest()
# 		if (hash_file == hash_sum):
# 			return 'ok'
# 		else:
# 			return (text_file)

def return_message(chat_id):
    with open(f'chats/chat_{chat_id}/message.json', 'r') as fd:
        return json.load(fd)

def append_message(info):
    # print(info)
    global PAUSE
    user_id = info.get('user_id')
    chat_id = info.get('chat_id')
    text = info.get('text')
    with open(f'chats/chat_{chat_id}/message.json', 'r') as fd:
        dic = json.load(fd)
    new_message = {}
    chat = dic.get('message')
    new_message[user_id] = text

###
    # with open(f'users/user_{user_id}.json', 'r') as fd:
        # info = json.load(fd)
        # if info.get('telegram_id'):
    #         if time.time() - PAUSE >= 3:
            # bot.send_message(int(info.get('telegram_id')), f'НОВАЯ ГРУППА:\n{user_id} добавил вас в "{chat_id}"')
    #             # global PAUSE
    #             PAUSE = time.time()
###

    if '@channel' in text:
        membs = members_of_chats(chat_id)
        for cha in membs:
            with open(f'users/user_{cha}.json', 'r') as fd:
                info = json.load(fd)
                print(info.get('telegram_id'))
                if info.get('telegram_id'):
                    bot.send_message(int(info.get('telegram_id')), f'ВАЖНОЕ СООБЩЕНИЕ:\n{user_id} написал что то очень важное, отправив уведомление всем в "{chat_id}"')
                    # global PAUSE
                    PAUSE = time.time()
    chat.append(new_message)
    dic['message'] = chat
    with open(f'chats/chat_{chat_id}/message.json', 'w') as fd:
        fd.write(dumps(dic))

#####

def new_user_info(user_id):
    info = {
        'user_id': user_id,
        'chat_id': [],
        'secret_chat_id': [],
        'telegram_id': 0,
    }
    with open(f'users/user_{user_id}.json', 'w') as fd:
        fd.write(json.dumps(info))

#####

def read_user_info(user_id, dic=False):
    """
    {
        'name': 'MyName',
        'chat_id': [1, 2],
        'secret_chat_id': [15, 24],
        'telegram_id': '12333123123',
    }
    """
    with open(f'users/user_{user_id}.json', 'r') as fd:
        info = json.load(fd)
        if dic:
            return info
    return info.get('name'), info.get('chat_id'), info.get('secret_chat_id'), info.get('telegram_id')


def check_login(user_id):
    if os.path.exists(f'users/user_{user_id}.json'):
        return False
    new_user_info(user_id)
    # with open(f'users/user_{user_id}.json', 'w') as fd:
        # fd.write(dumps({'user_id': user_id}))
    return True

def members_of_chats(chat_id):
    """
    chat_id: [user_id, user_id]
    {
        1: [1, 2, 3, 4],
        2: [2, 3],
    }
    """
    with open(f'chats/members_of_chats.json', 'r') as fd:
        chat = json.load(fd)
    return chat.get(chat_id)

def change_user_info(user_id, chat_id=None, secret_chat_id=None, telegram_id=None):
    info = read_user_info(user_id, dic=True)
    if chat_id and chat_id not in info['chat_id']:
        info['chat_id'].append(chat_id)
    if secret_chat_id and secret_chat_id not in info['secret_chat_id']:
        info['secret_chat_id'].append(secret_chat_id)
    if telegram_id:
        info['telegram_id'] = telegram_id
    with open(f'users/user_{user_id}.json', 'w') as fd:
        fd.write(json.dumps(info))

def append_chat(user_id, chat_id):
    if os.path.exists(f'chats/chat_{chat_id}/message.json'):
        return dumps(False)
    change_user_info(user_id, chat_id=chat_id)
    try:
        os.mkdir(f'chats/chat_{chat_id}')
    except:
        pass
    try:
        os.mkdir(f'chats/chat_{chat_id}/files')
    except:
        pass
    with open(f'chats/chat_{chat_id}/access.json', 'w') as fd:
        fd.write(dumps([]))
    with open(f'chats/members_of_chats.json', 'r') as fd:
        info = json.load(fd)
    if info.get(chat_id):
        info[chat_id] = info.get(chat_id).append(user_id)
    else:
        info[chat_id] = [user_id]
    with open(f'chats/members_of_chats.json', 'w') as fd:
        fd.write(dumps(info))
    # try:
        # os.mkdir(f'chats/chat_{chat_id}')
    # except:
        # pass
    with open(f'chats/chat_{chat_id}/message.json', 'w') as fd:
        fd.write(dumps({"message": []}))

### TODO### TODO### TODO### TODO### TODO### TODO### TODO### TODO### TODO

def return_access(chat_id):
    with open(f'chats/chat_{chat_id}/access.json', 'r') as fd:
        return json.load(fd)

def check_access(chat_id, user_id):
    with open(f'chats/chat_{chat_id}/access.json', 'r') as fd:
        if user_id in json.load(fd):
            return True
    return False 

def append_access(data):
    # with open(f'chats/chat_{chat_id}/access.json', 'r') as fd:
        # info = json.load(fd)
    # info = list_users
    lis = []
    chat_id = data.get('chat_id')
    for key in data:
        if key != 'chat_id' and key != 'accept_append':
            lis.append(key)
    with open(f'chats/chat_{chat_id}/access.json', 'w') as fd:
        fd.write(json.dumps(lis))

### TODO### TODO### TODO### TODO### TODO### TODO### TODO### TODO### TODO### TODO

def append_to_chat(user_id, chat_id):
    if not os.path.exists(f'users/user_{user_id}.json'):
        return False
    if chat_id in read_user_info(user_id, dic = True).get('chat_id'):
        return False
    change_user_info(user_id, chat_id=chat_id)
    with open(f'users/user_{user_id}.json', 'r') as fd:
        info = json.load(fd)
        if info.get('telegram_id'):
            # if time.time() - PAUSE >= 3:
            bot.send_message(int(info.get('telegram_id')), f'НОВАЯ ГРУППА:\n{user_id} добавил вас в "{chat_id}"')
                # global PAUSE
                # PAUSE = time.time()
    # with open(f'chats/chat_{chat_id}/access.json', 'r') as fd:
        # info = json.load(fd)
    # info.append()
    # with open(f'chats/chat_{chat_id}/access.json', 'w') as fd:
        # fd.write(json.dumps(info))
    with open(f'chats/members_of_chats.json', 'r') as fd:
        info = json.load(fd)
    if info.get(chat_id):
        chats = info.get(chat_id)
        chats.append(user_id)
        info[chat_id] = chats
    else:
        info[chat_id] = [user_id]
    with open(f'chats/members_of_chats.json', 'w') as fd:
        fd.write(dumps(info))
    return True

def return_chats(user_id):
    with open(f'users/user_{user_id}.json', 'r') as fd:
        return json.load(fd).get('chat_id')

# def append_user_to_chat(user_id, chat_id):
    # if not os.path.exists(f'users/user_{user_id}.json'):
        # return False
    # change_user_info(user_id, chat_id=chat_id)
    
def return_tree_files(chat_id):
    info = {}
    directory = os.path.join(os.getcwd(), f'chats/chat_{chat_id}/files')
    if directory:
        info['parent2'] = []
        info['parent1'] = []
        info['parent3'] = []
        info['parent4'] = []
        for direc in os.listdir(directory):
            info['parent1'].append(direc)
            # parent1 = QStandardItem(direc)
            if os.path.isdir(os.path.join(directory, direc)):
                for fil in os.listdir(os.path.join(directory, direc)):
                    # parent2 = QStandardItem(fil)
                    info['parent2'].append(fil)
                    # parent1.appendRow(parent2)
                    if os.path.isdir(os.path.join(os.path.join(directory, direc), fil)):
                        for fil_1 in os.listdir(os.path.join(os.path.join(directory, direc), fil)):
                            # parent3 = QStandardItem(fil_1)
                            info['parent3'].append(fil_1)
                            # parent2.appendRow(parent3)
                            if os.path.isdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
                                for fil_2 in os.listdir(os.path.join(os.path.join(os.path.join(directory, direc), fil), fil_1)):
                                    # parent4 = QStandardItem(fil_2)
                                    info['parent4'].append(fil_2)
                                    # parent3.appendRow(parent4)
    print(info)
    return info


def pull_files(chat_id):
    folder = []
    retur = {}
    for i in os.walk(f'chats/chat_{chat_id}/files'):
        folder.append(i)
    for address, dirs, files in folder:
        if files:
            retur[address] = []
            try:
                retur[address.split('files')[1]] = []
            except:
                pass
        for file in files:
            with open(os.path.join(address, file), 'r') as fd:
                try:
                    retur[address.split('files')[1]].append({file: fd.read()})
                except:
                    pass
    return retur

def return_link(chat_id, filename):
    folder = []
    for i in os.walk(f'chats/chat_{chat_id}/files'):
        folder.append(i)
    for address, dirs, files in folder:
        if filename in dirs:
            return (chat_id + (address+ '/' + dirs[0]).split('files')[1]).replace('\\', '/')
        for file in files:
            if file == filename:
                return (chat_id + (address+ '/' +file).split('files')[1]).replace('\\', '/')

def download_files(data):
    chat_id = data.get('chat_id')
    user_id = data.get('user_id')
    with open(f'users/user_{user_id}.json', 'r') as fd:
        info = json.load(fd)
        if info.get('telegram_id'):
    #         if time.time() - PAUSE >= 3:
            bot.send_message(int(info.get('telegram_id')), f'ИЗМЕНЕНИЯ ФАЙЛОВ:\n{user_id} только что запушил файлы в "{chat_id}"')
            # PAUSE = time.time()
    # try:
        # os.mkdir(f'chats/chat_{chat_id}/files/{data.get("name")}')
    # except:
        # pass
    # print(data)
    for fil, content in data.items():
        if fil == 'name' or fil == 'chat_id':
            continue
        # print(f'chats/chat_{chat_id}/files/{fil}')
        with open(f'chats/chat_{chat_id}/files/{fil}', 'w') as fd:
            fd.write(content)

#####

# @app.route('/<st>/')
# def question(st):
    # with open()
    # pass
    # with open(f'chats/chat_{st}/message.json') as fd:
        # return fd.read()
    # return 'https://127.0.0.1:5000/chats/chat_{st}/message.json'
    # link = f'https://127.0.0.1:5000/chats/{st}/message.json'
    # return render_template(f'<h1> {str_key} </h1>', link=link)
    # return render_template('question.html', link=link)

@app.route('/<chat_id>/<dir>/<one_more>/<lol>/<filename>')
def uplo_file(chat_id, dir, one_more, lol, filename):
    # print(f'chat_{chat_id}/files/{filename}')
    if not '.' in filename:
        zipf = zipfile.ZipFile(f'{filename}.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir(os.path.join(f'chats/chat_{chat_id}/files/{dir}/{one_more}/{lol}/', filename), zipf)
        zipf.close()
        return send_from_directory('./', f'{filename}.zip')
    return send_from_directory(f'chats/chat_{chat_id}/files/{dir}/{one_more}/{lol}/',
                               filename)

@app.route('/<chat_id>/<dir>/<one_more>/<filename>')
def uploa_file(chat_id, dir, one_more, filename):
    # print(f'chat_{chat_id}/files/{filename}')
    if not '.' in filename:
        zipf = zipfile.ZipFile(f'{filename}.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir(os.path.join(f'chats/chat_{chat_id}/files/{dir}/{one_more}/', filename), zipf)
        zipf.close()
        return send_from_directory('./', f'{filename}.zip')
    return send_from_directory(f'chats/chat_{chat_id}/files/{dir}/{one_more}/',
                               filename)

@app.route('/<chat_id>/<dir>/<filename>')
def upload_file(chat_id, dir, filename):
    # print(f'chat_{chat_id}/files/{filename}')
    if not '.' in filename:
        zipf = zipfile.ZipFile(f'{filename}.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir(os.path.join(f'chats/chat_{chat_id}/files/{dir}/', filename), zipf)
        zipf.close()
        return send_from_directory('./', f'{filename}.zip')
    return send_from_directory(f'chats/chat_{chat_id}/files/{dir}/',
                               filename)

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

@app.route('/<chat_id>/<filename>')
def uploaded_file(chat_id, filename):
    # print(f'chat_{chat_id}/files/{filename}')
    if not '.' in filename:
        zipf = zipfile.ZipFile(f'{filename}.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir(os.path.join(f'chats/chat_{chat_id}/files', filename), zipf)
        zipf.close()
        return send_from_directory('./', f'{filename}.zip')
    return send_from_directory(f'chats/chat_{chat_id}/files/',
                               filename)

@app.route('/', methods=['GET', 'POST'])
def echo():
    command = request.data.decode("utf-8")
    # if command.get('')
    command = request.form.to_dict()
    # print(command)
    
    if command.get('pull_files'):
        return make_response(dumps(pull_files(command.get('pull_files'))))

    if command.get('return_link'):
        return make_response(dumps(return_link(command.get('chat_id'), command.get('return_link'))))

    if command.get('tree'):
        return make_response(dumps(return_tree_files(command.get('tree'))))

    if command.get('name'):
        # info = command.get('name')
        download_files(command)

    if command.get('new_message'):
        info = command.get('new_message')
        append_message(command)
        return make_response(dumps(True))

    if command.get('return_accept'):
        return make_response(dumps(return_access(command.get('return_accept'))))

    if command.get('accept_append'):
        append_access(command)

    if command.get('check_enable'):
        user_id = command.get('check_enable')
        chat_id = command.get('chat_id')
        return make_response(dumps(check_access(chat_id, user_id)))

    if command.get('check_login'):
        user_id = command.get('check_login')
        check = check_login(user_id)
        return make_response(dumps(check))
    
    if command.get('read_message'):
        return make_response(dumps(return_message(command.get('read_message'))))

    if command.get('append_chat'):
        user_id = command.get('user_id')
        chat_id = command.get('append_chat')
        append_chat(user_id, chat_id)

    if command.get('return_users'):
        chat_id = command.get('return_users')
        return make_response(dumps(members_of_chats(chat_id)))

    if command.get('append_user_to_chat'):
        user_id = command.get('append_user_to_chat')
        chat_id = command.get('chat_id')
        return make_response(dumps(append_to_chat(user_id, chat_id)))

    if command.get('return_chats'):
        return make_response(dumps(return_chats(command.get('return_chats'))))
        # user_id = info.get('user_')

    if command.get('append_to_chat'):
        info = command.get('append_to_chat')
        user_id = info[0]
        chat_id = info[1]
        append_chat(user_id, chat_id)

    return '<h1> К апишке может подключится любой у кого есть доступ к wi-fi </h1>'

    files = all_files()
    if command.get('files'):
        return make_response(dumps(files))
    

    # a = request.form.to_dict()
    # for key in a:
    #     if key in files:
    #         check = check_files(key, a.get(key))
    #         a[key] = check
    #     else:
    #         return 'ko'
    # if (a):
    #     return (a)
    # else:
    #     return 'ko'

app.run(host='192.168.1.56', port='33')

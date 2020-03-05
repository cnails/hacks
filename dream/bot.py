import json

"""
info = {
    1 : [ { 1: 'hello' }, {1 : 'nice'} ],
    2 : [ { 3: 'nice' }, {4 : 'hello'} ],
    # 2 : 'test',
    # 3 : 'nice',
}
"""
# with open('test.json', 'w') as fd:
    # fd.write(json.dumps())

# with open('test.json', 'r') as fd:
    # dic = json.load(fd)
    # print(dic)
    # for chat_id, char_mes in dic.items():
    #     print(f'chat_id = {chat_id}')
    #     for user_mes in char_mes:
    #         for user_id, text_mes in user_mes.items():
    #             ...
    #         print(f'{user_id} - {text_mes}')

def new_user_info(user_id):
    info = {
        'user_id': user_id,
        'chat_id': [],
        'secret_chat_id': [],
        'telegram_id': 0,
    }
    with open(f'users/user_{user_id}.json', 'w') as fd:
        fd.write(json.dumps(info))

def change_user_info(user_id, chat_id=None, secret_chat_id=None, telegram_id=None):
    info = read_user_info(user_id, dic=True)
    if chat_id:
        info['chat_id'].append(chat_id)
    if secret_chat_id:
        info['secret_chat_id'].append(secret_chat_id)
    if telegram_id:
        info['telegram_id'] = telegram_id
    with open(f'users/user_{user_id}.json', 'w') as fd:
        fd.write(jsom.dumps(info))

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

def read_messages(chat_id):
    # for chat_id, char_mes in dic.items():
        # print(f'chat_id = {chat_id}')
        # for user_mes in char_mes:
            # for user_id, text_mes in user_mes.items():
                # ...
            # print(f'{user_id} - {text_mes}')

def write_message(chat_id, user_id, text):
    with open(f'chats/chat_{chat_id}/messages.json', 'w') as fd:
        dic = json.load(fd)
    new_message = {}
    chat = dic.get(chat_id)
    new_message[user_id] = text
    chat.append(new_message)
    dic[chat_id] = chat

# while True:
#     chat_id = input('chat_id = ')
#     if chat_id == '':
#         break
#     user_id = input('user_id = ')
#     text = input('text = ')
#     write_message(chat_id, user_id, text)

# print(dic)
# read_all_mes()

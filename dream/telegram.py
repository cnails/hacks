import telebot, os, json

bot = telebot.TeleBot('1040052141:AAEH4aSf_s9k-Tx3i_-w8phuPUZWiSakvAQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message.chat.id)
    # bot.send_message(message.chat.id, 'Привет, напиши свой логин, чтобы я мог отправлять тебе уведомления')
    bot.send_message(message.chat.id, 'Уведомления подключены')

@bot.message_handler(content_types=['text'])
def read_message(message):
    # if os.path.exists(f'stop_spam/{message.chat.id}.desk'):
        # bot.send_message(message.chat.id, 'Вы уже подключили уведомления')
    # if len(message.text) < 3:
        # bot.send_message(message.chat.id, 'Пожалуйста, укажите свой логин')
        # return
    bot.send_message(message.chat.id, 'Уведомления подключены')
    # print(message.chat.id)
    # telegram_id = message.text
    # if not os.path.exists(f'users/user_{telegram_id}.json'):
        # bot.send_message(message.chat.id, 'Проверьте логин и отправьте сообщение снова')
        # return
    # with open(f'users/user_{telegram_id}.json', 'r') as fd:
        # info = json.load(fd)
    # with open(f'stop_spam/{message.chat.id}.desk', 'w') as fd:
        # pass
    # info['telegram_id'] = message.chat.id
    # with open(f'users/user_{telegram_id}.json', 'w') as fd:
        # fd.write(json.dumps(info))
    # bot.send_message(message.chat.id ,'Уведомления подключены!')

print('start')
bot.polling()

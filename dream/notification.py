import telebot, json, os
# from bot import members_of_chats

# bot = telebot.TeleBot('1041190715:AAFAP8UnMiQznA2ea1GG2iAg9laYiY9yb8E')
# bot = telebot.TeleBot('1040052141:AAEH4aSf_s9k-Tx3i_-w8phuPUZWiSakvAQ')

def bot_send_notif(bot, telegram_id, text):
    bot.send_message(telegram_id, text)

def bot_send_notif_groups(bot, chat_id, text, members):
    # members = members_of_chats(chat_id)
    for user_id in members:
        with open(f'users/user_{user_id}.json', 'r') as fd:
            info = json.load(fd)
        telegram_id = int(info.get('telegram_id'))
        if telegram_id:
            bot_send_notif(telegram_id, text)

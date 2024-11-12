import telebot
import config

# from landing_page.models import UserContacts

bot = telebot.TeleBot(config.bot_token)
chat_id = config.my_id

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Я буду присылать вам контакты, каждый раз, когда их оставят через форму вашего сайта')

def send_contact_to_telegram(name, phone_number):
    bot.send_message(chat_id, f"<strong>Новый контакт</strong>\nИмя: <b>{name}</b>\nНомер: <b>{phone_number}</b>", parse_mode='html')




# @bot.message_handler(commands=[])
# def send_contact(name, phone_number):
#     bot.send_message(chat_id, f'{name}, {phone_number}')

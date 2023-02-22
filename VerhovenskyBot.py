import telebot

bot = telebot.TeleBot('6196881154:AAEyeS3nAfSQnrGlmAEaFytutdsdMbWH9yY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id,mess, 'Здравствуйте, я бот Ивана, принимаю сообщения и передаю их создателю', parse_mode='html')

bot.polling(non_stop=True)
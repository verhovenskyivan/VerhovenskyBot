import telebot

bot = telebot.TeleBot('6196881154:AAEyeS3nAfSQnrGlmAEaFytutdsdMbWH9yY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id,mess, 'Здравствуйте, я бот Ивана, принимаю сообщения и передаю их создателю', parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id,"И тебе привет", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой id:{message.from_user}")
    elif message.text == "photo":
        photo = open('icon.png','rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "audio":
        audio = open('/tmp/audio.mp3', 'rb')
        bot.send_audio(message.chat_id, audio)
        bot.send_audio(message.chat_id, "FILEID")
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Интересное фото')

    
bot.polling(non_stop=True)
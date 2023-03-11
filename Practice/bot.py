import telebot
import requests
from telebot import util
from telebot import types
from telebot import apihelper

apihelper.API_URL = "http://localhost:4200/bot{0}/{1}"

bot = telebot.TeleBot("6067029581:AAE7krVg-J-n03RCA3fSMmQtDX2D1pFJvQg")

@bot.message_handler(commands=['start'])
async def start(message):
   await bot.send_message(message.chat.id, 'Здравствуйте, я бот Ивана, принимаю сообщения и передаю их создателю',)

@bot.message_handler(commands=['info'])
async def info(message):
    await bot.send_message(message.chat.id, 'Меня зовут Иван Верховенский, увлекаюсь разработкой, работаю системным администратором и хочу стать DevOps инженером')

@bot.message_handler(commands=["get"])
async def get(message):
    await bot.send_document
    
@bot.message_handler(commands=['help'])
async def help(message):
    await bot.send_message(message.chat.id, 'Что вы хотите узнать?')

@bot.message_handler(commands="send")
async def send(message):
    await bot.get_file()
        
@bot.message_handler(commands=["sticker"])
async def sticker(message):
    await bot.send_sticker()
          
@bot.message_handler(commands=["resume"])
async def resume(message):
    await bot.send_document()

@bot.message_handler(commands=["random"])
async def help(message):
    await bot.send_message
    
@bot.message_handler(commands=["Gachi"])
async def Gachi(message):
    await bot.send_photo(message.chat.id) 
    updates = bot.get_updates(offset= 100,limit= 100,timeout=0)

@bot.message_handler(commands=["Type"])
async def Type(message):
    await bot.send_poll()
        
@bot.poll_answer_handler()

@bot.inline_handler(lambda query: query.query == "text")
async def query_text(inline_query):
    await bot.send_message()

@bot.message_handler(commands=['help'])
async def help(message):
    await bot.send_message(message.chat.id, 'Что вы хотите узнать?')

@bot.message_handler()
async def get_user_text(message):
    if  message.text == "Привет" or "ПРИВЕТ" or "привет":
        await bot.send_message(message.chat.id,"И тебе привет", )
    elif message.text == "Информацию":
        await bot.send_message(message.chat.id,f"Меня зовут Иван Верховенский, увлекаюсь разработкой, работаю системным администратором и хочу стать DevOps инженером   "  
                          f"Что-то еще?")
    else:
        await bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler()
async def get_user_doc(message):
    if message.text == "Резюме" or "РЕЗЮМЕ":
       await bot.send_document(message.chat.id, "file:///C:/Users/verhovensky/Downloads/%D0%92%D0%B5%D1%80%D1%85%D0%BE%D0%B2%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%98%D0%B2%D0%B0%D0%BD.pdf")

@bot.message_handler(content_types=['photo'])
async def get_user_photo(message):
    await bot.send_message(message.chat.id, 'Интересное фото')
 
@bot.message_handler(commands=['help'])
async def help(message):
    start = types.KeyboardButton('Start')
    help = types.KeyboardButton('Help')
    
@bot.message_handler()
async def upload_photo(message): 
    upload_photo = get_user_photo;  
    await bot.send_chat_action(message.chat.id,action=upload_photo)
    
@bot.message_handler()
async def file_downloader(get_file, message):
    get_file = file_downloader
    await bot.get_file(get_file.message.chat.id, get_file)

@bot.message_handler(func=lambda m: True)
async def echo_all(message):
	await bot.reply_to(message, message.text)

bot.infinity_polling()

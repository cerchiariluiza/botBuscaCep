#--coding: utf-8 --
import telebot #importar a lib do telegram pyTelegramBotApi

API_TOKEN='1504662549:AAG10Gd56WtXff-PHat9KLUMLKN9XwXpAyo' #api gerada pelo BotFather

bot.telebot.TeleBot(API_TOKEN) #sumário-sumário e Tele Bot(comando) aplicando token

#Inicio

@bot.message_handler(commands=['start']) # recebo mensagem /start
def send_welcome(message):
	msg= bot.reply_to(message, "Olá, este é um bot criado pela Lu") #mensagem enviada para o usuario
	
bot.polling() #escutador

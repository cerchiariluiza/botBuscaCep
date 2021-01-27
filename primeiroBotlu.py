#--coding: utf-8 --
import telebot #importar a lib do telegram pyTelegramBotApi
from telebot import types
API_TOKEN= '1504662549:AAG10Gd56WtXff-PHat9KLUMLKN9XwXpAyo' #api gerada pelo BotFather

bot = telebot.TeleBot(API_TOKEN) #sumário-sumário e Tele Bot(comando) aplicando token

#Inicio

@bot.message_handler(commands=['start']) # recebo mensagem /start
def send_welcome(message):
	cid = message.chat.id #pegar id da conversa
	msg= bot.reply_to(message, "Olá, este é um bot criado pela Luu. \n Nosso id é " + str(cid)) #mensagem enviada para o usuario
	bot.send_message(cid, "Caso você precise de ajuda, use a função /ajuda")
	
#ajuda
@bot.message_handler(commands=['ajuda'])
def send_help(message):
	cid = message.chat.id 
	msg_help = bot.reply_to(message, "Você não se lembra das funções: \n Opcão 1: /cadastro, \n Opção 2: /categoria, \n Opção 3: /contato")
	bot.send_message(cid, "Caso você precise de ajuda, envie um e-mail para fale_conosco@nw.br")
	
#categoria
@bot.message_handler(commands=['categoria'])
def send_help(message):
	cid = message.chat.id 
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) #crio o layout de opções, digo pra ele que só pode selecionar uma opção	
	markup.add('Pentest', 'Infiltração') #opções que aparecem ao cliente
	msg_cat = bot.reply_to(message, "Escolha a categoria desejada: ", reply_markup=markup) # qual categoria ele vai querer
	
	
bot.polling() #escutador

#--coding: utf-8 --
import telebot
import json
import urllib.request
import urllib #tratar urls de json, http
API_TOKEN= '1504662549:AAG10Gd56WtXff-PHat9KLUMLKN9XwXpAyo'
bot = telebot.TeleBot(API_TOKEN) #sumário-sumário e Tele Bot(comando) aplicando token

#Inicio



@bot.message_handler(commands=['cep']) # recebo cep

def send_cep(message):
	msg = bot.reply_to(message, "Digite o cep")
	cid = message.chat.id #pegar id da conversa
	bot.register_next_step_handler(msg, send_cep_step) #armazena a info digitada e joga aoprox passo def send_cep_step
	
def send_cep_step(message):
	cid = message.chat.id #pegar id da conversa
	mensagem_cep=message.text
	url = "https://viacep.com.br/ws/" + mensagem_cep +"/json/"
	response = urllib.request.urlopen(url) #abrir a url, ou sej,a abrir o json
	data = json.loads(response.read()) #json load carrega o json e ler os valores do json
	print (data)
	
	cep = data["cep"]
	logradouro = data["logradouro"]
	bairro = data['complemento']
	localidade = data['localidade']
	uf = data['uf']
	bot.send_message(cid, "CEP" + cep + "\nLogradouro" + logradouro + "\nBairro" + bairro + "uf" + uf) 
	
bot.polling()

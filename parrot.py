import telebot
import config

bot = telebot.Telebot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def parrot(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
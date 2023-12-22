import telebot
import info
token = ""

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start']) #/start
def repeat_message(message):
      bot.send_message(705359495, "Здравствуйте.\nЭто бот-визитка, в нём вы узнаете информацию обо мне.")
      bot.send_message(705359495, "Чтобы узнать все команды, напишите /help")

@bot.message_handler(commands=['help']) #/help
def repeat_message(message):
      bot.send_message(705359495, "/help - узнать все команды\n/about - узнать информацию обо мне\n/hobby - узнать мои увлечения")

@bot.message_handler(commands=['about']) #/about
def repeat_message(message):
      bot.send_message(705359495, info.show_about())

@bot.message_handler(commands=['hobby']) #/hobby
def repeat_message(message):
      bot.send_message(705359495, info.show_hobby(), parse_mode= "Markdown")

@bot.message_handler(content_types=['text'])
def repeat_message(message):
      bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['photo'])
def repeat_message(message):
      bot.send_photo(message.chat.id, message.photo[0].file_id)

bot.polling()
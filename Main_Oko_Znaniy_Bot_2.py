from telegram import ReplyKeyboardMarkup, Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from Oko_Znaniy_Bots_token import bot_token
import random
import wikipedia
q1=""
bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher
otvet_list=["Да","Возможно","Нет"]
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Задайте мне любой вопрос о будущем. А я отвечу.")
    context.bot.send_message(update.effective_chat.id, "(Возможно я не прав ведь ваша судьба в ваших руках)")
def vechnie_znania(update, context):
    if update.message.text == "Все":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Это ничего...")
    else:
        for i in range(0,50):
            for w in range(0,30):
                print(i+w)
        context.bot.send_message(update.effective_chat.id, "Думаю...")
        context.bot.send_message(update.effective_chat.id, otvet_list[random.randint(0, len(otvet_list)-1)])
vopros_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, vechnie_znania)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(vopros_handler)
updater.start_polling()
updater.idle()
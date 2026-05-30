from telegram import ReplyKeyboardMarkup, Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from Oko_Znaniy_Bots_token import bot_token
import random
import wikipedia
command_list=["/start", "/help", "/language", "/vechnoe_znanie", "/vechnoe_znanie_file", "/future"]
otvet_list=["Да","Возможно","Нет"]
bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher
def lang(update, context):
    wikipedia.set_lang(context.args[0])
def start(update, context):
    context.bot.send_message(update.effective_chat.id, text="Здравствуйте уважаемый гость!")
    context.bot.send_message(update.effective_chat.id, text="Для просмотра моих способностей введите /help")
def helper(update, context):
    context.bot.send_message(update.effective_chat.id, command_list)
def vechnoe_znanie(update, context):
    print(context.args[0])
    i=" ".join(context.args)
    znanie = wikipedia.summary(i)
    context.bot.send_message(update.effective_chat.id, znanie)
def vechnoe_znanie_sentences(update, context):
    print(context.args[0])
    in_chat = wikipedia.summary(context.args[0], context.args[1])
def vechnoe_znanie_file(update, context):
    print(context.args[0])
    in_file = wikipedia.summary(context.args[0])
    file_wiki = open('find_result.txt', 'w', encoding="utf-8")
    file_wiki.write(in_file)
    file_wiki.close()
    in_chat = in_file.split(".")[0]
    context.bot.send_message(update.effective_chat.id, in_chat)
    sending_file = open('find_result.txt', 'rb')
    context.bot.send_document(update.effective_chat.id, sending_file)
    sending_file.close()
def future(update, context):
    if update.message.text == "Все":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Это ничего...")
    else:
        for i in range(0,50):
            for w in range(0,30):
                print(i+w)
        context.bot.send_message(update.effective_chat.id, "Думаю...")
        context.bot.send_message(update.effective_chat.id, otvet_list[random.randint(0, len(otvet_list)-1)])



start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
helper_handler = CommandHandler("help", helper)
dispatcher.add_handler(helper_handler)
znanie1_handler = CommandHandler('vechnoe_znanie_sentences', vechnoe_znanie_sentences)
dispatcher.add_handler(znanie1_handler)
znanie2_handler = CommandHandler('vechnoe_znanie', vechnoe_znanie)
dispatcher.add_handler(znanie2_handler)
znanie3_handler = CommandHandler('vechnoe_znanie_file', vechnoe_znanie_file)
dispatcher.add_handler(znanie3_handler)
lang_handler = CommandHandler('language', lang)
dispatcher.add_handler(lang_handler)
fut_handler = CommandHandler('future', future)
dispatcher.add_handler(fut_handler)
updater.start_polling()
updater.idle()
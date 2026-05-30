from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Voithos_Bots_token import bot_token
import random
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
list_greeting = ['Приветствую', 'Добрый день!', 'Здравствуйте', 'Привет!', '???', '!}!', 'Чем я могу помочь?']
otvet_list=["Да","Возможно","Нет"]
command_list=["/start", "/help", "/sum", "/min", "/umn", "/del", "/count", "/eho", "/avtor", "/vopros",  "/random_ot_0_do_10", "/timer"]
def start(update, context):
    context.bot.send_message(update.effective_chat.id, list_greeting[random.randint(0, len(list_greeting)-1)])
def helper(update, context):
    context.bot.send_message(update.effective_chat.id, command_list)
def count(update, context):
    context.bot.send_message(update.effective_chat.id, "Считать по символам или по пробелам?")
    
def plus(update, context):
    spell=int(context.args[0])
    q=0
    w=int(len(str(spell)))/2
    e=-1
    a9=int(str(spell)[q:w])+int(str(spell)[w:e])
    context.bot.send_message(update.effective_chat.id, a9)
def minus(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите 2 числа разными сообщениями")
    update.message.text=a10
    update.message.text=a11
    a12=int(a10)/int(a11)
    context.bot.send_message(update.effective_chat.id, a12)
def umnozhenie(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите 2 числа разными сообщениями")
    update.message.text=a1
    update.message.text=a2
    a3=int(a2)*int(a1)
    context.bot.send_message(update.effective_chat.id, a3)
def delenie(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите 2 числа разными сообщениями")
    update.message.text=a4
    update.message.text=a5
    a6=int(a4)/int(a5)
    context.bot.send_message(update.effective_chat.id, a6)
def eho(update, context):
    context.bot.send_message(update.effective_chat.id, "Для остоновки режима эхо напишите stop")
    while update.message.text!="stop":
        a=update.message.text
        context.bot.send_message(update.effective_chat.id, a)
def avtor(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создал ...")
    context.bot.send_message(update.effective_chat.id, "Простите, кажется я забыл :)")
def vopros(update, context):
    context.bot.send_message(update.effective_chat.id, "Задайте мне любой вопрос о будущем, прошлом и настоящем. А я отвечу.")
    context.bot.send_message(update.effective_chat.id, "(Возможно я не прав)")
    due=30
    context.job_queue.run_once(due, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, otvet_list[random.randint(0, len(otvet_list)-1)])
def rand(update, context):
    context.bot.send_message(update.effective_chat.id, "Рандомное число от 0 до 10:")
    context.bot.send_message(update.effective_chat.id, random.randint(0,11))
#def message(update, context):
    #if update.message.text == "Voithos_Bot":
        #context.bot.send_message(chat_id=update.effective_chat.id, text="Я знаю это слово - это я!")
    #else:
        #context.bot.send_message(chat_id=update.effective_chat.id, text="Я пока тебя не совсем понимаю, но скоро научусь")
def alarm(context):
    job = context.job
    context.bot.send_message(job.context, '!!!Время вышло!!!')
def set_timer(update, context):
    due = int(context.args[0])
    if due < 0:
        context.bot.send_message(update.effective_chat.id, 'Нельзя ставить таймер меньше 0 секунд')
        return
    context.job_queue.run_once(alarm, due, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, 'Таймер установлен')

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
helper_handler = CommandHandler("help", helper)
dispatcher.add_handler(helper_handler)
umnozhenie_handler = CommandHandler("umn", umnozhenie)
dispatcher.add_handler(umnozhenie_handler)
plus_handler = CommandHandler("sum", plus)
dispatcher.add_handler(plus_handler)
minus_handler = CommandHandler("min", minus)
dispatcher.add_handler(minus_handler)
delenie_handler = CommandHandler("del", delenie)
dispatcher.add_handler(delenie_handler)
eho_handler = CommandHandler("eho", eho)
dispatcher.add_handler(eho_handler)
avtor_handler = CommandHandler("avtor", avtor)
dispatcher.add_handler(avtor_handler)
vopros_handler = CommandHandler("vopros", vopros)
dispatcher.add_handler(vopros_handler)
rand_handler = CommandHandler("random_ot_0_do_10", rand)
dispatcher.add_handler(rand_handler)
set_handler = CommandHandler("timer", set_timer)
dispatcher.add_handler(set_handler)
#message_handler = MessageHandler(Filters.text, message)
#dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()

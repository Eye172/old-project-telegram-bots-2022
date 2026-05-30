from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Validator_Bots_token import bot_token
bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
command_list=["/start", "/help", "/timer", "/check_password", "count(Любой текст без /)"]
list_greeting = ['Приветствую', 'Добрый день!', 'Здравствуйте', 'Привет!', '???', '!}!', 'Чем я могу помочь?']
def start(update, context):
    context.bot.send_message(update.effective_chat.id, list_greeting[random.randint(0, len(list_greeting)-1)])
def helper(update, context):
    context.bot.send_message(update.effective_chat.id, command_list)
def validator(password):
    t = len(password)
    if t < 8:
        return "Ваш пароль слишком короткий"
    for i in range(t):
        if password[i].isdigit():
            return "Ваш пароль безопасен"
    return "Не хватает цифр"
def validate(update, context):
    p=context.args[0]
    context.bot.send_message(update.effective_chat.id, validator(p))
def alarm(context):
    job = context.job
    while due!="/stop":
        context.bot.send_message(job.context, '!!!Время вышло!!!')
def set_timer(update, context):
    due = int(context.args[0])
    if due < 0:
        context.bot.send_message(update.effective_chat.id, 'Нельзя ставить таймер меньше 0 секунд')
        return
    context.job_queue.run_once(alarm, due, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, 'Таймер установлен')
    
def count(update, context):
    context.bot.send_message(update.effective_chat.id, str(int(len(update.message.text.split(' ')))))

validator_handler=CommandHandler("check_password", validate)
dispatcher.add_handler(validator_handler)
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
helper_handler = CommandHandler("help", helper)
dispatcher.add_handler(helper_handler)
set_handler = CommandHandler("timer", set_timer)
dispatcher.add_handler(set_handler)
count_handler = MessageHandler(Filters.text, count)
dispatcher.add_handler(count_handler)
updater.start_polling()
updater.idle()
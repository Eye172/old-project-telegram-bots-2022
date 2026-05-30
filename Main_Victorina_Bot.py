from telegram import Bot, Poll
from telegram.ext import Updater, CommandHandler, PollAnswerHandler, PollHandler
import random
from Victorina_Bots_token import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

def quiz(update, context):
    q0=random.randint(0,100)
    w0=random.randint(0,100)
    questions = [str(q0+w0), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100))]
    update.effective_message.reply_poll(str(q0)+"+"+str(w0)+"=...", questions, type=Poll.QUIZ, correct_option_id=0, is_anonymous=False)
    q0=random.randint(0,100)
    w0=random.randint(0,100)
    questions = [str(random.randint(0,100)+random.randint(0,100)), str(q0+w0), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100))]
    update.effective_message.reply_poll(str(q0)+"+"+str(w0)+"=...", questions, type=Poll.QUIZ, correct_option_id=1, is_anonymous=False)
    q0=random.randint(0,100)
    w0=random.randint(0,100)
    questions = [str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)), str(q0+w0), str(random.randint(0,100))]
    update.effective_message.reply_poll(str(q0)+"+"+str(w0)+"=...", questions, type=Poll.QUIZ, correct_option_id=3, is_anonymous=False)
    q0=random.randint(0,100)
    w0=random.randint(0,100)
    questions = [str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(q0+w0), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100))]
    update.effective_message.reply_poll(str(q0)+"+"+str(w0)+"=...", questions, type=Poll.QUIZ, correct_option_id=2, is_anonymous=False)
    q0=random.randint(0,100)
    w0=random.randint(0,100)
    questions = [str(random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(random.randint(0,100)+random.randint(0,100)), str(q0+w0)]
    update.effective_message.reply_poll(str(q0)+"+"+str(w0)+"=...", questions, type=Poll.QUIZ, correct_option_id=4, is_anonymous=False)

quiz_handler = CommandHandler('quiz', quiz)
dispatcher.add_handler(quiz_handler)

updater.start_polling()
updater.idle()


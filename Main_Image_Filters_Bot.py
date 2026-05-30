from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from Image_Filters_Bot_token import bot_token
import random
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageFilter
from easygui import *
import sys

q1=0
q2=0
q3=0

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher
command_list=["/start", "/help", "/image", "/blur", "/detail", "/contour", "/emboss", "/smooth", "/edge_enhance", "/sharpen", "/white_black", "/negativ", "/random_filter", "/brightness", "/sunset","/aliy", "/custom_filter"]

def start(update, context):
    context.bot.send_message(update.effective_chat.id, text="Здравствуйте уважаемый пользователь бота Image_Filters_Bot")
    context.bot.send_message(update.effective_chat.id, text="Для просмотра команд бота введите /help")
    
def helper(update, context):
    context.bot.send_message(update.effective_chat.id, command_list)

def image1(update, context):
    img = update.message.photo[-1].get_file()
    img.download('user_image.jpg')
    context.bot.send_message(update.effective_chat.id, text="Картинка сохранена")

def image2(update, context):
    context.bot.send_message(update.effective_chat.id, text="Отправьте картинку")
def BLUR(update, context):
    img=Image.open("user_image.jpg")
    img = img.filter(ImageFilter.BLUR)
    img.save("user_image_"+"BLUR.jpg")
    sending_img = open("user_image_"+"BLUR.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def DETAIL(update, context):
    img=Image.open("user_image.jpg")
    img = img.filter(ImageFilter.DETAIL)
    img.save("user_image_"+"DETAIL.jpg")
    sending_img = open("user_image_"+"DETAIL.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def CONTOUR(update, context):
    img=Image.open("user_image.jpg")
    img=img.filter(ImageFilter.CONTOUR)
    img.save("user_image_"+"CONTOUR.jpg")
    sending_img = open("user_image_"+"CONTOUR.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def EMBOSS(update, context):
    img=Image.open("user_image.jpg")
    img = img.filter(ImageFilter.EMBOSS)
    img.save("user_image_"+"EMBOSS.jpg")
    sending_img = open("user_image_"+"EMBOSS.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def SMOOTH(update, context):
    img=Image.open("user_image.jpg")
    img = img.filter(ImageFilter.SMOOTH)
    img.save("user_image_"+"SMOOTH.jpg")
    sending_img = open("user_image_"+"SMOOTH.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def EDGE_ENHANCE(update, context):
    img=Image.open("user_image.jpg")
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    img.save("user_image_"+"EDGE_ENHANCE.jpg")
    sending_img = open("user_image_"+"EDGE_ENHANCE.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def SHARPEN(update, context):
    img=Image.open("user_image.jpg")
    img = img.filter(ImageFilter.SHARPEN)
    img.save("user_image_"+"SHARPEN.jpg")
    sending_img = open("user_image_"+"SHARPEN.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
def filter1(update, context):
    source=Image.open("user_image.jpg")
    width,height=source.size
    result=Image.new("RGBA",(width,height))
    for w in range(width):
        for h in range(height):
            r,g,b=source.getpixel((w, h))
            gray=int(r*0.212+g*0.715+b*0.0746)
            result.putpixel((w,h),(gray,gray,gray,255))
    result.save("user_image_"+"white_black.png")
    sending_img = open("user_image_"+"white_black.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
    
def filter2(update, context):
    source=Image.open("user_image.jpg")
    width,height=source.size
    result=Image.new("RGBA",(width,height))
    for w in range(width):
        for h in range(height):
            r,g,b=source.getpixel((w, h))
            result.putpixel((w,h),(255-r,255-g,255-b,255))
    result.save("user_image_"+"negativ.png")
    sending_img = open("user_image_"+"negativ.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
    
def custom_filter(update, context):
    q1=int(context.args[0])
    q2=int(context.args[1])
    q3=int(context.args[2])
    source=Image.open("user_image.jpg")
    width,height=source.size
    result=Image.new("RGBA",(width,height))
    
    for w in range(width):
        for h in range(height):
            r,g,b=source.getpixel((w, h))
            result.putpixel((w,h),(q1-r,q2-g,q3-b,255))
    result.save("user_image_"+"custom_filter.png")
    sending_img = open("user_image_"+"custom_filter.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
    
def random_filter(update, context):
    q1=random.randint(0,256)
    q2=random.randint(0,256)
    q3=random.randint(0,256)
    source=Image.open("user_image.jpg")
    width,height=source.size
    result=Image.new("RGBA",(width,height))
    for w in range(width):
        for h in range(height):
            r,g,b=source.getpixel((w, h))
            result.putpixel((w,h),(q1-r,q2-g,q3-b,255))
    result.save("user_image_"+"random_filter.png")
    sending_img = open("user_image_"+"random_filter.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
    
def lightanddark(update, context):
    a = int(context.args[0])
    img=Image.open("user_image.jpg")
    width,height=img.size
    for w in range(width):
        for h in range(height):
            r,g,b=img.getpixel((w, h))
            nr=int(r*a)
            ng=int(g*a)
            nb=int(b*a)
            nrgb=nr+ng+nb
            ligark=nrgb/3
            if nr>255:
                nr=255
            elif ng>255:
                ng=255
            elif nb>255:
                nb=255
            elif nr<0:
                nr=0
            elif ng<0:
                ng=0
            elif nb<0:
                nb=0
            img.putpixel((w,h),(nr,ng,nb,255))
    img.save("user_image_"+"lightanddark_filter.png")
    sending_img = open("user_image_"+"lightanddark_filter.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)

def sunset(update, context):
    q1=450
    q2=350
    q3=250
    img=Image.open("user_image.jpg")
    width,height=img.size
    for w in range(width):
        for h in range(height):
            r,g,b=img.getpixel((w, h))
            img.putpixel((w,h),(q1-r,q2-g,q3-b,255))
    img.save("user_image_"+"sunset_filter.png")
    sending_img = open("user_image_"+"sunset_filter.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)

    
def gold(update, context):
    q1=450
    q2=350
    q3=250
    img=Image.open("user_image.jpg")
    width,height=img.size
    result=Image.new("RGBA",(width,height))
    for w in range(width):
        for h in range(height):
            r,g,b=img.getpixel((w, h))
            result.putpixel((w,h),(255-r,255-g,255-b,255))
    for w in range(width):
        for h in range(height):
            r,g,b=result.getpixel((w, h))
            result.putpixel((w,h),(q1-r,q2-g,q3-b,255))
    result.save("user_image_"+"gold_filter.png")
    sending_img = open("user_image_"+"gold_filter.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img) 
    

def ghostxgrimm_child(update, context):
    q1=572
    q2=272
    q3=272
    img=Image.open("user_image.jpg")
    width,height=img.size
    for w in range(width):
        for h in range(height):
            r,g,b=img.getpixel((w, h))
            img.putpixel((w,h),(q1-r,q2-g,q3-b,255))
    img.save("user_image_"+"aliy_filter.png")
    sending_img = open("user_image_"+"aliy_filter.png", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
helper_handler = CommandHandler("help", helper)
dispatcher.add_handler(helper_handler)
image1_handler = MessageHandler(Filters.photo, image1)
image2_handler = CommandHandler("image", image2)
blur_handler = CommandHandler("blur", BLUR)
dispatcher.add_handler(blur_handler)
detail_handler = CommandHandler("detail", DETAIL)
dispatcher.add_handler(detail_handler)
contour_handler = CommandHandler("contour", CONTOUR)
dispatcher.add_handler(contour_handler)
emboss_handler = CommandHandler("emboss", EMBOSS)
dispatcher.add_handler(emboss_handler)
smooth_handler = CommandHandler("smooth", SMOOTH)
dispatcher.add_handler(smooth_handler)
edge_enhance_handler = CommandHandler("edge_enhance", EDGE_ENHANCE)
dispatcher.add_handler(edge_enhance_handler)
sharpen_handler = CommandHandler("sharpen", SHARPEN)
dispatcher.add_handler(sharpen_handler)
white_black_handler = CommandHandler("white_black", filter1)
dispatcher.add_handler(white_black_handler)
negativ_handler = CommandHandler("negativ", filter2)
dispatcher.add_handler(negativ_handler)
custom_filter_handler = CommandHandler("custom_filter", custom_filter)
dispatcher.add_handler(custom_filter_handler)
random_filter_handler = CommandHandler("random_filter", random_filter)
dispatcher.add_handler(random_filter_handler)
lightanddark_filter_handler = CommandHandler("brightness", lightanddark)
dispatcher.add_handler(lightanddark_filter_handler)
dispatcher.add_handler(image2_handler)
dispatcher.add_handler(image1_handler)
sunset_handler = CommandHandler("sunset", sunset)
dispatcher.add_handler(sunset_handler)
aliy_handler = CommandHandler("aliy", ghostxgrimm_child)
dispatcher.add_handler(aliy_handler) 
updater.start_polling()
updater.idle()
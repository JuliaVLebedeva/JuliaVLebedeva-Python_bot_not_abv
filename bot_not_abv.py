from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

bot = Bot(token='5650714727:AAGGSkuHGplfSAC7Bza1cPd9Kq_VS5LCeZI') # GB_JuliaLebedeva_bot  # начало всегда 
updater = Updater(token='5650714727:AAGGSkuHGplfSAC7Bza1cPd9Kq_VS5LCeZI')                 # updater - храниться время отправки, тест переписки
dispahather = updater.dispatcher                                                          # начало всегда

def start(update, context):
    text = update.message.text.split()
    list = []
    for elements in text:
        if 'абв' not in elements:
            list.append(elements)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))


start_handler =  MessageHandler(Filters.text, start)
dispahather.add_handler(start_handler)                                                  # начало всегда

updater.start_polling()                                                                 # начало всегда
updater.idle()                                                                          # начало всегда



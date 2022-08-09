from itertools import count
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
from methods import *


bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
add_handler = CommandHandler('add', add)
galina_handler = CommandHandler('galina', galina)
# count_handler = CommandHandler('cont', cont)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown) #/game


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(galina_handler)
# dispatcher.add_handler(count_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()
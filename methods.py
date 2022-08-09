from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN


def add(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Введите числа через пробел после названия команды")
        return
    try: 
        arg = list(map(int, arg))
    except ValueError:
        context.bot.send_message(update.effective_chat.id, "Incorrect data")
    res = sum(arg)
    arg = '+'.join(list(map(str, arg)))
    context.bot.send_message(update.effective_chat.id, f"{arg} = {res}")


# def cont(update, context):
#     number_1 = update.message.text
#     try:
#         eval(number_1)
#         context.bot.send_message(update.effective_chat.id, f'{number_1} = {eval(number_1)}')
#     except ValueError:
#         context.bot.send_message(update.effective_chat.id, "Incorrect data. Try 1+2*(3*4)/7**4")
    


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создала компания GB!")


def message(update, context):
    text = update.message.text
    try:
        eval(text)
        context.bot.send_message(update.effective_chat.id, f'{text} = {eval(text)}')
    except:
        if text.lower() == 'привет':
            context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
        else:
            context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')


def galina(update, context):
    context.bot.send_message(update.effective_chat.id, f'Пердина!')
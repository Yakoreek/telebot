from bot import bot
from pars_bot import *


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы получить информацию по предмету Minecraft, введи название')


@bot.message_handler(commands=['help'])
def start(message):
    responce = ('Я телеграм бот "MineHelper". У меня вы можете получить информацию и крафт по интересующему предмету.\n'
                'Чтобы получить информацию, необходимо ввести название предмета на анлгийском языке.\n'
                'Я знаю следующие комманды:\n'
                '/start - начать чат со мной.\n'
                '/help - узнать мой функционал.\n'
                )
    bot.send_message(message.chat.id, responce)


@bot.message_handler(content_types=['text'])
def get_item(message):
    item = message.text.strip().lower().replace(' ', '')
    info_text = item_info_text(item)
    if info_text == False:
        bot.send_message(message.chat.id, 'Данный предмет не найден. Возможно название указано неверно, попробуйте еще раз')
        bot.register_next_step_handler(message, get_item)
        return
    info_image = 'https://www.minecraftcrafting.info/' + item_info_image(item)
    for paragraph in info_text:
        bot.send_message(message.chat.id, paragraph)
    bot.send_photo(message.chat.id, info_image)


def start_bot():
    print("Бот запущен")
    bot.polling(none_stop=True)
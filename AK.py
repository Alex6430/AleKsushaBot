import telebot
from telebot import types
from telebot.types import Message


TOKEN = '835278572:AAGRDxgEJORXw31j5auVMu4C0SPFEi8J2RU'
bot = telebot.TeleBot(TOKEN)

def main():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        print(message.chat.id)
        if message.chat.id == 263993916:
            bot.reply_to(message, 'Здравствуй хозяин')
        else:
            bot.reply_to(message, 'Привет')

    @bot.message_handler(commands=['help'])
    def send_help(message):
        # bot.reply_to(message, 'Помощь')
        key = types.InlineKeyboardMarkup()
        button_weather = types.InlineKeyboardButton(text="Погода", callback_data="Weather")
        button_youtube = types.InlineKeyboardButton(text="Ютуб", callback_data="youtube")
        key.add(button_weather, button_youtube)
        bot.send_message(message.chat.id, "Помощь", reply_markup=key)

    @bot.message_handler(commands=['url'])
    def url(message):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

    @bot.message_handler(commands=['share'])
    def switch(message):
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='Share', switch_inline_query="Telegram")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Выбрать чат", reply_markup=markup)

    @bot.message_handler(func=lambda message: True)
    def upper(message: Message):
        message.text = message.text.lower()
        val = message.text.find("хочу посмотреть")
        if message.text == 'ютуб':
            key = types.InlineKeyboardMarkup()
            button_choose_youtube = types.InlineKeyboardButton(text="ютуб", callback_data="youtube")
            key.add(button_choose_youtube)
            bot.send_message(message.chat.id, "нажми кнопку", reply_markup=key)
            # bot.reply_to(message, 'https://www.youtube.com/')
        elif message.text == 'погода':
            key = types.InlineKeyboardMarkup()
            button_choose_weather = types.InlineKeyboardButton(text="погода", callback_data="Weather")
            key.add(button_choose_weather)
            bot.send_message(message.chat.id, "нажми кнопку", reply_markup=key)
            # bot.reply_to(message, 'https://yandex.ru/pogoda/moscow')
        elif message.text == 'кино':
            url = 'https://w25.zona.plus/movies?page='
            key = types.InlineKeyboardMarkup()
            button_choose_movi_yes = types.InlineKeyboardButton(text="да", callback_data="choose_movi_yes")
            button_choose_movi_not = types.InlineKeyboardButton(text="нет", callback_data="choose_movi_not")
            key.add(button_choose_movi_yes, button_choose_movi_not)
            bot.send_message(message.chat.id, "хотите выбрать жанр?", reply_markup=key)
        elif message.text == 'хочу посмотреть':
            bot.reply_to(message, 'https://yandex.ru/pogoda/moscow')
        else:
            bot.reply_to(message, "Я тупой и не понимаю команду")

    bot.polling()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
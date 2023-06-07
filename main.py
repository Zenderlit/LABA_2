import telebot
from telebot import types

# Токен вашего бота
token = '6177157741:AAEPyD9E2nvThJqJX1h-XlcFD7eaQpPe6yA'

# Создаем объект чат-бота
bot = telebot.TeleBot(token)

# Словарь с вопросами и ответами (FAQ)
faq = {
    "Как оплатить обучение?": "Информацию о вариантах оплаты обучения можно найти на сайте вуза.",
    "Как узнать расписание занятий?": "Расписание занятий можно узнать на сайте вуза в личном кабинете студента.",
    "Как найти свой факультет?": "Факультет можно найти на сайте вуза или в личном кабинете студента.",
    "Как получить стипендию?": "Информацию о правилах получения стипендии можно узнать на сайте вуза.",
    "Как подать заявление на общежитие?": "Информацию о заявлении на общежитие можно получить в отделе студенческого обслуживания вуза.",
}

# Создаем объект клавиатуры с кнопками
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for question in faq:
    button = types.KeyboardButton(text=question)
    keyboard.add(button)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я - чат-бот для новичков в вузе.", reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    if text in faq:
        bot.reply_to(message, faq[text])

# Запускаем бота
bot.polling()

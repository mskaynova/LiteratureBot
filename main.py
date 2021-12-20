import telebot
import constants
import random
from telebot import types


name = ''
count = 0
q1 = ['В детсве этого автора разыграли друзья, подсыпав в булочки, которые тот позже съел, опилки', 'В большинстве произведений этого автора присутствуют образы Кавказа', 'Этот автор жил с 1814 по 1841', 'Этот автор написал произведение "Герой нашего времени"']
q2 = ['У этого автора было 29 состоявшихся и не состоявшихся дуэлей', 'Годы жизни этого автора: 1799-1837','Этот автор написал произведение "Евгений Онегин"']
q3 = ['Этот писатель очень любил рукоделие. Он кроил платья для сестер, вязал на спицах, ткал пояса', 'Этот писатель жил с 1809 по 1852 год', 'Он написал произведения "Шинель" и "Мертвые души"']
q4 = ['Этот писатель был трижды женат, но не имел детей, что являлось его осознанным выбором', 'Годы жизни этого писателя: 1891-1940', 'Им было написано произведение "Мастер и Маргарита"']
q5 = ['Первые произведения этого автора печатались в журнале его же брата', 'Этот автор жил с 1821 по 1881 год', 'Этот автор написал произведение "Преступление и наказание"']
bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def hello(message):
    '''
    Функция, отправляющая приветственное сообщение пользователю
    '''
    bot.reply_to(message, "Привет! Рада, что ты решил(а) воспользоваться LiteratureBot!! \n\nЭтот бот предназначен для того, чтобы проверить свои знания в области литературы и узнать что-то новое для себя \n\nПомни, что при ответе на вопросы теста необходимо ввести фамилию автора с заглавной буквы. \n\nЧтобы начать, напиши /starttest \n\nУдачи!!!!")
    
def get_name(message):
    '''
    Функция позволяет узнать имя пользователя и предложить начать тест
    '''
    global name
    name = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='давай',callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='не(', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text='Очень приятно,'+name+'. Давай начинать!', reply_markup = keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    '''
    Функция дает возмжность пользователю показать свою готовность к началу теста
    '''
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'напиши /test')
        bot.register_next_step_handler(call.message, test)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'очень жаль( отправь любое сообщение, чтобы начать снова')
        
def test(message):
    '''
    Функция, дающая команду к началу теста
    '''
    if message.text == '/test':
        bot.send_message(message.from_user.id, random.choice(q1))
        bot.register_next_step_handler(message, answer1)
    else:
        bot.send_message(message.from_user.id, 'Попробуй еще раз, напиши /test')
        
def answer1(message):
    '''
    Функция дает реакцию на ответ пользователя на первый вопрос, прибавляет балл к общему результату в случае правильного ответа
    '''
    if message.text == 'Лермонтов':
        bot.send_message(message.from_user.id, 'Молодец, правильно')
        bot.send_message(message.from_user.id, random.choice(q2))
        bot.register_next_step_handler(message, answer2)
        global count
        count += 1
    else:
        bot.send_message(message.from_user.id, 'Неправильно(')
        bot.send_message(message.from_user.id, random.choice(q2))
        bot.register_next_step_handler(message, answer2)
        
def answer2(message):
    '''
    Функция дает реакцию на ответ пользователя на второй вопрос, прибавляет балл к общему результату в случае правильного ответа
    '''
    if message.text == 'Пушкин':
        bot.send_message(message.from_user.id, 'Молодец, правильно')
        bot.send_message(message.from_user.id, random.choice(q3))
        bot.register_next_step_handler(message, answer3)
        global count
        count += 1
    else:
        bot.send_message(message.from_user.id, 'Неправильно(')
        bot.send_message(message.from_user.id, random.choice(q3))
        bot.register_next_step_handler(message, answer3)
        
def answer3(message):
    '''
    Функция дает реакцию на ответ пользователя на третий вопрос, прибавляет балл к общему результату в случае правильного ответа
    '''
    if message.text == 'Гоголь':
        bot.send_message(message.from_user.id, 'Молодец, правильно')
        bot.send_message(message.from_user.id, random.choice(q4))
        bot.register_next_step_handler(message, answer4)
        global count
        count += 1
    else:
        bot.send_message(message.from_user.id, 'Неправильно(')
        bot.send_message(message.from_user.id, random.choice(q4))
        bot.register_next_step_handler(message, answer4)
        
def answer4(message):
    '''
    Функция дает реакцию на ответ пользователя на четвертый вопрос, прибавляет балл к общему результату в случае правильного ответа
    '''
    if message.text == 'Булгаков':
        bot.send_message(message.from_user.id, 'Молодец, правильно')
        bot.send_message(message.from_user.id, random.choice(q5))
        bot.register_next_step_handler(message, answer5)
        global count
        count += 1
    else:
        bot.send_message(message.from_user.id, 'Неправильно(')
        bot.send_message(message.from_user.id, random.choice(q5))
        bot.register_next_step_handler(message, answer5)
        
def answer5(message):
    '''
    Функция дает реакцию на ответ пользователя на пятый вопрос, прибавляет балл к общему результату в случае правильного ответа
    '''
    if message.text == 'Достоевский':
        bot.send_message(message.from_user.id, 'Молодец, правильно')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDhQZhv2pmBG6FYXgdAYx3hh8KikxE4AACBgkAAhlWig6zGNC4EmXBqCME')
        bot.register_next_step_handler(message, result)
        global count
        count += 1
    else:
        bot.send_message(message.from_user.id, 'Неправильно(')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDhQZhv2pmBG6FYXgdAYx3hh8KikxE4AACBgkAAhlWig6zGNC4EmXBqCME')
        bot.send_message(message.from_user.id, 'Наипиши понравился ли тебе тест, чтобы продолжить')
        bot.register_next_step_handler(message, result)
        
def result(message):
    '''
    Функция, объявляющая результаты теста
    '''
    if count == 5:
        bot.send_message(message.from_user.id, 'Поздравляю ты ответил(а) на все вопросы правильно!!')
    if count == 4:
        bot.send_message(message.from_user.id, 'Ты не смог(ла) ответить верно лишь на один из вопросов! Попробуй снова, уверена у тебя получиться улучшить свой результат')
    if count == 3:
        bot.send_message(message.from_user.id, 'Ты верно ответил(а) на 3 вопроса! Попробуй еще раз, чтобы улучшить свой результат')
    if count == 2:
        bot.send_message(message.from_user.id, 'Ты верно ответил(а) на 2 вопроса! Попробуй снова, чтобы улучшить свой результат')
    if count == 1:
        bot.send_message(message.from_user.id, 'Ты верно ответил(а) на 1 вопрос! Попробуй снова, чтобы улучшить свой результат')
    if count == 0:
        bot.send_message(message.from_user.id, 'Ты не смог(ла) ответить верно на какой-либо из вопросов( Попробуй снова! У тебя обязательно получится!!!!')
    bot.send_message(message.from_user.id, 'Напиши /test, чтобы начать тест заново')
    bot.register_next_step_handler(message, test)
    
@bot.message_handler(content_types=['text'])
def start(message):
  '''
  Функция предлагает пользователю представиться, обрабатывает текст, полученный от пользователя
  '''
    if message.text == '/starttest':
        bot.send_message(message.from_user.id, 'Как к тебе можно обращаться?')
        bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.from_user.id, 'Попробуй еще раз, напиши /starttest')
        
if __name__=='__main__':        
    bot.infinity_polling()

import unittest
import mock
import main
from unittest.mock import ANY

class telegrambot_test(unittest.TestCase):

    @mock.patch('main.bot')
    def test_hello(self, bot):
        main.hello(message)
        ret = "Привет! Рада, что ты решил(а) воспользоваться LiteratureBot!! \n\nЭтот бот предназначен для того, чтобы проверить свои знания в области литературы и узнать что-то новое для себя \n\nПомни, что при ответе на вопросы теста необходимо ввести фамилию автора с заглавной буквы. \n\nЧтобы начать, напиши /starttest \n\nУдачи!!!!"
        bot.reply_to.assert_called_with(ret, reply_markup=ANY)

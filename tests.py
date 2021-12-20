import unittest
import time
from telethon import TelegramClient

api_id = int('')
api_hash = ''
client = TelegramClient('name', api_id, api_hash)

client.start()
class TG_test(unittest.TestCase):
    def teststart(self):
        try:
            client.send_message('@LiteratureMiemBot', '/start')
            time.sleep(3)
            messages = client.get_messages('@LiteratureMiemBot')
            for message in client.get_messages('@LiteratureMiemBot', limit=1):
                mes = message.message
            self.assertEqual(len(messages), 1)
            text = "Привет! Рада, что ты решил(а) воспользоваться LiteratureBot!! \n\nЭтот бот предназначен для того, чтобы проверить свои знания в области литературы и узнать что-то новое для себя \n\nПомни, что при ответе на вопросы теста необходимо ввести фамилию автора с заглавной буквы. \n\nЧтобы начать, напиши /starttest \n\nУдачи!!!!"
            self.assertRegex(mes, text)
        except:
            self.assertFalse(True)

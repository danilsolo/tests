
import time
import telebot
import pprint
import datetime

bot = telebot.TeleBot("421498566:AAE3gXP16P3itP1VS0HcSVXrPStQmtxfvzk")


@bot.message_handler(func=lambda message: True, content_types=['sticker'])
def echo_sticker(message):
    print(message)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "привет")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "не помогу")



@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    print(message)

    if 'стикер' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAADBAADWgMAAis9kAAB60YbFEePUXsC')

    if 'Ты встретил' in message.text and message.forward_from:
        bot.reply_to(message, '''Напиши первым любое сообщение реплаем на это и забирай моба, если ты не успел, попробуй еще раз
@Fenicu @Puzya @danilsolo @belaya_devushka @nii_batca''')


    if 'пес' in message.text.lower():
        bot.reply_to(message, '@operatorasfuck тут это, по твою душу')

    if '👍 Приняли участие' in message.text:
        bot.reply_to(message, '@eegor7 ты чо пес')

    if 'хуесос, тест' in message.text:
        bot.reply_to(message, 'ну ок че')

    if 'режим тишины' in message.text or 'салфетка' in message.text:
        bot.reply_to(message, salfetka)
        bot.pin_chat_message(-1001064490030, message.message_id + 1)

    if 'тест' in message.text:
        bot.reply_to(message, 'ну ок че')

    if 'пин' in message.text.lower() and message.reply_to_message:
        bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)




    # if datetime.datetime.now().hour == 18 and

if __name__ == '__main__':
    bot.polling(none_stop=True)
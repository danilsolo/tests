#coding:utf-8
import telebot
import inventory
import sqlite3
import logging
import time
import datetime

BOTCHAT = 76201733
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

def niceprint(string):
    tabindex = 0
    out = ''
    for i in string:
        if i == ',':
            out += i
            out += '\n'
            out += '\t' * tabindex
            continue
        if i == '{':
            tabindex += 1
        if i == '}':
            tabindex -= 1
            out += '\n'
        out += i
    return out



bot = telebot.TeleBot("421498566:AAElg4npwqhJdWZfFh9Ze2SRblb6f6og30Q")
admins = ['Vozhik', 'Hedina69', 'belaya_devushka', 'danilsolo']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    userid = message.from_user.id
    username = message.from_user.username
    logging.debug('user: ' + str(username) + ' command: /start')

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()

    userlist = []
    for row in c.execute('select username from profiles'):
        userlist.append(row[0])

    if username in userlist:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы')
        conn.commit()
        conn.close()
    else:
        querry = "insert into profiles (id, username) values ('{}', '{}')".format(userid, username)
        logging.debug('new: ' + str(username))
        c.execute(querry)
        conn.commit()
        conn.close()

        bot.send_message(message.chat.id, 'Вы зарегистрированы')

@bot.message_handler(commands=['getall'])
def getallusers(message):
    logging.debug('user: ' + str(message.from_user.username) + ' command: /getall')

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()
    querry = "select * from profiles"
    logging.debug(querry)
    out = ''
    for i in c.execute(querry):
        out += '@' + str(i[1]) + ' | ' + str(i[2]) + ' | ' + str(i[3]) + '\n'
        out += '🏅' + str(i[4]) + ' ⚔' + str(i[5]) + ' 🛡' + str(i[6]) + ' 🔥' + str(i[7]) + ' 🤺' + str(i[8]) + '\n'
        out += '<code>🤛🏻</code>' + str(i[13]) + '\n'
        out += '<code>🤜🏻</code>' + str(i[14]) + '\n'
        out += '<code>🎩</code>' + str(i[15]) + '\n'
        out += '<code>👐🏻</code>' + str(i[16]) + '\n'
        out += '<code>👕</code>' + str(i[17]) + '\n'
        out += '<code>👢</code>' + str(i[18]) + '\n'
        out += '<code>🌂</code>' + str(i[19]) + '\n'
        if str(i[21]) == '':
            out += '🌿\n'
        else:
            out += str(i[21]) + '\n'

        out += '📦' + str(i[20]) + '\n'
        out += '🕐' + str(i[22]) + '\n\n'

    logging.debug(out)
    bot.send_message(message.chat.id, out, parse_mode='HTML')
    conn.commit()
    conn.close()

@bot.message_handler(commands=['getme'])
def getallusers(message):
    logging.debug('user: ' + str(message.from_user.username) + ' command: /getme')

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()
    querry = "select * from profiles where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))

        out = '@' + str(i[1]) + ' | ' + str(i[2]) + ' | ' + str(i[3]) + '\n'
        out += '🏅' + str(i[4]) + ' ⚔' + str(i[5]) + ' 🛡' + str(i[6]) + ' 🔥' + str(i[7]) + ' 🤺' + str(i[8]) + '\n'
        out += '<code>🤛🏻</code>' + str(i[13]) + '\n'
        out += '<code>🤜🏻</code>' + str(i[14]) + '\n'
        out += '<code>🎩</code>' + str(i[15]) + '\n'
        out += '<code>👐🏻</code>' + str(i[16]) + '\n'
        out += '<code>👕</code>' + str(i[17]) + '\n'
        out += '<code>👢</code>' + str(i[18]) + '\n'
        out += '<code>🌂</code>' + str(i[19]) + '\n'
        out += str(i[21]) + '\n'

        out += '📦' + str(i[20]) + '\n'
        out += '🕐' + str(i[22])[:-7] + '\n'

        bot.send_message(message.chat.id, out,  parse_mode='HTML')
        # bot.send_message(message.chat.id, str(i))
    conn.commit()
    conn.close()


@bot.message_handler(commands=['dellall'])
def getallusers(message):
    logging.debug('user: ' + str(message.from_user.username) + ' command: /dellall')

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()
    querry = "delete from profiles"
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        bot.send_message(BOTCHAT, str(i))
    conn.commit()
    conn.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def getprofile(message):
    # logging.debug(niceprint(str(message)))
    # logging.debug(time.time())
    # print(str(message.from_user.username) + ': ' + message.text)
    # print(message.text.split('\n'))
    userid = message.from_user.id
    username = message.from_user.username

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()

    userlist = []
    for row in c.execute('select username from profiles'):
        userlist.append(row[0])
    conn.commit()
    conn.close()

    if '/class' in message.text and '🇨🇾' in message.text and message.forward_from.id == 265204902 and username in userlist:# and message.forward_date > time.time() - 60:
        logging.debug('пользователь: ' + str(message.from_user.username) + ' прислал профиль')
        # niceprint(message.text)

        heroinfo = message.text.split('\n')
        herosword = ''
        herosdagger = ''
        herohead = ''
        heroarms = ''
        herobody = ''
        herolegs = ''
        herospecials = ''
        pet = ''

        for param in heroinfo:
            # logging.debug(param)
            if param[0:2] in ['🇨🇾', '🇬🇵', '🇪🇺', '🇮🇲', '🇻🇦', '🇲🇴', '🇰🇮']:
                heroflag = param[:2]
                heroname = param[2:param.find(',')]
                heroprof = param[param.find(',')+1:].split()[0]
                logging.debug('heroflag: ' + heroflag)
                logging.debug('heroname: ' + str(heroname))
                logging.debug('hero prof: ' + str(heroprof))

            if param[0:2] == '🏅У':
                herolevel = param.split()[1]
                logging.debug('hero level: ' + str(herolevel))

            if param[0:1] == '⚔':
                heroattack = param.split()[1]
                herodefense = param.split()[3]
                logging.debug('hero attack: ' + str(heroattack))
                logging.debug('hero defense: ' + str(herodefense))

            if param[0:1] == '🔥':
                heroexp = param.split()[1].split('/')[0]
                logging.debug('hero exp: ' + str(heroexp))

            if param[0:1] == '🔋':
                herostamina = param.split()[1].split('/')[0]
                logging.debug('hero stamina: ' + str(herostamina))

            heromana = 0
            if param[0:1] == '💧':
                heromana = param.split()[1].split('/')[0]
                logging.debug('mana: ' + str(heromana))

            if param[0:1] == '💰':
                herogold = param.split()[0][1:]
                herogems = param.split()[1][1:]
                logging.debug('hero gold: ' + str(herogold))
                logging.debug('hero gems: ' + str(herogems))

            if param[0:1] == '🤺':
                herowins = param.split()[1]
                logging.debug('hero wins: ' + str(herowins))

            if param in inventory.swords:
                herosword = str(param)
                logging.debug('sword: ' + str(herosword))

            if param in inventory.dagger:
                herosdagger = str(param)
                logging.debug('dagger: ' + str(herosdagger))

            if param in inventory.head:
                herohead = str(param)
                logging.debug('head: ' + str(herohead))

            if param in inventory.arms:
                heroarms = str(param)
                logging.debug('arms: ' + str(heroarms))

            if param in inventory.body:
                herobody = str(param)
                logging.debug('body: ' + str(herobody))

            if param in inventory.legs:
                herolegs = str(param)
                logging.debug('legs: ' + str(herolegs))

            if param in inventory.specials:
                herospecials = str(param)
                logging.debug('specials: ' + str(herospecials))

            if param[0:1] == '📦':
                herostock = param.split()[1]
                logging.debug('hero stock: ' + str(herostock))

            if param[0:2] in inventory.pets:
                pet = param
                logging.debug('pet: ' + str(pet))

        querry ='''update profiles
        set heroflag = '{1}',
            heroname = '{2}',
            prof = '{3}',
            attack = '{4}',
            defense = '{5}',
            exp = '{6}',
            stamina = '{7}',
            mana = '{8}',
            gold = '{9}',
            gems = '{10}',
            wins = '{11}',
            sword = '{12}',
            dagger = '{13}',
            head = '{14}',
            arms = '{15}',
            body = '{16}',
            legs = '{17}',
            specials = '{18}',
            stock = '{19}',
            pet = '{20}',
            proftime = '{22}'
        where id = {21}
        '''.format(heroflag, heroname, heroprof, herolevel, heroattack, herodefense, heroexp, herostamina, heromana,
                   herogold, herogems, herowins, herosword, herosdagger, herohead, heroarms, herobody, herolegs,
                   herospecials, herostock, pet, userid, datetime.datetime.now())


        conn = sqlite3.connect('wwbot.db')
        c = conn.cursor()
        logging.debug(querry)
        c.execute(querry)
        conn.commit()
        conn.close()

        bot.send_message(message.chat.id, 'Профиль обновлен')

    else:
        logging.debug('пользователь: ' + str(message.from_user.username) + ' прислал дерьмовый профиль')
        logging.debug(niceprint(str(message)))
        if username in userlist:
            bot.send_message(message.from_user.id, 'Ты отсылаешь мне какую-то дичь')
        else:
            bot.send_message(message.from_user.id, 'Ты отсылаешь мне какую-то дичь попробуй написать /start')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    # niceprint(str(message))
    # print(str(message.from_user.username) + ': ' + message.text)

    if 'пин' in message.text.lower() and message.reply_to_message and message.from_user.username in admins:
        bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

    if message.chat.id == BOTCHAT:
        bot.send_message(BOTCHAT, 'понял')

    if 'нет' in message.text:
        bot.reply_to()

if __name__ == '__main__':
    bot.polling(none_stop=True)

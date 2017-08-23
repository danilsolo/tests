import telebot
import inventory
import sqlite3
import logging

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
    print(out)



bot = telebot.TeleBot("421498566:AAElg4npwqhJdWZfFh9Ze2SRblb6f6og30Q")
admins = ['Vozhik', 'Hedina69', 'belaya_devushka', 'danilsolo']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    userid = message.from_user.id
    username = message.from_user.username

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()
    querry = "insert into profiles (id, username) values ('{}', '{}')".format(userid, username)
    # querry = "insert into profiles (id, username) values ('" + str(id) + "', '" + str(username) + "')"
    logging.debug('new: ' + str(username))
    c.execute(querry)
    conn.commit()
    conn.close()

    bot.send_message(message.chat.id, 'Вы зарегистрированы')

@bot.message_handler(commands=['getall'])
def getallusers(message):

    conn = sqlite3.connect('wwbot.db')
    c = conn.cursor()
    querry = "select * from profiles"
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        bot.send_message(message.chat.id, str(i))
    conn.commit()
    conn.close()


@bot.message_handler(commands=['dellall'])
def getallusers(message):

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
    # niceprint(str(message))
    # print(str(message.from_user.username) + ': ' + message.text)
    # print(message.text.split('\n'))
    userid = message.from_user.id

    if '/class' in message.text:
        # niceprint(message.text)

        heroinfo = message.text.split('\n')

        for param in heroinfo:
            # logging.debug(param)
            if param[0:2] in ['🇨🇾', '🇬🇵', '🇪🇺', '🇮🇲', '🇻🇦', '🇲🇴', '🇰🇮']:
                heroflag = param[:2]
                heroname = param[2:param.find(',')]
                heroprof = param[param.find(',')+1:].split()[0]
                logging.debug('heroflag: ' + heroflag)
                logging.debug('heroname: ' + str(heroname))
                logging.debug('hero prof: ' + str(heroprof))

            if param[0:1] == '🏅':
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
                logging.debug('sword: ' + str(param))

            if param in inventory.dagger:
                herosdagger = str(param)
                logging.debug('dagger: ' + str(param))

            if param in inventory.head:
                herohead = str(param)
                logging.debug('head: ' + str(param))

            if param in inventory.arms:
                heroarms = str(param)
                logging.debug('arms: ' + str(param))

            if param in inventory.body:
                herobody = str(param)
                logging.debug('body: ' + str(param))

            if param in inventory.legs:
                herolegs = str(param)
                logging.debug('legs: ' + str(param))

            if param in inventory.specials:
                herospecials = str(param)
                logging.debug('specials: ' + str(param))

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
            pet = '{20}'
        where id = {21}
        '''.format(heroflag, heroname, heroprof, herolevel, heroattack, herodefense, heroexp, herostamina, heromana,
                   herogold, herogems, herowins, herosword, herosdagger, herohead, heroarms, herobody, herolegs,
                   herospecials, herostock, pet, userid)


        conn = sqlite3.connect('wwbot.db')
        c = conn.cursor()
        logging.debug(querry)
        c.execute(querry)
        conn.commit()
        conn.close()

        bot.send_message(message.chat.id, 'Профиль обновлен')


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
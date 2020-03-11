import string
import random
import sqlite3

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()


class bot:
    def translation(self):
        return self.translation

def respond(str):
    print(str)
    query = ("SELECT choice_text FROM bot_choice, bot_question WHERE bot_question.question_text LIKE '%" + str + "'")
    c.execute(query)
    result = c.fetchall()
    print(len(result))
    resp =  random.choice(result) if len(result) > 0 else "Disculpa, no entiendo"
    return resp

print(respond('Que venden?'))
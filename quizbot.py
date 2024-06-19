import os
import telebot
from datetime import datetime
import time
from telebot import types
import yaml

#BOT_TOKEN = os.environ.get('DOCBOT_TOKEN')
BOT_TOKEN = 
bot = telebot.TeleBot(BOT_TOKEN)

prev_question_time = time.time()

GAMES_BY_ID = []
GAMES_BY_ADMIN = []
GAMES_BY_PLAYERS = []

from enum import Enum
class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4
    PAUSED = 5
    WAITING_ANSWERS = 6

class Answer:
    def __init__(self, player_id, number, text, time, points):
        self.player_id = player_id
        self.number = number
        self.text = text
        self.time = time
        self.points = points
        

class Question:
    def __init__(self):
        self.question = None
        self.right_answer = None
        self.answers_from_players = []

# class to store state of the quiz game
class Game:
    def __init__(self, game_id, template):
        self.game_id = game_id
        self.template = template 
        self.status = Status.PENDING
        self.players = []
        self.question_num = 0


# class to store answer of the player: number, text, time, points
class Answer:
    def __init__(self, number, text, time, points):
        self.number = number
        self.text = text
        self.time = time
        self.points = points

# class to store state of the player of quiz game       
class Player:

@bot.message_handler(commands=['next'])
def test(message):
  global prev_question_time
  bot.reply_to(message, "Когда родился Ли Якокка?")
  prev_question_time = time.time()  

  


@bot.message_handler(func=lambda msg: True)
def general_question(message):
    answer_time = time.time() - prev_question_time
    bot.reply_to(message, "Ответ правильный ({})".format(answer_time), parse_mode = 'HTML')

print(str(datetime.now()) + " Quiz Doc is here!")
bot.infinity_polling()

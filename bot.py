from telebot import *
from dotenv import load_dotenv
import os

load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))
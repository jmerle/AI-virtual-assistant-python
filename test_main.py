#!/usr/bin/python3

from tools.interaction.speak import speak
from tools.interaction.get_audio import get_audio
from tools.AI.ai import ai
from settings.logs import *
from data.data import bye
from tools.string_processing import string_process

def check_done(msg):
    for i in bye:
        if i in msg:
            return True
    return False

def main() :
    logger.info('Bot starts.')
    speak('Hello sir, how can i help you?')
    get = 'goto light oj'
    msg = ai(get)
    speak(msg)
    speak('Good Bye, Sir.')
    logger.info('Bot stopped.')
    

main() 
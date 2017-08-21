# -*- coding:utf-8 -*- 

__author__="GYZ"
__date__ ="$2017-8-11 18:27:28$" 


from scripts.settings import SOUND_FILE_PATH
from scripts.settings import SILENCE_SOUND_PATH
from scripts.audioFileOperations import audioFileOperations
from scripts.findAudio import findAudio
import copy
import os

logo = '''
__     ___    __  __   _              ______   _______
\ \   / / \  |  \/  | | |__  _   _   / ___\ \ / /__  /
 \ \ / / _ \ | |\/| | | '_ \| | | | | |  _ \ V /  / / 
  \ V / ___ \| |  | | | |_) | |_| | | |_| | | |  / /_ 
   \_/_/   \_\_|  |_| |_.__/ \__, |  \____| |_| /____|
                             |___/                    '''      


def not_empty(s):
    return s and s.strip()

inputFile = 'input.txt'

f = open(inputFile)
text = f.read()
words = text.split('\n')

words = list(filter(not_empty, words))

# print words

audioFileOperations.createAudioFromList( words, 'tests/output.mp3', interval = 1200)




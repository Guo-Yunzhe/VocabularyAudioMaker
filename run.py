# -*- coding:utf-8 -*- 

__author__="GYZ"
__date__ ="$2017-8-11 18:27:28$" 

from scripts.settings import LOGO
from scripts.settings import SOUND_FILE_PATH
from scripts.settings import SILENCE_SOUND_PATH
from scripts.audioFileOperations import audioFileOperations
from scripts.findAudio import findAudio
import copy
import os
import argparse

def not_empty(s):
    return s and s.strip()

def main():
     
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', 
                        help = 'source vocabulary file',
                        action = 'store_true',
                        default = 'input.txt')
    parser.add_argument('-o', '--output', 
                        help = "output file's path",
                        action = 'store_true',
                        default = 'output.mp3')
    args = parser.parse_args()
    inputFile = args.source
    outputFile = args.output
    f = open(inputFile)
    text = f.read()
    words = text.split('\n')

    words = list(filter(not_empty, words))

    # print words

    audioFileOperations.createAudioFromList( words, outputFile, interval = 1200)


if __name__ == "__main__":
    main()
    pass # end



# -*- coding:utf-8 -*-  

from scripts.settings import SOUND_FILE_PATH
from scripts.settings import SILENCE_SOUND_PATH
from scripts.audioFileOperations import audioFileOperations
from scripts.findAudio import findAudio
import copy
import os

testFile_1 = 'tests/zaandam.mp3'
testFile_2 = 'tests/z-score.mp3'

# add

addPath = 'tests/test-add.mp3'

audioFileOperations.jointWaveFile(testFile_1, testFile_2, addPath)

# add blank

newPath = 'tests/test-add-blank.mp3'

audioFileOperations.addSilenceBefore(testFile_2, newPath,  length = 2500)


# recursively find all possible combinations
wordList = ['a', 'lot', 'of']

def getAllCombinations(wordList):
    if len(wordList) == 0:
        return []
    if len(wordList) == 1:
        lastWord = wordList[0]
        result = []
        result.append([lastWord])
        result.append([lastWord.capitalize() ])
        return result
    else:
        lastWord = wordList[0]
        newList = []
        for i in range(1, len(wordList)):
            newList.append( wordList[i] )
            pass # end of for i in
        # print 'newlist:',
        # print newList
        formerResult = getAllCombinations(newList)
        # print 'former:', 
        # print formerResult
        result = []
        for i in formerResult:
            case1 = copy.deepcopy(i)
            case1.append( lastWord )
            case2 = copy.deepcopy(i)
            case2.append( lastWord.capitalize() )
            result.append(case1)
            result.append(case2)
            pass
        return result
    pass # end of the function

x = getAllCombinations( wordList)
for i in x:
    # print list(reversed(i))
    eachList = list(reversed(i))
    print '-'.join(eachList)

print '\n\n'

findAudio.audio_file_path   = SOUND_FILE_PATH
findAudio.silence_file_path = SILENCE_SOUND_PATH
pharseList = findAudio.getWordPaths('indo chinese')
for i in pharseList:
    print i,
    print os.path.exists(i)
    
for i in range(4):
    dstPath = 'tests/idc-' + str(i) + ".mp3"
    strPath = pharseList[i]
    audioFileOperations.addSilenceBefore(strPath, dstPath,  length = 2500)

print ('\n\n')
print findAudio.byWord('good')
print findAudio.byWord('goodfsdsfd')

testWordList = [
    'test',
    'word',
    'list'
]

# audioFileOperations.createAudioFromList( testWordList, 'tests/first.mp3', interval = 1200)

def not_empty(s):
    return s and s.strip()

inputFile = 'input.txt'

f = open(inputFile)
text = f.read()
words = text.split('\n')

words = list(filter(not_empty, words))

# print words

audioFileOperations.createAudioFromList( words, 'tests/output.mp3', interval = 1200)
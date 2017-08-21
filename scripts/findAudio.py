# -*- coding:utf-8 -*-  
import os
import copy

class findAudio:
    # class variable
    audio_file_path = '~/DEFAULT-PATH/'
    silence_file_path = '~/DEFAULT-SILENCE-FILE.mp3'

    @staticmethod
    def byWord(wordStr, format = 'mp3'):
        possiblePaths = findAudio.getWordPaths(wordStr, format)
        for i in possiblePaths:
            if os.path.exists(i):
                return i, 1
        return findAudio.silence_file_path, 0
        pass

        pass # end of by word

    @staticmethod
    def getWordPaths(wordStr, format = 'mp3'):
        result = ''
        # test code
        path = findAudio.audio_file_path
        # print x
        # test code ..
        assert len(wordStr) >= 1, 'Invalid Word!'
        word = wordStr.lower()
        word = word.strip()
        word = word.replace('\r', '' )
        word = word.replace(' ' , '-')
        firstCharacter = word[0]
        assert firstCharacter in 'qwertyuioplkjhgfdsazxcvbnm' , 'Invalid Word!'
        # then fill the path
        path = path + firstCharacter + '/'
        possiblePaths = []
        if not '-' in word:
            # only 2 choice
            possiblePaths.append( path + word + '.' + format )
            possiblePaths.append( path + firstCharacter.upper() + word[1:] + '.' + format )
            pass
        else: # pharse
            parts = word.split('-')
            stringList = findAudio.getPharsePossibleStr(parts)
            for i in stringList:
                possiblePaths.append( path + i + '.' + format )
                pass # end of for i 
            pass # end of else
        # print possiblePaths
        return possiblePaths
        pass

    @staticmethod
    def getPharsePossibleStr(parts):
        result = []
        # get all combinations
        pharseList = findAudio.getAllCombinations(parts)
        # generate the strings
        for i in pharseList:
            eachList = list(reversed(i))
            eachStr = '-'.join(eachList)
            result.append(eachStr)
        # done
        return result
        pass

    
    @staticmethod
    def getAllCombinations(wordList):
        '''
            To get all combinations of serval simple word
            with or without capitalized.
            In Linux or Windows, this is vital, while in Macintosh,
            the system is not case sensitive.
        '''
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
            formerResult = findAudio.getAllCombinations(newList) 
            # recursive here
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

    pass
# -*- coding:utf-8 -*-  
import os
from pydub import AudioSegment # use pydub and ffmpeg

from findAudio import findAudio
from settings import SOUND_FILE_PATH
from settings import SILENCE_SOUND_PATH
from settings import ALBUM 
from settings import ARTIST 

class audioFileOperations:
    
    @staticmethod
    def createAudioFromList(wordList, outputPath,interval = 1200, format = 'mp3'):
        noRecordCount = 0
        findAudio.audio_file_path   = SOUND_FILE_PATH
        findAudio.silence_file_path = SILENCE_SOUND_PATH
        # print findAudio.byWord('book')
        result = AudioSegment.empty()
        silence = AudioSegment.silent(duration = interval)
        for eachWord in wordList:
            eachPath, statusCode = findAudio.byWord(eachWord)
            if statusCode == 0:
                noRecordCount += 1
                pass # end of the if
            eachWordAudio = AudioSegment.from_file(eachPath, format = format)
            result += eachWordAudio
            result += silence
            pass # end of `for each word`
        # info
        album = ALBUM
        artist = ARTIST
        # export
        file_handle = result.export(outputPath , format= format, 
                    tags = {"album": album , "artist": artist } )
        # print 'There are',
        # print noRecordCount,
        # print 'words have no audio.'
        return noRecordCount
        pass

    @staticmethod
    def mp3ToWave(srcPath, dstPath, format = 'mp3'):
        # Firstly, check the existence of the srcPath
        fileExist = os.path.exists(srcPath)
        haveMP3 = (format in srcPath) or ( format.upper() in srcPath)
        valid = haveMP3 and fileExist
        assert valid == True, "srcPath NOT EXIST or is NOT a MP3 FORMAT !"
        # Then do the convert
        try:
            sound = AudioSegment.from_mp3(srcPath)
            sound.export(dstPath, format="wav")
            # end of the convert
            result = True
        except:
            result = False # failure on convert
        finally:
            return result
        pass # end of `mp3ToWave`

    @staticmethod
    def jointWaveFile(firstPath, secondPath, dstPath, format = 'mp3'):
        # Firstly, check the existence of the srcPath
        fileExist  = os.path.exists(firstPath)
        fileExist2 = os.path.exists(secondPath)
        valid = fileExist2 and fileExist
        assert valid == True, "FILE NOT EXIST !"
        s1  = AudioSegment.from_file(firstPath,  format = format)
        s2  = AudioSegment.from_file(secondPath, format = format)
        new = AudioSegment.empty()
        new = s1 + s2
        # info
        album = ALBUM
        artist = ARTIST
        file_handle = new.export(dstPath, format= format, 
                        tags = {"album": album , "artist": artist } )
        pass # end of `jointWaveFile`
    
    @staticmethod
    def addSilenceBefore(srcPath, dstPath, format = 'mp3', length = 1500 ):
        # first we create silence sound, time is represented in `ms`
        silence = AudioSegment.silent(duration = length)
        sound   = AudioSegment.from_file(srcPath, format = format) 
        new = silence + sound
        # info
        album = ALBUM
        artist = ARTIST
        # export
        file_handle = new.export(dstPath, format=format, 
                        tags = {"album": album , "artist": artist } )
        pass # end of `addSilenceBefore`
    
    pass

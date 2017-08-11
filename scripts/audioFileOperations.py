# -*- coding:utf-8 -*-  
import os
from pydub import AudioSegment # use pydub and ffmpeg
import wave

class audioFileOperations:

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
    def jointWaveFile(firstPath, secondPath, dstPath, format = 'mp3', album = 'DEFAULT', artist = "DEFAULT"):
        # Firstly, check the existence of the srcPath
        fileExist  = os.path.exists(firstPath)
        fileExist2 = os.path.exists(secondPath)
        valid = fileExist2 and fileExist
        assert valid == True, "FILE NOT EXIST !"
        '''
        # open the file
        w1 = wave.open(firstPath)
        w2 = wave.open(secondPath)
        # Check the wave file's parameters: nchannels, sampwidth, framerate
        # acquiescently, `nchannels, sampwidth, framerate` of the two file 
        # should NOT different
        params_1 = w1.getparams()[:3]
        params_2 = w1.getparams()[:3]
        assert params_1 == params_2
        # then add them
        '''
        s1  = AudioSegment.from_file(firstPath,  format = format)
        s2  = AudioSegment.from_file(secondPath, format = format)
        new = AudioSegment.empty()
        new = s1 + s2
        file_handle = new.export(dstPath, format='mp3', 
                        tags = {"album": album , "artist": artist } )
        pass # end of `jointWaveFile`
    
    @staticmethod
    def addSilenceBefore(srcPath, dstPath, format = 'mp3', length = 1500 ,album = 'DEFAULT', artist = "DEFAULT"):
        # first we create silence sound, time is represented in `ms`
        silence = AudioSegment.silent(duration = length)
        sound   = AudioSegment.from_file(srcPath, format = format) 
        new = silence + sound
        # export
        file_handle = new.export(dstPath, format='mp3', 
                        tags = {"album": album , "artist": artist } )
        pass # end of `addSilenceBefore`
    
    pass

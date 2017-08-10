# -*- coding:utf-8 -*-  
import os
from pydub import AudioSegment # use pydub and ffmpeg

class audioFileOperations:

    @staticmethod
    def mp3ToWave(srcPath, dstPath):
        # Firstly, check the existence of the srcPath
        fileExist = os.path.exists(srcPath)
        haveMP3 = ('mp3' in srcPath) or ('MP3' in srcPath)
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
    def jointWaveFile(firstPath, secondPath, dstPath):
        # Firstly, check the existence of the srcPath
        fileExist  = os.path.exists(firstPath)
        fileExist2 = os.path.exists(secondPath)
        valid = fileExist2 and fileExist
        assert valid == True, "FILE NOT EXIST !"
        
        pass # end of `jointWaveFile`
    
    pass

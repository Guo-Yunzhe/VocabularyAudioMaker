# -*- coding:utf-8 -*-  

from scripts.audioFileOperations import audioFileOperations

testFile_1 = 'tests/zaandam.mp3'
testFile_2 = 'tests/z-score.mp3'

# add

addPath = 'tests/add.mp3'

audioFileOperations.jointWaveFile(testFile_1, testFile_2, addPath, artist = "GYZ")

# add blank

newPath = 'tests/add-blank.mp3'

audioFileOperations.addSilenceBefore(testFile_2, newPath,  length = 2500)
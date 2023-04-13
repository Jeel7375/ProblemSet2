from fileinput import filename
import os.path

def fileLength(fileName):
    rootPath = 'C:/Users/briju/Desktop/DP/ProblemSet2/'
    file_path = os.path.join(rootPath, fileName)
    isFile = os.path.exists(file_path)
    if isFile:
        size = os.path.getsize(file_path)
        print(f'The {file_path} size is', size, 'bytes')
    else:
        print(f'{file_path} not found.')

fileLength('PS_2_1.py')
# detali : Geneater the Folder title on date 
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
#           https://twitter.com/dong_ub 
# @history, @Date  
#   - Foleder

import os
import datetime

PATH= 'c:/Users/test/Documents/'
FOLDER= 'Sound recordings'

def getFileNames():
    DIR= PATH+FOLDER
    try:
        return os.listdir(DIR)
    except IOError as e:
        print(e+"file names")

def saveFileInfoInTXT(node_file_name: str, path: str):
    try:
        with open(f'{node_file_name}', 'w') as f:
            device_info: int= os.stat(path).st_dev
            uid: int= os.stat(path).st_uid
            byte_size: int= os.stat(path).st_size
            modified_time_recently: float= os.stat(path).st_mtime
            INFOMATION= f'device_info: {device_info}, uid: {uid}, byte_size: {byte_size}, modified_time_recently: {modified_time_recently}'
            # created_time
            f.write(INFOMATION)
    except IOError as e:
        print(e+"stat_result, so set default")

# Infomation node file
file_names= getFileNames()

for file_name in file_names:
    CURRENT_INFOMATION_SUMMTION= f'Info){DATE}.txt'
    saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)
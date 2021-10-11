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
DIR= PATH+FOLDER
DATE= datetime.date.today().strftime("%d%m%Y")

def getFileNames():
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
            creation_on_windows: int= os.stat(path).st_ctime_ns
            modified_time_recently: float= os.stat(path).st_mtime
            INFOMATION= f'device_info: {device_info}, uid: {uid}, byte_size: {byte_size}, creation_on_windows: {creation_on_windows}ms, modified_time_recently: {modified_time_recently}ms'
            f.write(f'{INFOMATION}\n entiry info\n{os.stat(path)}')
    except IOError as e:
        print(e+"stat_result, so set deifault")


# Main
file_names= getFileNames()
for file_name in file_names:
    CURRENT_INFOMATION_SUMMTION= f'Info){DATE}.txt'
    saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, DIR)
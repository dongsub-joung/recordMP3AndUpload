# Even when i made about "https://github.com/dongsub-joung/Sociology_bookList",
# always always i'm alone, had have not a group in or main.
# Korean is always be korean, so "korea" means the same "the lowest trust society and community commpletly".

import os
import datetime

PATH= 'c:/Users/test/Documents/Sound recordings'
DEFAULT= "Recording"

# Simple functions
def getIndex(index: int, array: list):
    for _ in array:
        index+= 1
    return index

# Functions
# Getter
def getFileNames():
    try:
        return os.listdir(PATH)
    except IOError as e:
        print(e+"file names")
        
def getFileName():
    try:
        return os.getFilseNames
    except IOError as e:
        print(e+"file name")

def getCreatedTime(file_name: str):
    try:
        return str(os.path.getmtime(file_name))
    except IOError as e:
        print(e+"created time")

def getModifiedTime(file_name: str):
    try:
        return str(os.getctime(file_name))
    except IOError as e:
        print(e+"modified time")

# Methos
def saveFileInfoInTXT(node_file_name: str, path: str):
    DEFAULT_MGS= 'DefaultSentence'
    try:
        with open(f'{node_file_name}', 'w') as f:
            stat_result= str(os.stat(path))
            f.write(stat_result)
    except IOError as e:
        print(e+"stat_result, so set default")
    finally:
        with open(f'{node_file_name}', 'w') as f:
            f.write(DEFAULT_MGS)

def fileNameing(name: str, date: str, created: str, modified: str):
    TIME= f'{date}){created}_{modified}'
    os.rename('Sound recordings', TIME)
  

# Main
DATE= datetime.date.today().strftime("%d%m%Y")
CURRENT_INFOMATION_SUMMTION= f'SUM){DATE}.txt'

m_array_index= 0
file_name= str(" ")
file_names= data_createds= date_modifieds= list()

file_names= getFileNames()
saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)

try:
    for file_name in file_names:
        file_name= str(PATH + '/' + file_name)
        data_createds.insert(getCreatedTime(file_name))
        date_modifieds.insert(getModifiedTime(file_name))
except IOError as e:
    print(e+"time list")

# 2. Folder: Current Date
#    File  : "Created Time" + "-" + "Modified Time"
m_array_index= getIndex(m_array_index, file_names)
for index in range(0, m_array_index):
    fileNameing(file_names[index], data_createds[index], date_modifieds[index])
# End
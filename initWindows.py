# Even when i made about "https://github.com/dongsub-joung/Sociology_bookList",
# always always i'm alone, had have not a group in or main.
# Korean is always be korean, so "korea" means the same "the lowest trust society and community commpletly".

# import datetime
import os
from datetime import date

# Define value
DEFAULT= "Recording"
FORM= ".M4a"

# Simple functions
def getIndex(index: int, array: list):
    for _ in array:
        index+= 1
    return index

# Functions
# Getter
def getFileNames():
    try:
        return os.listdir('my_dir/')
    except IOError as e:
        print(e+"file names")
        
def getFileName():
    try:
        return os.getFilseNames
    except IOError as e:
        print(e+"file name")

def getCreatedTime(file_name: str):
    try:
        return os.path.getmtime(file_name)
    except IOError as e:
        print(e+"created time")

def getModifiedTime(file_name: str):
    try:
        return os.getctime(file_name)
    except IOError as e:
        print(e+"modified time")

# Methos
def saveFileInfoInTXT(node_file_name: str, path: str):
    DEFAULT_MGS= 'DefaultSentence'
    try:
        with open(f'{node_file_name}', 'W') as f:
            stat_result= str(os.stat(path))
            f.write(stat_result)
    except IOError as e:
        print(e+"stat_result, so set default")
    finally:
        with open(f'{node_file_name}', 'W') as f:
            f.write(DEFAULT_MGS)

def fileNameing(name: str, date: str, created: str, modified: str):
    TIME= f'{date}){created}_{modified}'
    # original->new file title (name, str(TIME))

def moveTempsInFolder():
    # system command "move ."

# Main
PATH= # get relevent Directory
DATE= date.today.strftime("%d%m%Y")
CURRENT_INFOMATION_SUMMTION= f'SUM{DATE}.txt'

file_names= data_createds= date_modifieds= list()
file_name= data_created= date_modified= str(" ")

file_names= getFileNames()
saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)

try:
    for file_name in file_names:
        data_createds.insert(getCreatedTime(file_name))
        date_modifieds.insert(getModifiedTime(file_name))
except IOError as e:
    print(e+"time list")

# 2. Folder: Current Date
#    File  : "Created Time" + "-" + "Modified Time"
m_array_index= 0
m_array_index= getIndex(m_array_index, file_names)
for index in range(0, m_array_index+1):
    fileNameing(file_names[index], data_createds[index], date_modifieds[index])
file_name= fileNameing(names)

makeFolders(data_createds[index], date_modifieds[index])
# moveTempsInFolder()

# End
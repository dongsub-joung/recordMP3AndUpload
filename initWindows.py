# detali : Automate workflow on Sound Files. 
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
#           https://twitter.com/dong_ub
# @history, @Date  
#   - renaming files, dir in 2021-10-08 / 14:57
#   - Uploading @todo set the crul setion key in python
#   - 10-11 Do micro component as ".py", it mean each components will have the independency of moduls. 
#       *It's anwser why do not import class path in this project, but it's not restrict REST.API argument.
# @Comment
# Even when i made about "https://github.com/dongsub-joung/Sociology_bookList",
# always always i'm alone, had have not a group in or main.
# Korean is always be korean, so "korea" means the same "the lowest trust society and community commpletly".

import os
import datetime
import time

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
def getFileSizes(file_name: str, size_sum: int):
   try:
       size_sum+= os.stat(file_name).st_size
    except IOError as e:
        print(e+"size")

# Methos
def saveFileInfoInTXT(node_file_name: str, path: str):
    try:
        with open(f'{node_file_name}', 'w') as f:
            stat_result= str(os.stat(path))
            f.write(stat_result)
    except IOError as e:
        print(e+"stat_result, so set default")

def fileNameing(name: str, date: str, created: str, modified: str):
    TIME= f'{date}){created}_{modified}'
    os.rename('Sound recordings', TIME)

def getFuid(file_sizes: int):
    # os.system.__code__("curl 'https://up.ufile.io/v1/upload/finalise' \")
    DIR_TOKEN= '/TOKEN/fuid.txt'
    
    try:
        token= os.read(DIR_TOKEN)
        return str(token)
    except Exception as e:
        print(e+"fuid")
        return str(e)
 
def uploadingDir(file_name: str, file_type: str, total_chunk: str):
    # @todo Handle for ', \ char
    CURL_SITE= "https://up.ufile.io/v1/upload/finalise"
    FUID_FROM_SESSION_REQUEST= f'-d 'fuid={fuid}' \'

    os.getcwd(str("curl " + "'" + CURL_SITE + "'" + " \"))
    os.getcwd(str())
    return str(respon_oject)

def getUploadingSize(file_names: str):
    return 

# Main
DATE= datetime.date.today().strftime("%d%m%Y")
CURRENT_INFOMATION_SUMMTION= f'SUM){DATE}.txt'

m_array_index= m_file_sizes= 0
file_name= str(" ")
file_names= data_createds= date_modifieds= list()

file_names= getFileNames()
saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)

try:
    for file_name in file_names:
        file_name= str(PATH + '/' + file_name)
        m_file_sizes+= getFileSizes(file_name, m_file_sizes)
except IOError as e:
    print(e+"m_file_sizes")
try:
    for file_name in file_names:
        file_name= str(PATH + '/' + file_name)
        data_createds.insert(getCreatedTime(file_name))
except IOError as e:
    print(e+"data_createds")
try:
    for file_name in file_names:
        file_name= str(PATH + '/' + file_name)
        date_modifieds.insert(getModifiedTime(file_name))
except IOError as e:
    print(e+"tdate_modifieds")

# 2. Folder: Current Date
#    File  : "Created Time" + "-" + "Modified Time"
m_array_index= getIndex(m_array_index, file_names)
for index in range(0, m_array_index):
    fileNameing(file_names[index], data_createds[index], date_modifieds[index])

# 3. Uploading
fuid: str= getFuid(m_file_sizes)
uploadingDir(fuid, file_name, file_type, totoal_chunks)

# 4. wait
time.sleep(300)
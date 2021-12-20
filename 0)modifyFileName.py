# @detali : Helper modifing per Sound File on raw real time demons.  
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
# @Date @history   
#   - 10-11 12:39   builing pseudo code
#   -  ""   13:13   Fix core

import os

def getCreatedTime(file_name: str):
    try:
        return str(os.path.getmtime(file_name))
    except IOError as e:
        print(e+"created time")

def getLength(file_name: str):
    # @todo 
    try:
        return str(os.getctime(file_name))
    except IOError as e:
        print(e+"modified time")

def setFileTitle(create: str, LENGTH: str):
    FIRST= create.replace('mm/dd/yy', "")
    l_h= LENGTH[0,2]
    l_m= LENGTH[2,4]
    c_h= create[0,2]
    c_m= create[2,4]
    SECONDE_M= int(c_m) + int(l_m) % 60
    SECONDE_PLUSE= int(int(c_m) + int(l_m) / 60)
    SECONDE_H= int(c_h) + int(l_h) + SECONDE_PLUSE
    
    return str(FIRST+"__"+SECONDE_H+"-"+SECONDE_M)

# Main
PATH= 'c:/Users/test/Documents/Sound recordings'
FILENAME= "Recording"
FILENAME_AUTO= "Recording (autosaved)"

def defaultName(file_name: str):
    CREATED= getCreatedTime(file_name)
    LENGTH= getLength(file_name)
    TITLE= setFileTitle(CREATED, LENGTH)
    os.rename(file_name, TITLE)

try:
    defaultName(PATH+FILENAME)
except:
    defaultName(PATH+FILENAME_AUTO)
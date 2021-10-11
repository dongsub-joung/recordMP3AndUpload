# detali : Helper modifing per Sound File on raw real time demons.  
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
#           https://twitter.com/dong_ub
# @Date @history   
#   - 10-11 12:39   builing pseudo code

import os

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

def setFileTitle(create: str, modify: str):
    create.replace('mm/dd/yy', "")
    modify.replace('mm/dd/yy', "")
    FIRST= f'{create}__{modify}'

    c_h= create[0,2]
    m_h= modify[0,2]
    c_m= create[2,4]
    m_m= modify[2,4]
    SECONDE_H= int(m_h) - int(c_h)
    SECONDE_M= int(m_m) - int(c_m)
    
    return str(FIRST+SECONDE_H+"-"+SECONDE_M)

# Main
PATH= 'c:/Users/test/Documents/Sound recordings'
FILENAME= "Recording"
FILENAME_AUTO= "Recording (autosaved)"

def defaultName(file_name: str):
    CREATED= getCreatedTime(file_name)
    MODIFID= getModifiedTime(file_name)
    TITLE= setFileTitle(CREATED, MODIFID)
    os.rename(file_name, TITLE)

try:
    defaultName(PATH+FILENAME)
except Exception as e:
    defaultName(PATH+FILENAME_AUTO)
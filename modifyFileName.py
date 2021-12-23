# @detali : Helper modifing per Sound File on raw real time demons.  
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
# @Date @history   
#   - 10-11 12:39   builing pseudo code
#   -  ""   13:13   Fix core

import os
import filePathing
import datetime

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
    l_h= LENGTH[0:2]
    l_m= LENGTH[2:4]
    c_h= create[0:2]
    c_m= create[2:4]
    SECONDE_M= int(c_m) + int(l_m) % 60
    SECONDE_PLUSE= int(int(c_m) + int(l_m) / 60)
    SECONDE_H= int(c_h) + int(l_h) + SECONDE_PLUSE
    
    return str(FIRST+"__"+SECONDE_H+"-"+SECONDE_M)

def defaultName(file_name: str):
    CREATED= getCreatedTime(file_name)
    LENGTH= getLength(file_name)
    TITLE= setFileTitle(CREATED, LENGTH)
    
    # Value
    print(TITLE) 
    
    try:
        os.rename(file_name, TITLE)
    except:
        print("Err!")

def makeForders(subdir: str):

    DATE= datetime.date.today().strftime("%d%m%Y")
    DATE= DATE + ""
    d= DATE[0:2]
    m= DATE[2:4]
    y= DATE[4:0]

    try:
        if subdir in m:
            os.mkdir(f'{d}')
        elif subdir in y:
            os.makedirs(f'{m}/{d}')
        else:
            os.makedirs(f'{y}/{m}/{d}')
    except FileExistsError as exist_e:
        print(exist_e+"")
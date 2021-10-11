# detali : Helper Opening Automatly Sound File when 10% under on bettery. 
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
#           https://twitter.com/dong_ub
# @Date @history   
#   - 10-11 12:15   builing pseudo code

import os

PATH= str
SOUND_FILE= str

def getBetteryState():
    state: int
    # state= yandex.api.getBetteryUsage()
    return int(state)

def getSoundState():
    state: int
    state= os.Sound().getVolum()
    if(int(state) < 99):
        os.Sound().setVolum()

remain_power= getBetteryState()
if(remain_power<15):
    getSoundState()
    os.open(PATH+SOUND_FILE)


# Windows  
Win_PATH= 'c:/Users/test/Documents/'
Win_FOLDER= 'Sound recordings'
Win_DIR= f'{Win_PATH}{Win_FOLDER}'

# Kubuntu
Ku_PATH= '/home/dongsub/Music/'
Ku_FOLER= 'Recordings'
Ku_DIR= f'{Ku_PATH}{Ku_FOLER}'

# File Format
WIN_FILENAME= "Recording (autosaved)"
ANDROID_FILENAME= 'Voice'
# Ku_FILENAME= 'New recording '

def getWinPath():
    return Win_DIR

def getKubunPath():
    return Ku_DIR
import os

PATH= 'c:/Users/test/Documents/Sound recordings'

def getFileNames():
    try:
        return os.listdir(PATH)
    except IOError as e:
        print(e+"file names")

def saveFileInfoInTXT(node_file_name: str, path: str):
    try:
        with open(f'{node_file_name}', 'w') as f:
            stat_result= str(os.stat(path))
            f.write(stat_result)
    except IOError as e:
        print(e+"stat_result, so set default")

# Infomation node file
file_names= getFileNames()
for file_name in file_names:
    CURRENT_INFOMATION_SUMMTION= f'Info){file_name}.txt'
    saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)
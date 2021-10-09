import os

PATH= 'c:/Users/test/Documents/Sound_recordings'

def getFileNames():
    try:
        return os.listdir(PATH)
    except IOError as e:
        print(e+"file names")

def saveFileInfoInTXT(node_file_name: str, path: str):
    try:
        with open(f'{node_file_name}', 'w') as f:
            device_info: int= os.stat(path).st_dev
            uid: int= os.stat(path).st_uid
            byte_size: int= os.stat(path).st_size
            modified_time_recently: float= os.stat(path).st_mtime
            INFOMATION= f'device_info: {device_info}, uid: {uid}, byte_size: {byte_size}, modified_time_recently: {modified_time_recently}'
            # created_time
            f.write(INFOMATION)
    except IOError as e:
        print(e+"stat_result, so set default")

# Infomation node file
file_names= getFileNames()
for file_name in file_names:
    CURRENT_INFOMATION_SUMMTION= f'Info){file_name}.txt'
    saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)
import os
frome datetime import date

# Define value
PATH= "C:\Users\test\Documents\Sound recordings"
DEFAULT= "Recording"
FORM= "M4a"
RECORING_FILES= "Recording (autosaved)"
DATE= today.strftime("%d%m%Y")

file_name= " "
data_created= " "
date_modified= " "

# Main
file_name= os.getFilseNames
data_created= os.path.getmtime(file_name)
date_modified= os.getctime(file_name)

makeFolders(data_created, date_modified)
file_name= fileNameing(names)


# Functions
def saveFileInfoInTXT(file_names, data_node):
    with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)
    with open(f'{data_node}', 'W') as f:
        file_nodes_info= 'DefaultSentence'
        file_nodes_info= file_node= os.stat(file_names) + ''
        f.write(file_nodes_info)

def moveDateInPath(file_count):
    PRESENT= RECORING_FILES+FORM

    if PRESENT == file_name:
        pass

def getFileName():
    return os.getFilseNames
    
def fileNameing(names,created, modified):
    TIME= created+"_"+modified
    for file_name in names:
        if(file_name == DEFAULT):
            pass
        elif(file_name == FIRS):
            return DATE+"_1"
        else:
            numbers= file_name[-2]
            return DATE+numbers
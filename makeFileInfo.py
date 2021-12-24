import os;
import Comm_filePathing

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
        
# main functions
def addnamedata(file_names):
    try:
        for file_name in file_names:
            file_name= str(PATH + '/' + file_name)
            m_file_sizes+= self.getFileSizes(file_name, m_file_sizes)
    except IOError as e:
        print(e+"m_file_sizes")

def addCreateData(file_names):
    try:
        for file_name in file_names:
            file_name= str(PATH + '/' + file_name)
            data_createds.insert(self.getCreatedTime(file_name))
    except IOError as e:
        print(e+"data_createds")

def addModifiedData(file_names):
    try:
        for file_name in file_names:
            file_name= str(PATH + '/' + file_name)
            date_modifieds.insert(self.getModifiedTime(file_name))
    except IOError as e:
        print(e+"tdate_modifieds")



PATH= Comm_filePathing.getWinPath()

# main(Test)
addnamedata(file_names)
addCreateData(file_names)
addModifiedData(file_names)
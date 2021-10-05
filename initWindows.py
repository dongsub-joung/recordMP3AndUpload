improt os
frome datetime import date

const PATH= "C:\Users\test\Documents\Sound recordings"
const DEFAULT= "Recording"
const FIRST= "Recording (autosaved)"
DATE= today.strftime("%d%m%Y")

file_name= " "
data_created= " "
date_modified= " "

# names= os.getFilseNames
# data_created= os.get
# date_modified= os.get

makeFolders(data_created, date_modified)
file_name= fileNameing(names)

def moveEachPath(){

}

def fileNameing(...names, ...created, ...modified){
    TIME= created + modified
    for file_name in names:  
        if(file_name == DEFAULT){
            pass;
        } elif(file_name == FIRS) {
            return DATE+"_1"
        } else {
            numbers= file_name[-2]
            return DATE+numbers
        }
}
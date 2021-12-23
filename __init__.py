import datetime
import modifyFileName
import filePathing

def renaming():
    DATE= datetime.date.today().strftime("%d%m%Y")
    DATE= DATE + ""

    # get file-titles (written)
    # dir: role->end string "/"
    for file_name in arrays:
        old_name = f"{dir}{file_name}"
        format= f'{DATE}_{i}.mp4'
        new_name = f"{dir}{format}"
        os.rename(old_name, new_name)

def init():
    try:
        renaming()
    except FileExistsError as exist_e:
        print(exist_e+"")


init()
os.rename(file_name, TITLE)

# Main
# 1. Get File directory
dir= filepathing.getKubunPath()

# 2. Make data folder
makeForders(dir)

# @todo 3. File renaming selections
#       modifyFilename::defaultName()
#       self.renaming()
defaultName(filePathing.getKunPath())

# 4. Move files at the each foleders
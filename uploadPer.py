# detali : Get auto for Upload each files
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
#           https://twitter.com/dong_ub
# @history, @Date  
#   - 10-11 21:07 building core

from datetime import date
import os

files= [1,2,3,4,5]
file_sizes= [11,22,33,44,55]
file_size: int
# data: str
TOKENs= list()

PATH= 'c:/Users/test/Documents/Sound recordings'
FILE= "upload.txt"

# return both index, value
for index, file in files:
    with open(f'{FILE}', 'r') as f:
        commend = str(f.read())
        # @todo bash commend convert
        print(commend)
        print(str(f"-d 'file_size={file_sizes[index]}'"))

    # print(f'file: {file}')

# -d 'fuid=7b40c3f085481e8fb4feb2a7c914905b' \
# -d 'file_name=Screenshot 2021-07-09 at 15.47.05.png' \
# -d 'file_type=png' \
# -d 'total_chunks=1'
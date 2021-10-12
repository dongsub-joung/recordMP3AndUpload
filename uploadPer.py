# detali : Get auth at ufile.io for Upload each files
# @auther: Joung DongSub
# @Contact: e-mail or twitter  
#           joungdongsub1103@gmail.com  
#           https://twitter.com/dong_ub
# @history, @Date  
#   - 10-11 21:07   building core
#   - 10-12 20:49   First of all, what one single file upload server set on today's.

from datetime import date
import os

files= [1,2,3,4,5]
file_sizes= [11,22,33,44,55]
file_size: int
# data: str
TOKENs= list()

PATH= 'c:/Users/test/Documents/Sound recordings/TOKEN'
FILE= 'fuid.bat'

for index, file in enumerate(files):
    with open(f'{str(PATH+FILE)}', 'r') as f:
        commend = str(f.read())
        # @todo bash commend convert
        # init .bat, then get the token 
        TOKEN\file_size.txt
    # print(f'file: {file}')



# -d 'fuid=7b40c3f085481e8fb4feb2a7c914905b' \
# -d 'file_name=Screenshot 2021-07-09 at 15.47.05.png' \
# -d 'file_type=png' \
# -d 'total_chunks=1'
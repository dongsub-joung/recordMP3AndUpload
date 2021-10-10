import datetime
import os

PATH= 'c:/Users/test/Documents/'
FOLDER= 'Sound recordings'

subdir: list()
subdir= os.

DATE= datetime.date.today().strftime("%d%m%Y")
d= DATE[0,2]
m= DATE[2,4]
y= DATE[4,0]

try:
    if not subdir in y:
        os.makedirs(f'{y}/{m}/{d}')
    elif not subdir in m:
        os.makedirs(f'{m}/{d}')
    else:
        os.mkdir(f'{d}')
except FileExistsError as exist_e:
    print(exist_e)
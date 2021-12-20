import datetime
import os
import filepathing

def init(subdir: str):

    DATE= datetime.date.today().strftime("%d%m%Y")
    DATE= DATE + ""
    d= DATE[0:2]
    m= DATE[2:4]
    y= DATE[4:0]

    try:
        if subdir in m:
            os.mkdir(f'{d}')
        elif subdir in y:
            os.makedirs(f'{m}/{d}')
        else:
            os.makedirs(f'{y}/{m}/{d}')
    except FileExistsError as exist_e:
        print(exist_e+"")


dir= filepathing.getKubunPath()
init(dir)
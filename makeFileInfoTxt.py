import Comm_filePathing

PATH= Comm_filePathing.getWinPath()
DATE= datetime.date.today().strftime("%d%m%Y")

CURRENT_INFOMATION_SUMMTION= f'SUM){DATE}.txt'

self.saveFileInfoInTXT(CURRENT_INFOMATION_SUMMTION, PATH)
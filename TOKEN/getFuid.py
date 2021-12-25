# ./bat
# %file_sizes%= read(file_size.txt)
# curl 'https://up.ufile.io/v1/upload/create_session' \
# -d 'file_size={%file_sizes%}'

# > ./ fuid.txt


def getUploadingSize(index: int, list: list):
    return list[int]

def getFuid(file_sizes: int):
    # os.system.__code__("curl 'https://up.ufile.io/v1/upload/finalise' \")
    DIR_TOKEN= '/TOKEN/fuid.txt'
    
    try:
        token= os.read(DIR_TOKEN)
        return str(token)
    except Exception as e:
        print(e+"fuid")
        return str(e)


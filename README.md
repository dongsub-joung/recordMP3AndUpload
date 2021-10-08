# Record Sound Files And Upload automatly  

## Progress Arrow  
1. Scann the relative directory(For to get files info).    
2. Make the folder on date.  
3. converte the files name to "generated-moified"  
4. Upload the files, then midifiy the folder's title at time.  
5. voice recorder make the new dir for saving.  
> if new files are, perblishing on and repeating.

* when if you back around the host-service, you need it(ufile.io)   
* Before uploading, do auto-transfomation from "audio file form" to "picture form   

## ENV
- Python 3
- https://ufile.io  

## Files Usage  

- Node File Valuable infomation(Once get "stat_result" when init)  
    by OS __init__.pyi  

```py
st_mode: int  # protection bits,
    st_ino: int  # inode number,
    st_dev: int  # device,
    st_nlink: int  # number of hard links,
    st_uid: int  # user id of owner,
    st_gid: int  # group id of owner,
    st_size: int  # size of file, in bytes,
    st_atime: float  # time of most recent access,
    st_mtime: float  # time of most recent content modification,
    st_ctime: float  # platform dependent (time of most recent metadata change on Unix, or the time of creation on Windows)
    st_atime_ns: int  # time of most recent access, in nanoseconds
    st_mtime_ns: int  # time of most recent content modification in nanoseconds
    st_ctime_ns: int  # platform dependent (time of most recent metadata change on Unix, or the time of creation on Windows) in nanoseconds
    if sys.version_info >= (3, 8) and sys.platform == "win32":
        st_reparse_tag: int
    if sys.platform == "win32":
        st_file_attributes: int
    def __getitem__(self, i: int) -> int: ...
    # not documented
    def __init__(self, tuple: Tuple[int, ...]) -> None: ...
    # On some Unix systems (such as Linux), the following attributes may also
    # be available:
    st_blocks: int  # number of blocks allocated for file
    st_blksize: int  # filesystem blocksize
    st_rdev: int  # type of device if an inode device
    st_flags: int  # user defined flags for file

    # On other Unix systems (such as FreeBSD), the following attributes may be
    # available (but may be only filled out if root tries to use them):
    st_gen: int  # file generation number
    st_birthtime: int  # time of file creation

    # On Mac OS systems, the following attributes may also be available:
    st_rsize: int
    st_creator: int
    st_type: int
```  

## Reference  
- https://help.ufile.io/en/article/upload-files-1p925sk/  
import os
import time
import re
def syncfile():
    fp=open("c:\\Python27\\myproject\\myapp\\access_to_kedbfiles.txt")
    data=fp.read()
    fp.close()
    find=r'%s'%data
    global full,full1
    os.chdir(find)
    file1=[]
    full=[]
    full1=[]
    for root,folders,files in os.walk('.'):

        file1=files
    for i in file1:
        if re.search('.xls',i):
            j= os.path.abspath(i)
            full.append(j)
    return full

'''
from importlib.metadata import distributions  
import os, time

for dist in distributions():
    print("%s %s: %s" % (dist.metadata["Name"], dist.version, time.ctime(os.path.getctime(dist._path))))
'''


import magic
file_magic = magic.Magic(magic_file="E:/Coding/RAG/Code/libmagicwin64-master/magic.mgc")

import sys
import hashlib
import os

BUF_SIZE = 65536

md5 = hashlib.md5()
sha1 = hashlib.sha1()

try:
    filepath = sys.argv[1]
except:
    filepath = input('File Path -> ')
finally:
    try:
        with open(filepath, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
    except:
        print("Invalid filepath!")
        input()
        os._exit(0)

print("Hash: {0}".format(md5.hexdigest()))
input()

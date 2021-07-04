import os
import hashlib
file_location = os.path.abspath("md5 encoding.txt")
hasher = hashlib.md5()
with open(file_location,'rb') as file:
    content = file.read()
    hasher.update(content)
print(hasher.hexdigest())
import hashlib       # importing hashlib package to perform md5 encryption
hashing = input("Enter the string to be md5 hashed:- ")       # accepting the string from user to be hashed
hashed = hashlib.md5(hashing.encode())       #hashing the string 
print("The byte equivalent of hash is : ", hashed.digest())       # printing the Byte Equivalent of Hash
print("The hexadecimal equivalent of hash is : ", hashed.hexdigest())       # printing the Hexadecimal Equivalent of Hash

import hashlib

userName = "Me"
userPassword = "hello"



file = open('test.txt', 'r')
lines = file.readlines()
for line in lines:
    items = line.strip().split('/')
        #checking if username matches what is stored in file and if the hashed pw matches
    if items[0] == userName and items[1] == hashlib.sha256(userPassword.encode()).hexdigest():
            login_successful = True
            break
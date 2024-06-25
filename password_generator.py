import random
def password():
    options='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    x=int(input("Enter the length of the password: "))
    pwd=''
    for i in range(1,x+1):
        x=random.choice(options)
        pwd+=x
    print("The password is: ",pwd,'\n')
password()
while True:
    repeat=int(input("Generate another password?\nYES=1\nNO=2\n"))
    if repeat==1:
        password()
    elif repeat==2:
        exit()
    else:
        print("Invalid Input!!")
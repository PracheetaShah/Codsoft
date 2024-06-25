def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def exp(x,y):
    return x**y
while  True:
    choice=int(input(("Press 1 to start\nPress 2 to exit\nEnter your choice: ")))
    if choice==1:
        print("+  : addition\n-  : subtraction\n*  : multiplication\n/  : division\n^  : exponent")
        operator=input("Choose any operation from above: ")
        num1=int(input("Enter the 1st number: "))
        num2=int(input("Enter the 2nd number: "))
        if operator=="+":
            print("Sum is: ",add(num1,num2),'\n')
        elif operator=="-":
            print("Difference is: ",sub(num1,num2),'\n')
        elif operator=="*":
            print("Product is: ",mul(num1,num2),'\n')
        elif operator=="/":
            print("Quotient is: ",div(num1,num2),'\n')
        elif operator=="^":
            print("The exponent value is: ",exp(num1,num2),'\n')
        else:
            print("operator not available")
    elif choice==2:
        print("Done")
        exit()
    else:
        print("Invalid input")
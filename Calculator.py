m="yes"
while m=="yes": 
    print("***Calculator***")
    num1=int(input("Enter the first Number: "))
    num2=int(input("Enter the Second Number: "))
    op=input("Enter the Operator:(+,-,*,/): ")
    if op=='+':
        print("Sum of Two Number is: "+str(num1+num2))
    elif op=='-':
        print("Sum of Two Number is: "+str(num1-num2))
    elif op=='*':
        print("Sum of Two Number is: "+str(num1*num2))
    elif op=='/':
        print("Sum of Two Number is: "+str(num1/num2))
    else:
        print("Invalid Input...")
    m=input("Do you to Run Again enter yes: ")

year=int(input("Enter the year"))
if year%4==0 and year%100!=0:
    if year%400==0:
        print("Its leap year")
    else:
        print("Its not yer year")
else:
    print("Its not yer year")
    
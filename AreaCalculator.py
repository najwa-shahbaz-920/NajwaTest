choice="yes"
while choice=="yes":
    print("Area Calculator")
    print("1-Square")
    print("2-Rectangle")
    print("3-Triangle")
    print("4-Circle")
    ch=int(input("Enter your choice"))
    if ch==1:
        side=int(input("Enter the side of the square: "))
        print("The Area of Square: "+str(side*side))
    elif ch==2:
        len=int(input("Enter the Length of Rectangle: "))
        width=int(input("Enter the width of Rectangle: "))
        print("Area of Rectangle is: "+str(len*width))
    elif ch==2:
        len=int(input("Enter the Length of Triangle: "))
        width=int(input("Enter the width of Triangle: "))
        print("Area of Triangle is: "+str(0.5*len*width))
    elif ch==4:
        r=int(input("Enter the radius of the circle: "))
        print("The Area of Circle: "+str(2*3.14*r))
    else:
        print("Invalid input")
    choice=input("Do you want to Run again Enter yes: ")
    
    
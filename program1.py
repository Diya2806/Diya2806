a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))

print("1) Addition \n2) Subtraction\n3) Multiply\n4) Divide\n5) Modulo \n6) Exit")
ch=int(input("Enter your choice:"))
if ch==1:
    print("Addition=",a+b)
elif ch==2:
    print("Subtraction=",a-b)
elif ch==3:
    print("Multiply=",a*b)
elif ch==4:
    print("Divide=",a/b)
elif ch==5:
    print("Modulo=",a%b)
else:
    exit
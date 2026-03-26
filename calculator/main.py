from addition import add
import subtraction
from division import div as Division 
import multiplication as mul

if __name__=='__main__':
    print("Welcome to small calculator")
    print("select one operation 1) Addition \n 2) Subtraction \n 3)multiplication \n 4)dividion ")
    choice = int(input("Enter your choice"))
    if choice == 1:
        a,b = map(int,input("enter a and b").split())
        print(add(x=a,y=b))
    elif choice == 2:
        a,b = map(int,input("enter a and b").split())
        print(subtraction.sub(x=a,y=b))
    elif choice == 3:
        a,b = map(int,input("enter a and b").split())
        print(mul.mul(x=a,y=b))
    elif choice == 4:
        a,b = map(int,input("enter a and b").split())
        print(Division(x=a,y=b))
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")
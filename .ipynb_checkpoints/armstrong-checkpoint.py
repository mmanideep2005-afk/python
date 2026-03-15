#reverse of the number
'''n = int(input("enter a number:"))
temp=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print(s)
if s==temp:
    print("palindrome")
else:
    print("not a palindrome")'''
'''r=n%10
s=s+r #sumof numbers
n=n//10''' 
#Armstrong number
n = int(input("enter a number:"))
temp=n
count=0
while n>0:
    n=n//10
    count+=1
print(count)
s=0
while n>0:
    r=n%10
    s=s+r**count
    n=n//10
print(s)    
if s==temp:
    print("Armstrong")
else:
    print("not a Armstrong")
#perfect number



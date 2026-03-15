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
'''#Armstrong number
n = int(input("enter a number:"))
temp=n
count=0
while n>0:
    n=n//10
    count+=1
print(count)
s=0
n=temp
while n>0:
    r=n%10
    s=s+r**count
    n=n//10
print(s)    
if s==temp:
    print("Armstrong")
else:
    print("not a Armstrong")'''
#perfect number
n = int(input())
temp = n  # Use the original input stored in temp
s = 0
i = 1

# A perfect number is equal to the sum of its proper divisors
while i < n:
    if n % i == 0:
        s = s + i
    i = i + 1

if s == temp:
    print("Perfect Number")
else:
    print("not a Perfect Number")


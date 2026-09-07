# palindrome to check number
num=121
temp=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if temp==reverse:
    print("it is a palindrome")
else:
    print("not palindrome")



# reverse a string
s="anjali"
s1=list(s)
n=len(s1)
for i in range(n//2):
    s1[i],s1[n-1-i]=s1[n-1-i],s1[i]
    l=" ".join(s1)
print(l)



# reverse a string
s="anjali"
s1=list(s)
n=len(s1)
count=0
for i in range(n//2):
    if s1[i]!=s1[n-1-i]:
        count+=1
if count==0:
    print("palindrome")
else:
    print("not palindrome")


    # how to reverse a list of numbers
l=[1,2,3,4,5,6,7]
n=len(l)
for i in range(n//2):
    l[i],l[n-1-i]=l[n-1-i],l[i]
print(l)


# palindrome of list
l=[1,2,3,3,2,1]
n=len(l)
c=0
for i in range(n//2):
    
    if l[i]!=l[n-1-i]:
        c+=1
if c==0:
    print("palindrome")
else:
    print("not palindrome")
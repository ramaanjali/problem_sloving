#  using the for loop
# a=[3,2,7,9,6]
# targ=int(input("enetr a number"))
# for i in range (len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==targ:
#            print(i,j)
                
    #  usinf functions  and class and object
class sloution:
        def two_sum(self,num,targ):
            for i in range(len(num)):
                for j in range(i+1,len(num)):
                     if num[i]+num[j]==targ:
                            return i,j
num=list(map(int,input("enter a number").split()))
targ=int(input("enter a number"))
s=sloution()
print(s.two_sum(num,targ))



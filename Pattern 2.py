n=int(input('enter height(odd number)'))
for i in range(0,n):
   c=n 
   for j in range(0,i):
       if i+j==n-1:  #first increase cylcles then decrease(due to upper limits)
           break
       c=c-2 
   print(' '*((n-c)//2),'*'*c)

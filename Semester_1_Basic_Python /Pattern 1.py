n=int(input('enter height'))
c=0
for i in range(0,n):
   print(2*(n-c)*' ',end='')
   c=i
   for j in range (0,i+1):  #print increased values in row
       c=c+1
       print(c,end=' ')
   for j in range (0,i):   #print decresed values in row
       c=c-1
       print(c,end=' ')
   print() 


x=int(input('enter number of elements in list '))
a=[]
print('enter elements (numbers)')
for i in range(1,x+1):  #to take input
    print('element ',i,end=' ')
    p=(int(input()))
    a.append(p)
max=a[0]
print(a)
for i in range(0,len(a)):
    l=0
    for j in range(i,len(a)):
        l=l+a[j]  #to calculate sum of contiguous array
        if l>max:  #finding largest sum
            max=l
print('largest sum of contiguous subarray =',max)

a=[1,2,3,4,5,6,9,6,8]
for i in range(len(a)):
    max=0
    for j in range(i,len(a)):
         if max<a[j]: 
             p=j
             max=a[j]
    a[p]=a[i]
    a[i]=max
print(a)

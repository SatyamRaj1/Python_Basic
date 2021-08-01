a=[3,5,7,0,5,2,7,4]
for i in range(0,len(a)):
    flag=0
    for j in range(0,len(a)-i-1):
       if a[j+1]>a[j]:
           p=a[j+1]
           a[j+1]=a[j]
           a[j]=p
           flag=1
    if flag==0:
       break
print(a)

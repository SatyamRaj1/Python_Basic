max1=-4
max2=-65
a=[]
n=int(input())
for _ in range(n):
    name = input()
    score = float(input())    
    b=[name,score]
    a.append(b)
    if(max1<score):
        max2=max1
        max1=score
nam=[]
print(a)


for i in range(n):
    if(a[i][1]==max2):
        nam.append(a[i][0])        
nam.sort()
for j in nam:
    print(j)        
    

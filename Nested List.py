sum=0
a=[1,2,3,[4,5,6]]
for i in a:
    if type(i)==list:
        for j in i:
            sum=sum+j
    else:
        sum=sum+i
print(sum)        
 

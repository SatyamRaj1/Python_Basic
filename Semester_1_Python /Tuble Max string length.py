a=(1,12131,'ssf','sfdfge')
max=0
for i in a:
    if type(i)==str:
        if len(i)>max:
            max=len(i)
            val=i
print(max)
print(val)            

a=tuple(input('enter students name(separated by space)').split())
print('input tuple is',a)
b=()
for i in range(0,len(a)):
    c=0
    max=''
    for j in range(0,len(a)):
        if max<a[j] and a[j] not in b:
            max=a[j]
    b=b+(max,)        
print('tuple in ascending order:')
print(b)

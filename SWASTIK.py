n=int(input('enter height of central line(odd number)'))
for i in range(1,(n+1)//2):
    if i==1:
        print('*',' '*(n//2-3),'*'*(n//2+1))
    else:
        print('*',' '*(n//2-3),'*')
print('*'*n)
for i in range(((n+1)//2)+1,n+1):
    if i==n:
        print('*'*(n//2+1),' '*(n//2-3),'*')
    else:
        print(' '*(n//2-1),'*',' '*(n//2-3),'*')

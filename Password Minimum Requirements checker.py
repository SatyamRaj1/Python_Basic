x=input('give input(passwords separated by ,)')
x=x.split(',')
for i in x:
    if len(i)>5 and len(i)<13:
        a=0
        b=0
        c=0
        d=0
        for j in i:
            if ord(j)>47 and ord(j)<58:
                a=a+1
            elif ord(j)>64 and ord(j)<91:
                b=b+1
            elif ord(j)>96 and ord(j)<123:
                c=c+1
            else:
                d=d+1
        if (a*b*c*d)!=0:
            print(i,',')
 

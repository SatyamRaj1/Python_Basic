a='raja babu aayenge raja babu khana khayenge'
b=a.split()
c={}
for i in b:
    if i not in c.keys():
        c[i]=1
    else:
        c[i]=c[i]+1
print(c)

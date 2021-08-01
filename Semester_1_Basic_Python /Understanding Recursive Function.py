def f(n,str0):
    if n<=1:
        return n
    print(str0)
    return f(n-1,'left')+f(n-2,'right')
print(f(6,'center'))
    
    

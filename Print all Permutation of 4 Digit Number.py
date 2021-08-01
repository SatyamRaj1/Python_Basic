x=input('give any four digit number')
print('all permutations of given number is:')
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            if i!=j and j!=k and i!=k:   
                l=6-i-j-k
                print(x[i],x[j],x[k],x[l])
        

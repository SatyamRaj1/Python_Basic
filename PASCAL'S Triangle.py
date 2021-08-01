n=int(input('enter number of lines'))
a=[1]
print(a[0])    #printing first line
for i in range(0,n-1):       #loop for printing next n-1 lines
    b=[]                #creating empty list so it can store next line values
    for j in range(0,len(a)+1):    #every line has 1 more element than previous 
        if j==0 or j==len(a):    #first and last character of eachline is 1
            b.append(1)
        else:
            c=a[j-1]+a[j]  #pattern of pascal triangle
            b.append(c)
            
    for j in b:      #to print list in sting way
        print(j,end='  ')
    print()
    a=b            #assigning created line to next line

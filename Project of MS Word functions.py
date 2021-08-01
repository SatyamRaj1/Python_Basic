def T1(a,k):
    b=set(a.split())
    c=''
    for i in b:
        if len(set(i))>=k:   #to check no. of didtinct character
            c=c+i+' , '
    return c
def T2(a):
    c=0
    for i in a:
        if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123):  
            c=c+1
    return c
def T3(a):
    c=0
    for i in a:
        if ord(i)!=32 and i!='\n':   #except space and next line
            c=c+1
    return c
def T4(a,w):
    a=a.split()
    if w in a:   
        return True
    else:
        return False
def T5(a,k):
    a=a.split()
    b=''
    for i in a:
        if len(i)>=k:
            b=b+i+','
    return b        
def T6(a):
    a=a.split()
    maxl=0
    b=''
    for i in a:   #for maximum length
        if len(i)>maxl:
            maxl=len(i)
    for i in a:  #words of maximum length
        if len(i)==maxl:
            b=b+i+','
    return maxl,b        
def T7(a,w):
    a=a.split()
    c=0
    for i in a:
        if i==w:
            c=c+1
    return c        
def T8(a):
    b={}
    for i in a.split():
        if i not in b:
            b[i]=1
        else:
            b[i]=b[i]+1
    return b        
def T9(a):
    b={}
    d={}
    for i in a:   #to find frequency of all characters
        if i!=' ' and i!='\n':   #to store all characters other than space and '\n'
            if ord(i)>=97 and ord(i)<=122:  #to convert all small letters to capital
                i=chr(ord(i)-32)
            if i not in b.keys():
                b[i]=1
            else:
                b[i]=b[i]+1
    c=list(b.keys())   
    for i in range(0,len(c)):   #to store all characters in ascending order
        flag=0
        for j in range(0,len(c)-i-1):
            if c[j+1]<c[j]:
                p=c[j+1]
                c[j+1]=c[j]
                c[j]=p
                flag=1
        if flag==0:
            break
    for i in c:   #to find frequency of each character in ascending order
        d[i]=b[i]    
    return d
def T10(a):
    b=''
    for i in range(0,len(a)):
        if (a[i-1]==' ' or a[i-1]=='\n' or i==0)and ord(a[i])>=97 and ord(a[i])<=122:  #to convert first letter to capital
            b=b+chr(ord(a[i])-32)
        else:
            b=b+a[i]
    return b    
def T11(a):
    b=''
    for i in a:
        if ord(i)>64 and ord(i)<91:
            b=b+chr(ord(i)+32)        
        elif ord(i)>96 and ord(i)<123:
            b=b+chr(ord(i)-32)
        else:
            b=b+i
    return b    
def T12(a,w,r):
    b=''
    for i in a.split('\n'):   #to store all lines in different elements
        for j in i.split():   #to store all words in 2D list in each line
            if j==w:
                b=b+r+' '
            else:
                b=b+j+' '
        b=b+'\n'        
    return b
def T13(a,w,r):
    b=''
    for i in a:
        if i==w or i==chr(ord(w)-32):  
            b=b+r
        else:
            b=b+i
    return b    
def T14(a):
    b=''
    a=a.split('\n')
    for i in range(len(a)-1,-1,-1):  #reverse all lines
        a[i]=a[i].split()   
        for j in range(len(a[i])-1,-1,-1): # reverse position of each word in line
            b=b+a[i][j]+' '    
        b=b+'\n'    
    return b
def T15(a):
    b=''
    for i in a.split('\n'):   #to store each line separately
        t=''
        for j in i.split():  #to separate word in each line by using 2D list
            for k in range(len(j)-1,-1,-1):   #to reverse each word
                t=t+j[k]
            t=t+' '    
        b=b+t+'\n'
    return b    
def T16(a):
    b=''
    c=[]
    for i in a.split():  #to store distinct words
        if i not in c:
            c.append(i)        
    for i in c:    #to store all those words which occured only once
        n=0
        for j in a.split():
            if i==j:   
                n=n+1
            if n==2:
                break
        if n==1:   
            b=b+i+','
    return b
def T17(a,w):
    b=[]
    for i in a.split():  #to store all distinct words
        if i not in b:
            b.append(i)
    for i in range(0,len(b)):
        test=0
        for j in range(0,len(b)-1-i):   #bubble sort of all distinct words
            if b[j]>b[j+1]:
                sw=b[j]
                b[j]=b[j+1]
                b[j+1]=sw
                test=1
        if test==0:
            break
    c=[]
    if w=='asc':
        return b
    elif w=='desc':
        for i in range(len(b)-1,-1,-1):  #descending order
            c.append(b[i])
        return c
def T18(a,w):
    b=''
    for i in a.split('\n'):
        for j in i.split():
            if j!=w:
                b=b+j+' '
        b=b+'\n'        
    return b
def T19(a,n,w,win):
    fl=0
    a=a.split('\n')  #store all lines so that line can be check
    for i in range(0,len(a)):
        a[i]=a[i].split()   #store all words in sub lists
    for i in range(0,len(a[n-1])):
        if a[n-1][i]==w:   #n-1 is required line and loop to check word
            t=i
            fl=1
            break
    if fl==0:
        return 'word is not present'
    a[n-1].insert(t,win)
    b=''
    for i in range(0,len(a)):     #to store edited 2D list as string
        for j in range (0,len(a[i])):
            b=b+' '+a[i][j]
        b=b+'\n'    
    return b
def T20(a,w1,w2):
    a=a.split()
    b=''
    c=0
    for i in range(0,len(a)):   
        if c==1:   #to take only first slice
            break
        if a[i]==w1:  #starting word
            for j in range(i,len(a)-i):
                b=b+a[j]+' '     #store all mid words 
                if a[j]==w2:  #ending word
                    c=1
                    break
    return b
def T21(a):
    uc=0
    lc=0
    dig=0
    spe=0
    for i in a:
        if ord(i)>=65 and ord(i)<=90:
            uc=uc+1
        elif ord(i)>=97 and ord(i)<=122:
            lc=lc+1
        elif ord(i)>=48 and ord(i)<=57:
            dig=dig+1
        elif ord(i)!=32:
            spe=spe+1
    return uc,lc,dig,spe                   
print('enter your paragraph  (enter *#* in next line to finish entering,press enter for next line')
a=input()
x=input()
while(x!='*#*'):
    a=a+'\n'+x
    x=input()
y='y'    
while(y=='y'):
    print("""give task number you want to perform:
1.  Find the word with K distinct characters where K is an integer.
2.  Count the number of alphabets.
3.  Total length of paragraph excluding spaces
4.  Search any word is available in the string or not.
5.  find Words whose length is greater than or equal to k
6.  Length of longest word and find all words with longest length
7.  Count frequency of specific word
8.  Find frequency of all words
9.  Find frequency of each alphabet (capital and small are treated as same)
10. Capitlize first alphabet of each word
11. Change case of all alphabets  (capital-small and small-capital)
12. Replace a words throughout paragraph
13. replace a alphabet throughout paragraph  
14. Reverse all content
15. Reverse each word
16. Find all unique words(occured only once) 
17. Print all distinct words in increasing and decreasing order
18. Delete a word
19. Insert a word by refering line and word
20. slicing(picking a part of paragraph)
21. Count all lower case, upper case, digits, and special symbols""")
    t=int(input())
    if t<1 or t>21:
        print('invalid task number')
    elif t==1:
        k=int(input('enter min requirement of distinct characters in words'))
        print('words with ',k,' distinct characters are:','\n',T1(a,k))
    elif t==2:
        print('total number of alphabets are',T2(a))
    elif t==3:
        print('Total length of paragraph excluding spaces is',T3(a))
    elif t==4:
        w=input('enter word whose presence you want to check')
        if T4(a,w)==True:
            print('it is present')
        else:
            print('it is not present')
    elif t==5:
        n=int(input('give minimum length(k)'))
        print(T5(a,n))
    elif t==6:
        w1,w2=T6(a)
        print('length of longest words',w1,'\n','longest words are:',w2)
    elif t==7:
        w=input('enter word whose frequency you want to check')
        print('frequency is',T7(a,w))
    elif t==8:
        print('all words with their frequency(case sensitive)','\n',T8(a))
    elif t==9:
        print('frequency of all alphabets,digits,symbols,spaces,no. line are:'+'\n','(here capital and small are different)',"\n",T9(a))
    elif t==10:
        print('paragraph after capitalisation of first letter is ','\n',T10(a))
    elif t==11:
        print('paragraph after reversing case of each alphabet is','\n',T11(a))
    elif t==12:
        w=input('which word is to be replaced: ')
        r=input('give word by which given word is to be repaced: ')
        print('paragraph after replacing is','\n',T12(a,w,r))
    elif t==13:
        w=input('which alphabet you want to replace(both capital and small will be replaced) \n (enter in lower case only) ')
        r=input('give alphabet by which given alphabet is to be repaced: ')
        print('paragraph after replacing is','\n',T13(a,w,r))
    elif t==14:
        print('reversed content is','\n',T14(a))
    elif t==15:
        print('paragraph after reversing each word is:','\n',T15(a))
    elif t==16:
        print('all unique words are:','\n',T16(a))
    elif t==17:
        w=input('enter asc for ascending and desc for descending order : ')
        print('sorted distinct words are:','\n',T17(a,w))
    elif t==18:    
        w=input('give word to be deleted: ')
        print('paragraph after deleting all words ','\n',T18(a,w))
    elif t==19:    
        win=input('give word to be inserted')
        n=int(input('enter line number'))
        if n<1 or n>len(a.split('\n')):
            print('line number is not valid')
        else:
            w=input('enter word before which in line '+str(n)+' you want to insert')
            print('updated paragraph is','\n',T19(a,n,w,win))
    elif t==20:
        w1=input('enter starting word ')
        w2=input('enter ending word ')
        print('selected part of paragraph is (apperaring first):','\n',T20(a,w1,w2))
    elif t==21:    
        w=T21(a)
        print('upper case letters: ',w[0],'  lower case letters: ',w[1])
        print('digits: ',w[2],'   special characters: ',w[3])
    y=input('enter y to continue ')    

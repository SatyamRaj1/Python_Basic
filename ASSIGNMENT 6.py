def Q1(a):
    if int(a[0])>int(a[1]):
        if int(a[0])>int(a[2]):
               return a[0]
        else:
            return a[2]
    else:
        if int(a[2])>int(a[1]):
               return a[2]
        else:
            return a[1]         
def Q2(a):
    b=''
    for i in range(len(a)-1,-1,-1):    #to reverse string
        b=b+a[i]
    return b
def Q3(a):    #recursion to find factorial
    if a==1 or a==0:
        return 1
    else:
        return a*Q3(a-1)  
def Q4(a,n):
    a[0]=int(a[0])
    a[1]=int(a[1])
    if a[0]>a[1]:   #to find max for proper range
        m=a[0]
        a[0]=a[1]
        a[1]=m
    if n>a[0] and n<a[1]:    #to check if number is in range
        return 'number is in the given range'
    else:
        return 'number is not in given range'
def Q5(a):
    u=0
    l=0
    for i in a:
        if ord(i)>=65 and ord (i)<=90:   #to check upper case
            u=u+1
        elif ord(i)>=97 and ord(i)<=122:   #to check lower case
            l=l+1
    return u,l
def Q6(a):
    b=[]
    for i in a:
        if i not in b:   #for unique values
            b.append(i)
    return b
def Q7(a):
    for i in range(65,91):
        if chr(i) not in a and chr(i+32) not in a:    #to check if any alphabet is not present 
            return 'string is not pangram'
    return 'string is pangram'
def Q8_a():    #declaring second function
    print('it is statement from second function')
def Q8():   #first function
    print('this is a statement from first function')
    Q8_a()   #calling second function from first function
def Q9():            
    return Q10.__code__.co_nlocals     #predefined function to find number of local variables
def Q10(n):
    if n==0:
        print('nothing to be printed')     
    elif n<0:
        print('rows cant be negative')
    else:
        a=[1]
        print(n*' ',a[0])
        if n>1:
            for i in range(0,n-1):    #to print pascal's triangle
                b=[]
                print((n-i)*' ',end='')
                for j in range(0,len(a)+1):
                    if j==0 or j==len(a):   #for first and last elements
                        b.append(1)
                    else:
                        b.append(a[j]+a[j-1])   #defination
                    print(b[j],end=' ')
                print()
                a=b
def Q11(a,t):
    for i in range(len(a)):
        flag=0
        for j in range(0,len(a)-1-i):    #bubble sort
            if a[j+1]<a[j]:
                p=a[j+1]
                a[j+1]=a[j]
                a[j]=p
                flag=1
        if flag==0:
            break   
    b=''
    if t=='asc':    #to print again in hyphen form
        for i in range(0,len(a)):
            b=b+a[i]
            if i!=len(a)-1:
                b=b+'-'
        return b    
    if t=='desc':
        for i in range(len(a)-1,-1,-1):
            b=b+a[i]
            if i!=0:
                b=b+'-'
        return b
    
def Q12(a):
    if len(a)!=2:   
        return 'invalid range'
    a[0]=int(a[0])
    a[1]=int(a[1])
    if a[0]>a[1]:
        mx=a[0]
        a[0]=a[1]
        a[1]=mx
    return [i**2 for i in range(a[0],a[1]+1)]   #list comprehension to find square of each number in the range
def Q13(a,b):
    return a+b,a-b
def Q14(p,name='',sal=9000):    #default arguement
    global det   #to store information in dictionary  
    if p!='y':
        return det   #when called to print information
    else:
        det[name]=sal    #when called to store information
def Q15(n):    #recursion to find sum
    if n<=1:
        return n
    else:
        return n+Q15(n-1)
def Q16():
    return 'statement from original function'
def Q17(a):   #recursion to find multiplication
    if len(a)==0:   #if all elements are multiplied
        return 1
    else:
        return (int(a.pop()))*Q17(a)
def Q18(a,p):  #recursion to find if number is prime or not
    if p==1:   #if number is prime finally p will be 1 a
        return 'number is prime'   
    elif a%p==0 or p<1:   #no number <2 is prime and if number is divisible by any other number it is not prime
        return 'number is not prime'
    else:
        return Q18(a,p-1)   #recursion
def Q19(a):
    if a==Q2(a):   #Q2(a) reverse string
        return 'string is pallindrome'
    else:
        return 'string is not pallindrome'
def Q20(a):
    return 6*(a**2)+3*a+2   #defination
def Q21(a):
    return n**2+1     #defination
y='y'
while y=='y':
    print('''Questions list is:
1. Write a Python function to find the MAX of three numbers.
2. Write a Python function to reverse a String.
3. Write a Python function to calculate the factorial of a number (a non-negative integer).
4. Write a Python function to check whether a number is in a given range.
5. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
6. Write a Python function that takes a list and returns a new list with unique elements of the first list.
7. Write a Python function to check whether a string is a pangram or not.
Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
8. Write a Python Program to access a function inside a function.
9. Write a Python Program to detect the number of local variables declared in a function.
10. Write a Python function that prints out the first n rows of Pascal’s triangle.
Note: Each number is the two number above it added together.
11. Write a Python Program that accepts a hyphen-separated sequence of words as input and prints the word in a hyphen-separated sequence after sorting them alphabetically.
12. Write a Python function to create and print a list where the values are square of numbers between 1 and 30(both included).
13. Write a Python function such that it can accept two variables and calculate the addition and subtraction of it. 
14. Create a function in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000.
15. Write a recursive function to calculate the sum of numbers from 0 to 20.
16. Assign a different name to function and call it through the new name.
17. Write a Python function to multiply all the numbers in the list.
18. Write a Python function that takes a number as a parameter and check if the number is prime of not.
19. Write a Python function that checks whether a passed string is palindrome or not.
20. Write a Python function that takes x as argument and returns y. Call the function for x = 2 and print the answer.
Formula: y = 6x^2 + 3x + 2
21. Write a Python function x(n) for computing an element in the sequence x(n) = n^2 + 1
Call the function for n = 4 and print the result. ''')
    q=int(input('enter question no. '))
    if q<1 or q>21:
        print('wrong question number ')
    elif q==1:
        a=input('enter three numbers separated by space ').split()
        if len(a)!=3:
            print('enter 3 numbers only')
        else:
            print('maximum =',Q1(a))
    elif q==2:
        a=input('enter string')
        print('reversed string is:',Q2(a))
    elif q==3:
        n=int(input('give number to find its factorial '))
        if n<0:
            print('factorial of negative number dont exist')
        else:
            print('factorial of',n,'is',Q3(n))
    elif q==4:
        a=input('give starting and ending points of the range separated by space ').split()
        n=int(input('give number you want to check '))
        print(Q4(a,n))
    elif q==5:
        a=input('give any string ')
        u,l=Q5(a)
        print('number of upper case letters:',u,'  number of lower case letters:',l)
    elif q==6:
        a=input('enter elements of lists separated by space ').split()
        print('list containing all unique elements is ',Q6(a))
    elif q==7:
        a=input('give string to check is it pangram or not ')
        print(Q7(a))
    elif q==8:
        Q8()
    elif q==9:
        print('number of local variables in  Q10 function are:',Q9())
    elif q==10:
        n=int(input('enter number of rows you want to print '))
        Q10(n)
    elif q==11:
        a=input('enter sequence separated by hyphen ').split('-')
        p=input('enter asc for ascending and desc for descending ')
        print('sorted sequence is ',Q11(a,p))
    elif q==12:
        a=input('enter range of numbers to print squares of all the numbers between them(for given question 1 and 30)  (separated by space)').split()
        print(Q12(a))
    elif q==13:
        a=input('enter both number separated by space ').split()
        s,d=Q13(int(a[0]),int(a[1]))
        print('addition=',s,'subtracion first-second =',d)
    elif q==14:
        a=[]
        det={}
        p='y'
        while p=='y':   #loop to take input details of all employees
            a=input('enter employee name and salary separated by space (enter name only if you dont want to enter salary) '+'\n').split()
            if len(a)==1:
                Q14(p,a[0])
            elif len(a)==2:
                Q14(p,a[0],a[1])
            else:
                print('enter only name and salary')
            p=input('enter y to enter more details ')    
        print('details of all employees are: \n',Q14(p))   #to print details
    elif q==15:
        n=int(input('enter number to calculate sum of all natural numbers less than equal to it'+'\n'))
        print(Q15(n))
    elif q==16:
        new=Q16    #assigning different name to function Q16
        print(new())   #calling function through new name
    elif q==17:
        a=input('enter elements(numbers only) of lists separated by spaces ').split()
        print('multplication =',Q17(a))
    elif q==18:
        a=int(input('enter number to check is it prime or not '))
        print(Q18(a,a//2))   #to check number a is divisible by all numbers less than a//2
    elif q==19:
        a=input('enter string to check is it palindrome or not ')
        print(Q19(a))
    elif q==20:
        a=int(input('enter value of x to evaluate y = 6x^2 + 3x + 2  '))
        print('y =',Q20(a))
    elif q==21:
        n=int(input('enter n to find element of sequence x(n) = n^2 + 1  '))
        print('x(n) corresponding to given n is',Q21(n))
    y=input('enter y to continue ')    
        
        
            
            
        
        
            
            

    

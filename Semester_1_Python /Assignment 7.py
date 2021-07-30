def Q1(a,b):
    d={}
    e={}
    if len(a)==len(b): #no need to run loops if lengths are not same
        for i in a:   #to calcuate frequency of each alphabet is string1
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in b:   #to calcuate frequency of each alphabet is string2
            if i not in e:
                e[i]=1
            else:
                e[i]=e[i]+1
        if d==e:    #if all alphabets and their frequency are same then they are permutaions
            return 'both strings are permutaions of each other' 
    return 'both stings are not permutaions of each other'   #if length is not same or alphabets,frequency are not same   
def Q2(a):
    t=1
    zero=0
    b=5
    while ((a//b)!=0):
        b=5
        b=b**t    #to calculate power of 5 
        zero+=a//b  
        t+=1
    return zero
def Q3_1(a,b,s=0):   #to calculate sum of digits raise to order
    if a==0:
        return 0
    return ((a%10)**b)+(Q3_1(a//10,b,s))   #add last digit raise to order and number from recursion to find next digits raise to power
def Q3_2(a):
    l=0
    while(a!=0):   #calculate order
        l+=1
        a=a//10    #reducing digits by 1
    return l    
def Q3_3(a,s):
    if a==s:
        print('it is armstrong')
    else:
        print('it is not armstrong')
def Q4(a):
    if len(a)==1:
        return int(a[0])  
    else:
        return int(a.pop())+Q4(a)  #last element + again recursion to find all elements in that way
def Q5(a):
    if len(a)==1:   #base case
        return a  #for remaining last element (first element)
    else:
        return a[-1]+Q5(a[:-1])   #last word +recurrsion to again find last element in remaining string
def Q6(a,r,n):
    if n==1:  #base case
        return a   #for adding a (first element) 
    else:
        return a*(r**(n-1))+Q6(a,r,n-1)  #from defination S(n)=S(n-1)+ar**(n-1)
def Q7(a):
    if a<=1:   #base case
        print(a)
    else:
        Q7(a-1)  #first store elements in stack then take out and print  
        print(a)  #from last in first out method of stack it will print 1 first (ascending)
def Q8(a):
    if a<=1:  #base case
        print(a)
    else:
        print(a)   #first printing then going on next recursion as upper limit is given so that descending order can be printed
        Q8(a-1)
def Q9(a):
    if a==0:  #base case
        return 1   #0!=1
    else:
        return a*Q9(a-1)   #from defination n!=n*(n-1)!
def Q10(a):   
    if a<=1:   #base case
        return 1
    else:
        return Q10(a-1)+Q10(a-2)   #defination a(n)=a(n-1)+a(n-2)
def Q11(a,b): 
    if a==0:  #base case 1    from a%b if zero is came then b is g.c.d
        return b
    if b==0:   #base case 2   if b==0 then is g.c.d  
        return a
    return Q11(b,a%b)   #if b divides a then b is g.c.d  and also it will help to swap if other number is larger
def Q12(a,b):
    return (a*b)/Q11(a,b)  #L.C.M * G.C.D =a*b
def Q13(a,b):
    if b==0 or a==b:   #base case
        return 1    #C(n,0)=C(n,n)=1
    return Q13(a-1,b-1)+Q13(a-1,b)   #from formula C(n,r)=C(n-1,r)+C(n-1,r-1)
def Q14(a):
    if len(a)==1:   #base case  when only 1 element is remaining
        return int(a[0])
    if int(a[0])<Q14(a[1:]):  #using recursion it will return highest in the list as it will continue check each element with all elements after it
        return int(a[0])      #will return that no. a[0] if it is highest in all members after it
    else:
        return Q14(a[1:])       
def Q15(a):
    if len(a)==1:   #base case  when only 1 element is remaining
        return int(a[0])
    if int(a[0])>Q15(a[1:]):  #using recursion it will return lowest in the list as it will continue check each element with all elements after it
        return int(a[0])
    else:
        return Q15(a[1:])
def Q16(a):
    if a//10==0:  #base case when only 1 digit is present
        return 1
    return 1+Q16(a//10)  # 1+recursion for number with 1 less digit 
def Q18():  
    x=input('enter number( will raise error if any other thing is given) ')
    if x.isdigit():  #if only numbers are in string given as input this condition will convert it's type to integer
        x=int(x)
    if type(x)!=int:   #if type of x is not int it will raise error
        raise TypeError('Only integers are allowed')
def Q19():
    try:
        x=int(input('enter the number x: '))
        y=int(input('enter the number y: '))
        print('yeah Yeah ! Your answer(quotient when x/y) is :', x//y)
    except ZeroDivisionError:         #when divided by zero
        print('Sorry ! You are dividing by zero')
        
                    #Q17
'''Answer of Q17
(a) def fact(num):
          if num==0:
               return 1
          else:
               return num*fact(num-1)
resason:    it is a recursive function for finding factorial so in recursive case acc. to defination of factorial n!=n*(n-1)!
so for factorial of n-1 funtion will again repeat(recursion) and with each time multiplying by n

(b)   def test(i,j):
           if i==0:
               return j
           else:
               return (i-1,i+j)
      print(test(4,7))
Ans: 17
Exp:  this program is made in such a way that it will add j and numbers less than equal to i upto 0 and in place of 0 they are adding 1
      in each recursion value of i decreases by 1 and value of j is added with i and in base case when i==0 it return 1 j which has become now 17
      
(c)l=[]
   def convert(b):
       if(b==0):
          return l
       dig=b%2
       l.append(dig)
       convert(6//2)
   convert(6)
   l.reverse()
   for i in l:
       print(i,end="")
output:  110
exp:   this program will calculate binary equivalent of given number(here 6) here it is calculated using division method where
       dig will insert remainder when divided by 2 in list and then function is called again by recursion after dividing it with 2
       this process goes on till b(number)==0 then it will return list having binary expansion in reverse order as binary number is considered from below
       (start from last remainder and finish at first remainder) so using reverse function exact binary number is calculated in list having each digit then it is printed as string using for loop

(d) def fun(n):
       if (n>100):
           return n-5
       return fun(fun(n+11))
    print(fun(45))   
output: 100
Exp: as this is a function with nested recurrsion so first inside function will get called and then outside
     initially the function will keep get calling till value of n is less than 100. since n=45 and 11 is added firstly it will keep calling until n become 110
     then value of n will get reduce by 5 two times when n==100 again 11 will added and then 2 times 5 reduces and pass 101 to next recursion
     it will decrease value whenever n will be greater than 100 and increase whenever n=<100 finally it will return n==100

(e)   ans:  c) b() is tail recursive but a() isn't
      exp:   in a() after return statement n is multiplied with next recurrsion so some actions are performed after return statement in else part so it is non tail recursive
             while in b() no action is performed after return statement only function is called again so it is tail recurrsive
         '''
y='y'
while(y=='y'):
    print('''Questions list
Q1) Write a iterative python program using function:
For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Q2)Write a non recursive python program using function to count trailing zeroes in factorial of a number
Q3)Write a python program to check Armstrong Number.Your Program must have 3 different functions
● Define a Function to calculate x raised to the power y (This function must be recursive).
● Define a Function to calculate order of the number where order means order is number of digits.( This function must be Iterative )
● Define a Function to check whether the given number is Armstrong number or not.( This function must be Iterative )
Q4)Write a recursive python program to sum all the elements of a list.you can store list internally
Q5)Write a recursive python program to reverse a date in the format "yyyyMMdd
Q6)Write the recursive implementation to get the sum of first n terms of G.P.
Q7)Write a recursive python program that takes in the upper limit and prints all numbers within the given range in increasing order.
Q8)Modify above program in Q7 and print now in decreasing order using recursion
Q9)Write a recursive python program to find the factorial of an integer
Q10)Write a recursive python program to print the fibonacci series upto n_terms
Q11)Write a recursive python program to return gcd of a and b
Q12)Write a recursive python program to return lcm of a and b
Q13)Write a recursive python program that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k).
Q14)Write a recursive python program to find Minimum element of array
Q15)Write a recursive python program to find Maximum element of array,you can store input array internally.
Q16) Write a recursive python program find out and return the number of digits present in a number recursively.
Q17) In comments
Q18 Write a python program Raise a TypeError if x is not an integer using “raise” keyword to raise an exception.
Q19 Write a python program with try-except for division of x by y and show
(i)No exception, so try clause will run.
(ii)There is an exception so only except clause will run.''')
    q=int(input('enter question number: '))
    if q<1 or q>19:
        print('invalid question number')
    elif q==17:
        print('it is written as a comment')
    elif q==1:
        s1=input('enter string 1 ')
        s2=input('enter string 2 ')
        print(Q1(s1,s2))
    elif q==2:
        a=int(input('enter number to find trailing zeroes in its factorial '))
        print('number if trailing zeroes =',Q2(a))
    elif q==3:
        a=int(input('enter number to check whether it is armstrong or not '))
        b=Q3_2(a)   #to calculate order
        s=Q3_1(a,b)   #to calculate sum of digits raised to order
        Q3_3(a,s)     #to check if number equal to sum of digits raised to order
    elif q==4:
        a=input('enter elements of lists(numbers only) (separated by space) ').split()
        print('sum of all elements of list =',Q4(a))
    elif q==5:
        a=input('enter date ')
        print('reversed date =',Q5(a))
    elif q==6:
        a=int(input('enter a(first term of G.P) '))
        r=int(input('enter r(common ratio of G.P) '))
        n=int(input('enter n(no.of terms upto which sum is to be calculated '))
        print('sum = ',Q6(a,r,n))
    elif q==7:
        a=int(input('enter upper limit '))
        Q7(a)
    elif q==8:
        a=int(input('enter upper limit '))
        Q8(a)
    elif q==9:
        a=int(input('enter number to find its factorial '))
        print('factorial =',Q9(a))
    elif q==10:   
        a=int(input('enter no. of terms you want to print '))
        for i in range(0,a):
            print(Q10(i),end=' ')
        print()
    elif q==11:  
        a=input('enter numbers(separated by space) to find G.C.D ').split()
        print('G.C.D. = ',Q11(int(a[0]),int(a[1])))
    elif q==12:
        a=input('enter numbers(separated by space) to find L.C.M ').split()
        print('L.C.M. = ',Q12(int(a[0]),int(a[1])))
    elif q==13:
        a=input('enter n and k (separated by space to find Binomial Coefficient C(n,k) ').split()
        print('Binomial Coefficient C(n,k) =',Q13(int(a[0]),int(a[1])))
    elif q==14:  
        a=input('enter elements(only numbers) of list(array) separated by space ').split()
        print('minimum =',Q14(a))
    elif q==15: 
        a=input('enter elements(only numbers) of list(array) separated by space ').split()
        print('maximum =',Q15(a))
    elif q==16:   
        a=int(input('enter a number to calculate number of digits present in it '))
        print('number of digits =',Q16(a))
    elif q==18: 
        Q18()
    elif q==19:
        Q19()
    y=input('enter y to continue ')

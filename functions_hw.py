
# 5/ Write a Python program to reverse a string.
def ReverseString (string):
    i=len(string)-1
    reverse=""
    while i>=0 :
        reverse = reverse + string[i]
        i = i-1 
    return reverse 

# to check it uncomment the code below 
'''
s = "hi bye"    
print(ReverseString(s))
'''

# 1/ Write a Python function that checks whether a passed string is palindrome or not.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def deleteSpace(string) :
    s= string.split()
    res=""
    for i in s:
        res = res+i 
    return res

def Palindrome (string):
    s = deleteSpace(string)
    return (ReverseString(s)==s)

# to check it uncomment the code below 
'''
print(Palindrome("nurses run"))
print(Palindrome("madam"))
print(Palindrome("hi bye"))
'''
# 2/ Write a Python function that takes a number as a parameter and checks if the number is prime or not.
# A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def Prime (n):
    for i in range(2,int(n/2)+1):
        if (n%i == 0) :
            return False 
    return True 

# to check it uncomment the code below
'''
print (Prime(21))
print(Prime(7))
'''

# 3/ Write a Python function to check whether a number is in a given range.
def GivenRange (a,b,n):
    return(n in range(a,b))
# to check it uncomment the code below
'''
print(GivenRange(1,50,30))
print(GivenRange(5,9,1))
'''

# 4/ Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def fact(n): 
    f=1
    for i in range(2,n+1):
        f = f*i 
    return f

# to check it uncomment the code below
'''
print(fact(5))
''' 

# 6/ Write a Python function to sum all the numbers in a list.
def SumList (list):
    sum = 0 
    for element in list : 
        sum = sum+ element
    return sum 

# to check it uncomment the code below 
'''
list = [1,2,3,4]    
print(SumList(list))
'''

# 7/ Write a Python function to find the Max of three numbers.
def Max3 (a,b,c):
    return max(max(a,b),c) 

# to check it uncomment the code below 
'''
print(Max3(55,1,9))
'''



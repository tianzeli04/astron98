#!/usr/bin/env python
# coding: utf-8

# In[76]:


'''1 Power of a Number
Write a function to compute the value of x raised to the power y without
using the built-in pow or ** operator.'''
def power(x, y):
    while y>1: 
        x*=x
        y-=1
    return x
power(2,2)


# In[77]:


'''2 Minimum and Maximum
Write a function that takes a list of numbers as input and returns the mini-
mum and maximum values in the list as a tuple.'''
def extrema(list=[]):
    min=list[0]
    max=list[0]
    for i in range (0, len(list)):
        if list[i]<i-1:
            min=list[i]
        elif list[i]>i-1:
            max=list[i]
        i+=1
    return (min, max)

extrema([1,2,3,4,3,0])


# In[78]:


'''3 Check Leap Year
Write a function that takes a year as input and returns True if it’s a leap
year, and False otherwise. A leap year is divisible by 4 but not divisible by
100 unless it is also divisible by 400.'''

def isLeapYear(x):
    leap=False
    if x%4==0:
        if x%400==0:
            leap=True
        elif x%100!=0:
            leap=True
    return leap

isLeapYear(100)


# In[79]:


'''4 Calculate BMI (Body Mass Index)
Write a function that takes a person’s weight (in kilograms) and height (in
meters) as input and returns their BMI.'''

def CalcBMI(w,h):
    BMI=w/(h**2)
    return BMI

CalcBMI(14,5)


# In[80]:


'''5 Rotating Digits
Implement a function called rotate digits that takes an integer n as input
and rotates its digits to the right by one position. For example, given the
input 12345, the function should return 51234. You may *not* convert the
input to a string but you can use properties of a string in your answer.
Hint: Use modulus (%) and floor division (//).
Ex: 12345 % 10 = 5 and 12345 // 10 = 1234'''
def rotate(x):
    d=0
    a=x%10
    b=x//10
    while x>0:
        x=x//10
        d+=1
    return 10**(d-1)*a+b

rotate(12345)
    


# In[2]:


'''6 Minimum and Maximum but with Loops
For both minimum and maximum, write one function to manually find that
value using a for loop and another to manually find it using a while loop. You
may not use min() or max(). In total you should have written 4 functions.'''
def extremaFor(list=[]):
    min=list[0]
    max=list[0]
    j=1
    for i in range (0, len(list)):
        if list[i]<i-1:
            min=list[i]
        if list[i]>i-1:
            max=list[i]
        i+=1
    return (min, max)

def extremaWhile(list=[]):
    min=list[0]
    max=list[0]
    j=1
    while j<len(list):
        if list[j]>j-1:
            max=list[j]
        if list[j]<j-1:
            min=list[j]
        j+=1
    return (min, max)


extremaWhile([1,2,3,4,3,0])


# In[82]:


'''7 Vowels
Write a function which takes in a string and outputs the number of vowels.
Consider only a,e,i,o,u to be vowels and do not forget about capital letters.
Ex: vowel count(”UC Berkeley”) will return 41'''
def countVowels(str):
    vowels=""
    AEIOU="aeiouAEIOU"
    for i in range(0, len(str)):
        for j in range (0, len(AEIOU)):
            if str[i]==AEIOU[j]:
                vowels+=str[i]
        i+=1
    return len(vowels)

countVowels("UC Berkeley")
            


# In[54]:


'''8 Digital Root
Write a function that takes in an integer and returns the sum of the digits
(the digital root).
Ex: digital root(12345) will return 15'''

def dRoot(x):
    y=0
    while x>0:
        y+=x%10
        x=x//10
    return y
dRoot(12345)


# In[ ]:





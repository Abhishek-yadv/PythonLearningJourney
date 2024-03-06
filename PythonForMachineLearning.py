# ***********************************
import datetime
import time
print("Time in second since the epoch: %s" %time.time())
print("Current date & time: ", datetime.datetime.now())
print("Or like this: ", datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().
strftime("%j"))
print("Day of the month : ", datetime.date.today().
strftime("%d"))
print("Day of week: ", datetime.date.today().
strftime("%A"))


# ****************************************
#arithmetic calculates with date-
#related values, as shown in the following code block:
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c)
c_sec = c.seconds/3600
print(c_sec)
c_total_sec = c.total_seconds()/3600
print(c_total_sec)


# ****************************************
# Converting Strings to Dates
from datetime import datetime
text = '2014-08-13'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z-y
print('Date Diff is: ',diff)
# >>> Date Diff is:  3151 days, 20:18:24.079637


# ****************************************
# Command-Line Arguments
"""
Python provides a getopt module to parse command-line options and
arguments, and the Python sys module provides access to any command-
line arguments via the sys.argv. This serves two purposes:
* ➡ sys.argv is the list of command line arguments
* ➡ len(sys.argv) is the number of command line arguments
"""

# ****************************************
# Nested Loop
max = 5
for x in range(1, max+1):
    for y in range(1, x+1):
        print(y,"", end = "")
    print()

    
# ****************************************
# Split Function
x = 'This is a string that contains abc and Abc'
matchcase = 0
identical = 0
x = x.split(" ")
print(x)
for i in x:
    if i == "abc":
        matchcase = matchcase + 1
    elif i == "Abc":
        identical = identical + 1
if matchcase > 0 :
    print("Found matchcase: ", matchcase)
if identical > 0 :
    print("Found identical: ", identical)
if matchcase == 0 and identical == 0:
    print("No matches found")


# ****************************************
# Using the split() Function to Print Justified Text
import string
wordCount = 0
str1 = 'this is a string with a set of words in it'
print('Left-justified strings:')
print('-----------------------')
for w in str1.split():
    print('%-10s' % w)
    wordCount = wordCount + 1
    if (wordCount % 2 == 0):
        print("")
    print("\n")
    print('Right-justified strings:')
    print('------------------------')
    wordcount = 0
    for w in str1.split():
        print('%10s % w')
        wordcount = wordCount + 1
        if (wordcount % 2 == 0):
            print()

    
# ****************************************
# The join function
#Another way to remove extraneous spaces is to use the join() func-tion, as shown here:
text1 = '  there are extra spaces  '
print('text1:',text1)
text2 = ' '.join(text1.split())
print('text2:',text2)
text2 = 'XYZ'.join(text1.split())
print('text2:',text2)

# ****************************************
# The break/continue/pass statements
print('first loop')
for x in range(1,4):
    if(x == 2):
        break
    print(x)


print('second loop')
for x in range (1,4):
    if(x == 2):
        continue
    print(x)


print('third loop')
for x in range(1, 4):
    if (x == 2):
        pass
    print(x)

# >>> first loop
# >>> 1
# >>> second loop
# >>> 1
# >>> 3
# >>> third loop
# >>> 1
# >>> 2
# >>> 3

# ****************************************
# User-Defined Functions in Python
'''
■ Function blocks begin with the keyword def followed by the function name and parentheses.

●■ Any input arguments should be placed within these parentheses.

●■ The first statement of a function can be an optional statement—the documentation string of the function or docstring.

●■ The code block within every function starts with a colon (:) and is indented.

●■ The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

●■ If a function does not specify return statement, the function automati-cally returns None, which is a special type of value in Python

'''

def func():
    print(3)
func()
# >>>3


def func():
    print(3)
print(func())
# >>>3
# >>> None


# ********************************************
# Specifying Default Values in a Function
def numberFunc(a, b=10):
    print(a, b)
    
def stringFunc(a, b='xyz'):
    print(a, b)
    
def collectionFunc(a, b=None):
    if (b is None):
        print('No value assigned to b')
        
numberFunc(3)
stringFunc('one')
collectionFunc([1, 2, 3])

# >>> (3, 10)
# >>> ('one', 'xyz')
# >>> No value assigned to b


# ********************************************
# Returning Multiple Values from a Function
def MultipleValues():
    return 'a', 'b', 'c'
x, y, z = MultipleValues()
print('x:', x)
print('y:', y)
print('z:', z)

# ********************************************
# Functions with a Variable Number of Arguments
def sum(a, b):
    return a + b
values = (1, 2)
s1 = sum(*values)
print('s1 = ', s1)


def sum(*values):
    sum = 0
    for x in values:
        sum = sum + x
    return sum
values1 = (1, 2)
s1 = sum(*values1)
print('s1 = ', s1)

values2 = (1, 2, 3, 4)
s2 = sum(*values2)
print('s2 = ', s2)


# ********************************************
# Lambda Expressions
add = lambda x, y: x + y
x1 = add(5,7)
x2 = add('Hello', 'Python')
print(x1)
print(x2)
# >>> 12
# >>> Hello Python

# ********************************************
# Recursion
def factorial(num):
    if(num > 1):
        return num* factorial(num - 1)
    else:
        return 1
result = factorial(5)
print('The factorial of 5 =', result)
# >>> The factorial of 5 = 120


def factorial2(num):
    prod = 1
    for x in range(1, num+1):
        prod = prod * x
    return prod
result = factorial2(5)
print('The factorial of 5=', result)


def fib(num):
    if (num == 0):
        return 1
    elif (num == 1):
        return 1
    else:
        return fib(num-1) + fib(num-2)
result = fib(10)
print('Fibonacci value of 10 =', result)


# ********************************************
# Calculating the GCD of Two Numbers
""" The greatest common divisor (GCD) of two positive integers is the largest
    integer that divides both integers with a remainder of 0 """

def gcd(num1, num2):
    if (num1 % num2 == 0):
        return num2
    elif (num1 < num2):
        print("switching ", num1, " and ", num2)
        return gcd(num2, num1)
    else:
        print("reducing", num1, " and ", num2)
        return gcd(num1-num2, num2)
result = gcd(24, 10)
print("GCD of", 24, "and", 10, "=", result)


# ********************************************
# Calculating the LCM of Two Numbers
"""
The lowest common multiple (LCM) of two positive integers is the smallest integer that is a multiple of those two integers. Some values are shown here:
lcm(6,2) = 2
lcm(10,4) = 20
lcm(24,16) = 48



In general, if x and y are two positive integers, you can calculate their
LCM as follows:
lcm(x,y) = x/gcd(x,y)*y/gcd(x,y)
"""


def gcd(num1, num2):
    if (num1 % num2 == 0):
        return num2
    elif (num1 < num2):
        # print("switching ", num1, " and ", num2)
        return gcd(num2, num1)
    else:
        # print("reducing", num1, " and ", num2)
        return gcd(num1-num2, num2)
def lcm(num1, num2):
    gcd1 = gcd(num1, num2)
    lcm1 = num1*num2/gcd1
    return lcm1
result = lcm(24, 10)
print("The LCM of", 24, "and", 10, "=", result)



#########################################
######################################
###################### Chapter 3
# Working with Lists
point = [7, 8]
x,y = point
print(x)
print(y)
# >>> 7
# >>> 8

line = ['a', 10, 20, (2020, 10, 31)]
x1, x2, x3, date1 = line
print(x1)
print(x2)
print(x3)
print(date1)
# >>> a
# >>> 10
# >>> 20
# >>> (2020, 10, 31)

# Note : number and/or structure of the variables must have match the data, otherwise will give error

line = ['a', 10, 20, (2020, 10, 31)]
x1, x2, x3, (year,month, day) = line
print(x1)
print(x2)
print(x3)
print(year)
print(month)
print(day)
# >>> a
# >>> 10
# >>> 20
# >>> 2020
# >>> 10
# >>> 31


#***********************************
# Reversing and Sorting a List

a = [4, 1, 2, 3]
a.reverse()
print(a)
# >>> [3, 2, 1, 4]

# OR
a = [4, 1, 2, 3]
print(a[::-1])

# The Python sort() method sorts a list:
a = [4, 1, 2, 3]
a.sort()
print(a)
# >>> [1, 2, 3, 4]


# ***********************************
# uppercase and lowercase
list1 = ['a', 'list', 'of', 'words']
list2 = [s.upper() for s in list1]
list3 = [s for s in list1 if len(s) <=2]
list4 = [s for s in list1 if 'w' in s]
print("list1",list1)
print("list2",list2)
print("list3",list3)
print("list4",list4)

# >>> list1['a', 'list', 'of', 'words']
# >>> list2['A', 'LIST', 'OF', 'WORDS']
# >>> list3['a', 'of']
# >>> list4['words']


# ***********************************
# Lists and Arithmetic Operations
x = [3, 1, 2, 4]
maxList = x.sort()
minList = x.sort(x.reverse())
min1 = min(x)
max1 = max(x)
print(min1)
print(max1)
minList = x.sort(reverse=True)
sorted(x, reverse=True)


# *************************************
# Lists and Filter-Related Operations
mylist = [1, -2, 3, -5, 6, -7, 8]
pos = [n for n in mylist if n > 0]
neg = [n for n in mylist if n < 0]

print(pos)
print(neg)
# >>> [1, 3, 6, 8]
# >>> [-2, -5, -7]

# You can also specify if/else logic in a filter, as shown here:
mylist = [1, -2, 3, -5, 6, -7, 8]
negative_list = [n if n < 0 else 0 for n in mylist]
postive_list = [n if n > 0 else 0 for n in mylist]
print(postive_list)
print(negative_list)
# >>>[1, 0, 3, 0, 6, 0, 8]
# >>>[0, -2, 0, -5, 0, -7, 0]

# ***************************************
# Sorting Lists of Numbers and Strings
"""
Note:-
that if you sort a list of character strings the output is case sen-
sitive, and that uppercase letters appear before lowercase letters. This is
due to the fact that the collating sequence for ASCII places uppercase let-
ter(decimal 65 through decimal 91) before lowercase letters
(decimal 97 through decimal 127) 
"""
list1 = ['a', 'A', 'b', 'B', 'Z']
print(sorted(list1))
# >>> ['A', 'B', 'Z', 'a', 'b']

""" You can specify str.lower if you want treat uppercase letters as though
they are lowercase letters during the sorting operation, as shown here: """
list1 = ['a', 'A', 'b', 'B', 'Z']
print(sorted(list1, key=str.lower))
['a', 'AA', 'bbb', 'BBBBB', 'ZZZZZZZ']

# Note :-You can also specify the reverse option so that the list is sorted in re-verse order:
list1 = ['a', 'A', 'b', 'B', 'Z']
print(sorted(list1, reverse = True))
# >>> ['b', 'a', 'Z', 'B', 'A']


#Note:- You can even sort a list based on the length of the items in the list:
list1 = ['a', 'AA', 'bbb', 'BBBBB', 'ZZZZZZZ']
print(sorted(list1, key = len))
# >>> ['a', 'AA', 'bbb', 'BBBBB', 'ZZZZZZZ']



# ***************************************************
# Counting Digits, Uppercase, and Lowercase Letters
str = "abc4234AFde"
digi_count = 0
alpha_count = 0
lower_count = 0
uper_count = 0
for i in range(0, len(str)):
    char = str[i]
    if char.isdigit():
        # print("this is a digit:", char)
        digi_count = digi_count + 1
    elif char.isalpha():
        # print("this is a alphabetic:", char)
        if char == char.lower():
            lower_count = lower_count + 1
        else:
            uper_count = uper_count + 1
print('Original String: ', str)
print('Number of digits: ', digi_count)
print('Total alphanumeric:', alpha_count)
print('Upper Case Count: ', uper_count)
print('Lower Case Count: ', lower_count)

# >>> Original String:  abc4234AFde
# >>> Number of digits:  4
# >>> Total alphanumeric: 0
# >>> Upper Case Count:  2
# >>> Lower Case Count:  5 



# *********************************************
# Iterating through Pairs of Lists
list1 = [1,2,3]
list = [3*x for x in list1]
print(list)
# >>> [3, 6, 9]


# Create a new list with pairs of elements consisting of the original ele-ment and the original element multiplied by 3
list1 = [1, 2, 3]
list2 = [[x, x*3] for x in list1]
print(list2)
# >>> [[1, 3], [2, 6], [3, 9]]


# Compute the product of every pair of numbers from two lists:
list1 = [1,2,3]
list2 = [5,6,7]
list = [a*b for a in list1 for b in list2]
print(list)
# >>> [5, 6, 7, 10, 12, 14, 15, 18, 21]

# Calculate the sum of every pair of numbers from two lists:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list = [a+b for a in list1 for b in list2]
print(list)
# >>> [6, 7, 8, 7, 8, 9, 8, 9, 10]

# Calculate the pair-wise product of two lists:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list = [list1[i]*list2[i] for i in range(len(list1))]
# >>> [8, 12, -54]


# Other List related Functions (append(), insert(), delete(), pop(), and extend())

# Note:- Define a Python list (notice that duplicates are allowed):
a = [1, 2, 3, 2, 4, 2, 5]
print(a.count(1), a.count(2))
# >>> 1 3


# Insert -8 in position 3:
a = [1, 2, 3, 2, 4, 2, 5]
a.insert(3, -8)
print(a)
# >>> [1, 2, 3, -8, 2, 4, 2, 5]

# Remove occurrences of 3
a = [1, 2, 3, 2, 4, 2, 5]
a.remove(3)
print(a)

a.remove(2)
print(a)

# Remove occurrences of 1:
a = [1, 2, 3, 2, 4, 2, 5]
a.remove(1)
print(a)
# >>> [2, 3, 2, 4, 2, 5]?

# Append 19 to the list:
a = [1, 2, 3, 2, 4, 2, 5]
a.append(1)
print(a)
# >>> [1, 2, 3, 2, 4, 2, 5, 1]

# Print the index of 19 in the list:
a = [2, -8, 2, 4, 2, 5, 19]
b = a.index(19)
print(b)
# >>> 6

# Reverse the list:
a = [2, -8, 2, 4, 2, 5, 19]
a.reverse()
print(a)
# >>> [19, 5, 2, 4, 2, -8, 2]

# Sort the list:
a = [2, -8, 2, 4, 2, 5, 19]
a.sort()
print(a)
# >>> [-8, 2, 2, 2, 4, 5, 19]

# Extend list a with list b:
a = [2, -8, 2, 4, 2, 5, 19]
b = [100,200,300]
a.extend(b)
print(a)
# >>> [2, -8, 2, 4, 2, 5, 19, 100, 200, 300]


# Remove the first occurrence of 2:
a = [2, -8, 2, 4, 2, 5, 19]
a.pop(2)
print(a)
# >>> [2, -8, 4, 2, 5, 19]

# Remove the last item of the list:
a = [2, -8, 2, 4, 2, 5, 19]
a.pop()
print(a)
# >>> [2, -8, 2, 4, 2, 5]





# ****************************************
# Working with Vectors (A vector is a one-dimensional array of values, and you can performvector-based operations, such as addition, subtraction, and inner product.)
v1 = [1,2,3]
v2 = [1,2,3]
v3 = [5,5,5]

s1 = [0, 0, 0]
d1 = [0, 0, 0]
p1 = 0

print("Initial Vectors")
print('v1:',v1)
print('v2:',v2)
print('v3:',v3)

for i in range(len(v1)):
    d1[i] = v3[i] - v2[i]
    s1[i] = v3[i] + v2[i]
    p1 = v3[i] * v2[i] + p1
    
print("After operations")
print('d1:', d1)
print('s1:', s1)
print('p1:', p1)


# **********************************
# Working with Matrices
mm = [["a","b","c"],["d","e","f"],["g","h","i"]];
print('mm: ', mm)
print('mm[0]: ', mm[0])
print('mm[0][1]:', mm[0][1])
# >>> mm:  [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# >>> mm[0]:  ['a', 'b', 'c'] 
# >>> mm[0][1]: b

# ******************************************
# The NumPy Library for Matrices
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
# >>> [[ 1 -2  3] 
# >>> [ 0  4  5] 
# >>> [ 7  8 -9]]


# The next snippet returns the transpose of matrix m:
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m.T)
# >>> [[ 1  0  7] 
# >>>  [-2  4  8] 
# >>>  [ 3  5 -9]]

# The next snippet returns the inverse of matrix m (if it exists):
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m.I)
# >>> [[ 0.33043478 -0.02608696  0.09565217]  
# >>>  [-0.15217391  0.13043478  0.02173913] 
# >>>  [ 0.12173913  0.09565217 -0.0173913 ]]

# >>> The next snippet defines a vector y and then computes the product m*v:
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
v = np.matrix([[2], [3], [4]])
print(v)
# >>> matrix([[2], [3], [4]])
print(m*v)
# >>> matrix([[ 8],[32],[ 2]])


# >>>The next snippet imports the numpy.linalg subpackage and then computes the determinant of the matrix m:
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
import numpy.linalg
print(numpy.linalg.det(m))
# >>> -229.99999999999983


# >>> The next snippet finds the eigenvalues of the matrix m:
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
numpy.linalg.eigvals(m)
# >>> array([-13.11474312, 2.75956154, 6.35518158])

# >>> The next snippet finds solutions to the equation m*x = v:
import numpy as np
x = numpy.linalg.solve(m, v)
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)


# ***********************************************
#############################################
# (Sets)
"""
A Python set in Python is an unordered collection that does not contain duplicate elements.
Use curly braces or the set() function to create sets. Set objects support set-theoretic operations
such as union, intersection, and difference.
"""
# Note: set() is required in order to create an empty set because {} creates an empty dictionary.

# Create a list of elements:
l = ['a', 'b', 'a', 'c']

# Create a set from the preceding list:
l = ['a', 'b', 'a', 'c']
s = set(l)
print(s)
# >>> {'c', 'b', 'a'}

# Test if an element is in the set:
l = ['a', 'b', 'a', 'c']
s = set(l)
if 'a' in s:
    print('True')
else:
    print('False')
# >>> True

# Create a set from a string:
n = set('abacad')
print(n)
# >>> {'b', 'd', 'c', 'a'}

# >>> Subtract n from s:
l = ['a', 'b', 'a', 'c']
s = set(l)
n = set('abacad')
print(s-n)
# >>> set()

# Subtract s from n:
l = ['a', 'b', 'a', 'c']
s = set(l)
n = set('abacad')
print(n-s)
# >>> {'d'}

# The union of s and n:
l = ['a', 'b', 'a', 'c']
s = set(l)
n = set('abacad')
print(s|n)
# >>> {'d', 'b', 'c', 'a'}

# The intersection of s and n:
l = ['a', 'b', 'a', 'c']
s = set(l)
n = set('abacad')
print(s & n)
# >>> {'b', 'a', 'c'}

# >>> The exclusive-or of s and n:
l = ['a', 'b', 'a', 'c']
s = set(l)
n = set('abacad')
print(s^n)
# >>> {'d'}

# ***********************************************
#############################################
# Dictionaries
dict1 = {'key1':'value1', 'key2':'value2'}

# The "empty dict" is just an empty pair of curly braces {}


# Creating a Dictionary
dict1 = {}
dict1 = {'x' : 1, 'y' : 2}


#Displaying the Contents of a Dictionary
dict1 = {'x':1,'y':2}
print(dict1)
print(dict1['x'])
print(dict1['y'])

# Key/value bindings for a dict and a set are not necessarily stored in the same order that you defined them.

# Python dictionaries also provide the get method in order to retrieve key values:
dict1 = {'x': 1, 'y': 2}
print(dict1.get('x'))
print(dict1.get('y'))
print(dict1.get('z'))

# >>> 1
# >>> 2
# >>> None

# You can also use dict comprehensions to create dictionaries from ex-pressions, as shown here:
dict = {x:x**3 for x in (3,6,2)}
print(dict)
# >>> {3: 27, 6: 216, 2: 8}

# ***********************************************
# Checking for Keys in a Dictionary
dict1 = {'x': 1, 'y': 2}
print('x' in dict1)
# >>> True

# ***********************************************
# Deleting Keys from a Dictionary
MyDict = {'x' : 5, 'y' : 7}
MyDict['z'] = 13
print(MyDict)
# >>> {'x': 5, 'y': 7, 'z': 13}


MyDict = {'x': 5, 'y': 7}
del MyDict['x']
print(MyDict)
# >>> {'y': 7}


MyDict = {'x' : 5, 'y' : 7}
MyDict.keys()
print(MyDict.keys())
# >>> dict_keys(['x', 'y'])


MyDict = {'x' : 5, 'y' : 7}
MyDict.values()
print(MyDict.values())
# >>> dict_values([5, 7])


# ***********************************************
# >>> Iterating through a Dictionary
MyDict = {'x' : 5, 'y' : 7, 'z' : 13}
for key, value in MyDict.items():
    print(key,value)
# >>> x 5
# >>> y 7
# >>> z 13

# ***********************************************
# >>> Interpolating Data from a Dictionary
# The % operator substitutes values from a Python dictionary into a string by name.

hash = {}
hash['Beverage'] = 'coffe'
hash['count'] = 3
print(hash)
# >>> {'Beverage': 'coffe', 'count': 3}

# ***********************************************
# Dictionary Formatting
h = {}
h['apple'] = 4
h['mango'] = 6
h['banana'] = 9
print(h)
# >>> {'apple': 4, 'mango': 6, 'banana': 9}


# Other Sequence Types in Python
# Python supports 7 sequence types: str, unicode, list, tuple, bytearray, buffer, and xrange

# ***********************************************
##################################################
# INTRODUCTION TO NUMPY AND PANDAS
# Numpy :- 
"""
NumPy is a Python module that provides many convenience methods and also better performance. NumPy provides a core library for scientific computing in Python, with performant multidimensional arrays and good
vectorized math functions, along with support for linear algebra and random numbers.

NumPy is modeled after MatLab, with support for lists, arrays, and so forth.
NumPy is easier to use than Matlab, and it’s very common in Ten-sorFlow code as well as Python code

"""

# Useful numpy features

"""
* NumPy arrays have a fixed size, whereas Python lists can expand dynamically. Whenever you modify the size of an ndarray, a new array is created and the original array is deleted.

* NumPy arrays are homogeneous, which means that the elements in a NumPy array must all have the same data type. Except for NumPy arrays of objects, the elements in NumPy arrays of any other data type must have the same size in memory.

An array is a set of consecutive memory locations used to store data. Each item in the array is called an element.
The number of elements in an array is called the dimension of the array. A typical array declaration is
shown here:
arr1 = np.array([1,2,3,4,5])
"""

import numpy as np
list1 = [1,2,3,4,5]
print(list1)
# >>> [1, 2, 3, 4, 5]

import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
# >>> [1 2 3 4 5]

# ***********************************************
# Working with Loops
# displays the contents of loop1.py that illustrates how to iterate through the elements of a NumPy array and a Python list.

import numpy as np
list = [1,2,3]
arr1 = np.array([1,2,3])
for i in list:
    print(i)
for e in arr1:
    print(e)
    
# ***********************************************
# Appending Elements to Arrays
import numpy as np
arr1 = np.array([1,2,3])
# these method do not work
# arr1.append(4)
# arr1 = arr1 + [5]
arr1 = np.append(arr1,4)
arr1 = np.append(arr1,[5])

for e in arr1:
    print(e)
    
arr2 = arr1 + arr1
for e in arr2:
    print(e)

# ***********************************************
# Appending Elements to Arrays
import numpy  as np
arr1 = np.array([1,2,3])
arr1 = np.append(arr1,4)
for e in arr1:
    print(e)
    
arr1 = np.array([1,2,3])
arr1 = np. append(arr1, 4)
arr2 = arr1 + arr1
for e in arr2:
    print(e)

# >>> 1 2 3 4 2 4 6 8

# ***********************************************
# Multiply Lists and Arrays
import numpy as np
list1 = [1,2,3]
arr1 = np.array([1,2,3])
print('list: ',list1)
print('arr1: ',arr1)
print('2*list:',2*list1)
print('2*arr1:',2*arr1)
# >>> list:  [1, 2, 3]
# >>> arr1:  [1 2 3]  
# >>> 2*list: [1, 2, 3, 1, 2, 3]
# >>> 2*arr1: [2 4 6]

# ***********************************************
# Doubling the Elements in a List
import numpy as np 
list1 = [1,2,3]
list2 = []
for e in list1:
    list2.append(e*2)
    
print('list1', list1)
print('list2', list2)
# >>> list1 [1, 2, 3]
# >>> list2 [2, 4, 6]

# ***********************************************
# Lists and Exponents
import numpy as np
list1 = [1,2,3]
list2 = []

for e in list1:
    list2.append(e**2)

print(list1)
print(list2)

# ***********************************************
# Arrays and Exponents
import numpy as np
arr1 = np.array([1,2,3])
arr2 = arr1**2
arr3 = arr1**3
print("arr1", arr1)
print("arr2", arr2)
print("arr3", arr3)
# >>> arr1 [1 2 3]   
# >>> arr2 [1 4 9]   
# >>> arr3 [ 1  8 27]

# ***********************************************
# Math Operations and Arrays
import numpy as np
arr1 = np.array([1,2,3])
sqrt = np.sqrt(arr1)
log1 = np.log(arr1)
exp1 = np.exp(arr1)
print(sqrt)
print(log1)
print(exp1)

# >>> [1.         1.41421356  1.73205081]
# >>> [0.         0.69314718  1.09861229]   
# >>> [2.71828183 7.3890561  20.08553692]

# ***********************************************
# Working with “-1” Subranges with Vectors
import numpy as np
arr1 = np.array([1,2,3,4,5])
import numpy as np
# -1 => "all except the last element in ..." (row or col)
arr1 = np.array([1,2,3,4,5])
print('arr1:',arr1)
print('arr1[0:-1]:',arr1[0:-1])
print('arr1[1:-1]:',arr1[1:-1])
print('arr1[::-1]:', arr1[::-1]) # reverse!
# >>> arr1: [1 2 3 4 5]      
# >>> arr1[0:_1]: [1 2 3 4]  
# >>> arr1[1:_1]: [2 3 4]    
# >>> arr1[::_1]: [5 4 3 2 1]

# ***********************************************
# Working with “-1” Subranges with Arrays
import numpy as np
# -1 => "the last element in ..." (row or col
arr1 = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print('arr1:', arr1)
print('arr1[-1,:]:', arr1[-1,:])
print('arr1[:,-1]:', arr1[:,-1])
print('arr1[-1:,-1]:',arr1[-1:,-1])
# >>> arr1: [[ 1  2  3]        
# >>>  [ 4  5  6]
# >>>  [ 7  8  9]
# >>>  [10 11 12]]
# >>> arr1[-1,:]: [10 11 12]   
# >>> arr1[:,-1]: [ 3  6  9 12]
# >>> arr1[-1:,-1]: [12]


list = [1,2,3,4,5]
print(list[:])

# ***********************************************
# Other Useful NumPy Methods
"""
* ➡ The method np.zeros() initializes an array with 0 values.
* ●➡ The method np.ones() initializes an array with 1 values.
* ●➡ The method np.empty()initializes an array with 0 values.
* ●➡ The method np.arange() provides a range of numbers:
* ●➡ The method np.shape() displays the shape of an object:
* ●➡ The method np.reshape() <= very useful!
* ●➡ The method np.linspace() <= useful in regression
* ●➡ The method np.mean() computes the mean of a set of numbers:
* ●➡ The method np.std() computes the standard deviation of a set of numbers:
"""

# **********************************************
# Arrays and Vector Operations
import numpy as np
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print('a: ', a)
print('b: ', b)
print('a + b: ', a+b)
print('a _ b: ', a-b)
print('a * b: ', a*b)
print('a / b: ', a/b)
print('b / a: ', b/a)
print('a.dot(b):',a.dot(b))


# **************************************
# NumPy and Dot Products (1)
import numpy as np
a = np.array([1,2])
b = np.array([2,3])

dot2 = 0
for e, f in zip(a,b):
    dot2 = e*f + dot2
print('a: ',a)
print('b: ',b)
print('a*b: ',a*b)
print('dot1:',a.dot(b))
print('dot2:',dot2)
# >>> a:  [1 2]  
# >>> b:  [2 3]  
# >>> a*b:  [2 6]
# >>> dot1: 8    
# >>> dot2: 8 

# **************************************
# NumPy and Dot Products (2)
import numpy as np
a = np.array([1,2])
b = np.array([2,3])
print('a: ',a)
print('b: ',b)
print('a.dot(b): ',a.dot(b))
print('b.dot(a): ',b.dot(a))
print('np.dot(a,b):',np.dot(a,b))
print('np.dot(b,a):',np.dot(b,a))
# >>> a:  [1 2]     
# >>> b:  [2 3]     
# >>> a.dot(b):  8  
# >>> b.dot(a):  8  
# >>> np.dot(a,b): 8
# >>> np.dot(b,a): 8


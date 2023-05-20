###############################################
##################################### List
# List ordered, mutable, allow duplicate elements
mylist = ['banana', "cherry", "apple"]
print(mylist)


# **********************************
mylist1 = [5,True, "apple", "apple"]
print(mylist1)

###
mylist = ['banana', "cherry", "apple"]
item = mylist[0]
item = mylist[-1] # this refer last item
print(item)

# ********************************** iterateable
mylist = ['banana', "cherry", "apple"]
for i in mylist:
    print(i)
    
# **********************************
mylist = ['banana', "cherry", "apple"]
if "apple" in mylist:
    print("yes")
else:
    print("no")
    
# **********************************
mylist = ['banana', "cherry", "apple"]
print(len(mylist))

# **********************************
mylist = ['banana', "cherry", "apple"]
mylist.append("lemon")
print(mylist)
mylist.insert(1, "blueberry")
print(mylist)
mylist.pop()
print(mylist)
mylist.remove("cherry")
print(mylist)
mylist.reverse()
print(mylist)
mylist.clear()
print(mylist)

# **********************************    Noteble point between sort and sorted
mylist = [4, 3, 1, -1, -5, -10]
newlist = sorted(mylist) #sorted method doesn't change orignal list
print(newlist)
print(mylist)
# >>> [-10, -5, -1, 1, 3, 4]
# >>> [4, 3, 1, -1, -5, -10]

# *****************************
mylist = [4, 3, 1, -1, -5, -10]
mylist.sort()
print(mylist)
print(mylist)
# >>> [-10, -5, -1, 1, 3, 4]
# >>> [-10, -5, -1, 1, 3, 4]


# ***********************************
mylist = ["Abhishek"] * 5
print(mylist)
mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2
print(new_list)

# ***********************************
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]
print(a)
# >>> [2, 3, 4, 5]

a = mylist[:5]
print(a)
# >>>[1, 2, 3, 4, 5]

a = mylist[5:]
print(a)
# >>>[6, 7, 8, 9]

a = mylist[::1] #with step 1
print(a)
# >>>[1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist[::2] #with step 2 every second items
print(a)
# >>>[1, 3, 5, 7, 9]

a = mylist[::-1] #reverse list
print(a)
# >>>[9, 8, 7, 6, 5, 4, 3, 2, 1]

############################## Copying list
##########################
list_org = ["banana","cherry","apple"]
list_copy = list_org # both list same refer in the memory
list_copy.append("lemon")
print(list_copy)
print(list_org)
# >>>['banana', 'cherry', 'apple', 'lemon']
# >>>['banana', 'cherry', 'apple', 'lemon']

# **************************************
### if you want make actual copy of list you can do with copy method
list_org = ["banana", "cherry", "apple"]
list_copy = list_org.copy()
list_copy.append("lemon")
print(list_copy)
print(list_org)
# >>> ['banana', 'cherry', 'apple', 'lemon']
# >>> ['banana', 'cherry', 'apple']

# ******* OR
list_org = ["banana", "cherry", "apple"]
list_copy = list(list_org) #this also makes origanal copy
list_copy.append("lemon")
print(list_copy)
print(list_org)
# >>> ['banana', 'cherry', 'apple', 'lemon']
# >>> ['banana', 'cherry', 'apple']

# ******* OR
list_org = ["banana", "cherry", "apple"]
list_copy = list_org[:] # this also makes origanal copy
list_copy.append("lemon")
print(list_copy)
print(list_org)

# ******* OR
mylist = [1,2,3,4,5,6]
b = [i*i for i in mylist]
#  it's not necessary to put i you can also put x here
# b = [x*x for i in mylist]
print(mylist)
print(b)
# >>> [1, 2, 3, 4, 5, 6]
# >>> [1, 4, 9, 16, 25, 36]


#########################################
####################################
########################### Tuple
# Tubled: ordered, Unmutable,allows duplicat elements
# it can't be changes after cretion
mytuple = ("max", 28, "Boston")
print(mytuple)
print(type(mytuple))
# >>> ('max', 28, 'Boston')
# >>> <class 'tuple'>

# ***********************************
mytuple = ("max")
print(mytuple)
print(type(mytuple))
# >>> max
# >>> <class 'str'>

# ***********************************
mytuple = tuple(["max", 28, "boston"])
print(mytuple)

item = mytuple[0]
print(item)
# >>> max

item = mytuple[-1]
print(item)
# >>> boston


# ***********************************
# tuple does not suppert item assignment
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)
mytuple[0] = "Tim"
# >>>TypeError: 'tuple' object does not support item assignment


# ***********************************
# check item in tuple or not
mytuple = tuple(["Max", 28, "Boston"])
if "Tim" in mytuple:
    print("yes")
else:
    print("no")
# >>> no

# ***********************************
# check item in tuple or not
mytuple = tuple(["Max", 28, "Boston"])
if "Max" in mytuple:
    print("yes")
else:
    print("no")
# >>> yes

# ***********************************
# find number of items in tuple
my_tuple = ('a', 'p','p','l','e')
print(len(my_tuple))

# Count the number of elements inside 
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))
# >>> 2

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('o'))
# >>> 0

# We can also find index of some especific element
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.index('l'))
# >>> 3

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.index('l'))
# >>> 3

# We can also convert tuple in list or interchangibly
my_tuple = ('a', 'p', 'p', 'l', 'e')
my_list = list(my_tuple)
print(my_list)
# >>> ['a', 'p', 'p', 'l', 'e']

my_list = ['a', 'p', 'p', 'l', 'e']
my_tuple2 = tuple(my_list)
print(my_tuple2)
# >>> ('a', 'p', 'p', 'l', 'e')

# ***********************************
# SLICING WITH TOUPLE
a = (1,2,3,4,5,6,7,8,9)
b = a[2:5]
print(b)
# >>>(3, 4, 5)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[2::]
print(b)
# >>>(3, 4, 5, 6, 7, 8, 9)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[::1]
print(b)
# >>>(1, 2, 3, 4, 5, 6, 7, 8, 9)


my_tuple = ("Max", 28, "Boston")
name,age = my_tuple
print(name)
print(age)
print(city)
# >>> too many values to unpack (expected 2)

# ************************************* We can unpacked multiple element with the help of "*"
my_tuple = (0,1,2,3,4)
i1, *i2,i3 = my_tuple
print(i1)
print(i3)
print(i2)
# 0
# >>> 4
# >>> [1, 2, 3]

# ******************************** Create a list and tuple with same elemnts and then we used to get size of element list  Return the number of bytes
import sys
my_list = [0,1,2, "hello", True]
my_tuple = (0,1,2,"hello",True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
# >>> 104 bytes
# >>> 80 bytes

# ******************************** in timeit module
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number = 1000000))
# >>> 0.05566509999334812
# >>> 0.017760899965651333


######################################################
#################################################
############################### Dictionaries
# Dictionaries is collection data type that is unorder and mutable, it consist collection of key value pairs so each key value pair maps to key its associate value

mydict = {"name":"Max","age":28, "city":"new york"} #braces
print(mydict)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}


mydict2 = dict(name = "mary", age = 27,city = "Boston")
print(mydict2)
# Note here don't need to add double quotes
# >>> {'name': 'mary', 'age': 27, 'city': 'Boston'}


mydict = {"name": "Max", "age": 28, "city": "new york"}
value = mydict["name"]
print(value)
# >>> Max


mydict = {"name": "Max", "age": 28, "city": "new york"}
value = mydict["age"]
print(value)
# >>> 28


mydict = {"name": "Max", "age": 28, "city": "new york"}
value = mydict["lastname"]
print(value)
# >>> KeyError


mydict = {"name": "Max", "age": 28, "city": "new york"}
print(mydict)
mydict["email"] = "max@xyz.com"
print(mydict)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}
# >>> {'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'max@xyz.com'}


mydict = {'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'max@xyz.com'}
mydict["email"] = "coolmax@xyz.com"
print(mydict)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'coolmax@xyz.com'}

# ************************************* Delete items in dict
mydict = {'name': 'Max', 'age': 28,
        'city': 'new york', 'email': 'coolmax@xyz.com'}
del mydict["name"]
print(mydict)
# >>>{'age': 28, 'city': 'new york', 'email': 'coolmax@xyz.com'}


# ************************************* Remove specific items
mydict = {'name': 'Max', 'age': 28,
    'city': 'new york', 'email': 'coolmax@xyz.com'}
print(mydict)
mydict.pop("age")
print(mydict)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'coolmax@xyz.com'}
# >>> {'name': 'Max', 'city': 'new york', 'email': 'coolmax@xyz.com'}

# ************************************* Remove arbitary items
mydict = {'name': 'Max', 'city': 'new york', 'email': 'coolmax@xyz.com'}
print(mydict)
mydict.popitem()
print(mydict)
# >>> {'name': 'Max', 'city': 'new york', 'email': 'coolmax@xyz.com'}
# >>> {'name': 'Max', 'city': 'new york'}


mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
if "name" in mydict:
    print(mydict["name"])
# >>> Max

mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
if "lastname" in mydict:
    print(mydict["lastname"])
# >>>

mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
try:
    print(mydict["name"])
except:
    print("Error")
# >>> max

mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
try:
    print(mydict["lastname"])
except:
    print("Error")
# >>> Error


# ********************************************
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
for key in mydict:
    print(key)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}
# >>> name
# >>> age
# >>> city


# ********************************************
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
for key in mydict.keys():
    print(key)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}
# >>> name
# >>> age
# >>> city


# ********************************************
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
for value in mydict.values():
    print(value)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}
# >>> Max
# >>> 28
# >>> new york


# ********************************************
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
for key, value in mydict.items():
    print(key,value)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}
# >>> name Max
# >>> age 28
# >>> city new york


# *********************************************
########### If keys already exist its value got overwritten
## In this orignal one changed
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
mydict_cpy = mydict
mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)
# >>> {'name': 'Max', 'age': 28, 'city': 'new york'}
# >>> {'name': 'Max', 'age': 28, 'city': 'new york','email': 'max@xyz.com'}
# >>> {'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'max@xyz.com'}


# ********************************************
############# copying by using builtin function
#### In this method orignal one did not change
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
mydict_cpy = mydict.copy()
mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)
# >>>{'name': 'Max', 'age': 28, 'city': 'new york'}
# >>>{'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'max@xyz.com'}
# >>>{'name': 'Max', 'age': 28, 'city': 'new york'} Orignal one did not change


# ********************************************
############ even in this method orignal one did not changed
mydict = {'name': 'Max', 'age': 28, 'city': 'new york'}
print(mydict)
mydict_cpy = dict(mydict)
mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

# >>>{'name': 'Max', 'age': 28, 'city': 'new york'}
# >>>{'name': 'Max', 'age': 28, 'city': 'new york', 'email': 'max@xyz.com'}
# >>>{'name': 'Max', 'age': 28, 'city': 'new york'}

# ********************************************
########################### UPDATE METHOD
my_dict = {"name":"max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name = "Mary", age = 27, city = "Boston")

my_dict.update(my_dict_2)
print(my_dict)
# >>>{'name': 'Mary', 'age': 27, 'email': 'max@xyz.com', 'city': 'Boston'}


my_dict = {3:9, 6:36, 9:81}
print(my_dict)
value = my_dict[3]
print(value)
# >>>{3: 9, 6: 36, 9: 81}
# >>>9

# *******************************************
########### we can also Use tuple As a key
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)
# >>> {3: 9, 6: 36, 9: 81}
# >>> {(8, 7): 15}

# *******************************************
# we can't use list as tuple bcz it's mutable (Unhashble type)
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
mytuple = [8, 7]
mydict = {mytuple: 15}
print(mydict)
# >>> Traceback(most recent call last):
# >>>   File "c:\VsCode\py4e\tempCodeRunnerFile.py", line 4, in <module >
# >>>   mydict = {mytuple: 15}
# >>> TypeError: unhashable type: 'list'



################################################
#########################################
################################# SETS

# ************************************
# Set is collection data type that is unorder, mutable, no duplicate value
myset = {1,2,3}
print(myset)
# >>> {1, 2, 3}


myset = {1, 2, 3,3,2,1}
print(myset)
# >>> {1, 2, 3}

myset = set("hello")
print(myset)
# >>> {'e', 'h', 'o', 'l'}

# *************************************
myset = {}
print(type(myset))
# >>> <class 'dict'>

myset = set()
print(type(myset))
# >>> <class 'set'>

# ***********************************
# Set is mutable
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# ************************************
## We can also remove elements with remove method
myset = {1,2,3,4,5}
myset.remove(3)
print(myset)
# >>> {1, 2, 4, 5}

myset = {1, 2, 3, 4,5}
myset.remove(7)
print(myset)
# >>> KeyError: 7 # For this we can use discard method


# ******************************************
### We can use discard method to avoid error
myset = {1, 2, 3, 4, 5}
myset.discard(3)
print(myset)
# >>> {1, 2, 4, 5}

myset = {1, 2, 3, 4,5}
myset.discard(7)
print(myset)
# >>> {1, 2, 3, 4, 5}


myset = {1, 2, 3, 4, 5}
myset.clear()
print(myset)
# >>> set()

myset = {1, 2, 3, 4, 5}
print(myset.pop())
print(myset)
# >>> 1
# >>> {2, 3, 4, 5}

# *******************************************
# iterate each element in set
myset = {1, 2, 3}
for i in myset:
    print(i)
# >>> 1
# >>> 2
# >>> 3

myset = {1, 2, 3}
if 1 in myset:
    print("yes")
# >>> yes

myset = {1, 2, 3}
if 4 in myset:
    print("yes")
# >>> 


# ***********************************
################# UNION, INTERSECTION
odds = {1,3,5,7,9}
even = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(even)
print(u)
# >>> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

i = odds.intersection(even)
print(i)
# >>> set()


odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

i = odds.intersection(primes)
print(i)
# >>> {3, 5, 7}


# ********************************************
## Diffrence in sets
# All element in 1st set thag are not in 2nd set

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)
# >>>{4, 5, 6, 7, 8, 9}

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setB.difference(setA)
print(diff)
# >>> {10, 11, 12}


# ******************************************
### Symmetric method
# symmetric method return all element but not which are available in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.symmetric_difference(setB)
print(diff)
# >>> {4, 5, 6, 7, 8, 9, 10, 11, 12}

#Union , Intersection, and symmetric does not affect real set

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.update(setB)
print(setA)
# >>> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# **************************************** Update intersection method
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)
# >>> {1, 2, 3}

# **************************************** Update difference method
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)
# >>> {4, 5, 6, 7, 8, 9}

# **************************************** Update symmetric difference method
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)
# >>> {4, 5, 6, 7, 8, 9, 10, 11, 12}


# ****************************************
### Subset (means) the all the elemnts of our first set are in also in second set
setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setA.issubset(setB))
# >>> False 

setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setB.issubset(setA))
# >>> True

# ***************************************
## Superset return truf if first set contain all the element of second set
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issuperset(setA))
# >>> False (bcz setB not contain all the element of setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issuperset(setB))
# >>> True

# ***************************************
### disjoint method return if both sets return null intersection
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.isdisjoint(setB))
# >>> False

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7,8}
print(setA.isdisjoint(setC))
# >>> True


# *********************************
## it only copy reference
setA = {1,2,3,4,5,6}
setB = setA
setB.add(7)
print(setB)
print(setA)
# >>>{1, 2, 3, 4, 5, 6, 7}
# >>>{1, 2, 3, 4, 5, 6, 7}

setA = {1,2,3,4,5,6}
setB = setA.copy()
setB.add(7)
print(setB)
print(setA)
# >>> {1, 2, 3, 4, 5, 6, 7}
# >>> {1, 2, 3, 4, 5, 6}

setA = {1,2,3,4,5,6}
setB = set(setA)
setB.add(7)
print(setB)
print(setA)
# >>> {1, 2, 3, 4, 5, 6, 7}
# >>> {1, 2, 3, 4, 5, 6}

# **************************************
########## Frozen set
a = frozenset([1,2,3,4])
a.add(2)
print(a)
# >>> AttributeError: 'frozenset' object has no attribute 'add'


a = frozenset([1, 2, 3, 4])
a.remove(1)
print(a)
# >>> AttributeError: 'frozenset' object has no attribute 'remove'


####################################################
###########################################
########################### String
# Strings: ordered, immutable, text representation
my_string = "Hello World" #or 'hello world'
print(my_string)


# But remember when text already contain single quote
# my_string = 'I'm a programmer'   #wrong
my_string = 'I\'m a programmer'
print(my_string)
# >>> I'm a programmer


my_string = "I'm a programmer"
print(my_string)
# >>> I'm a programmer


my_string = """Hello
world"""
print(my_string)
# >>> Hello
# >>> world


my_string = """Hello\ world"""
print(my_string)
# >>> Hello world

my_string = "Hello World"
char = my_string[0]
print(char)
# >>> H

my_string = "Hello World"
char = my_string[-1]
print(char)
# >>> d

my_string = "Hello World"
char = my_string[1:5]
print(char)
# >>> ello

my_string = "Hello World"
char = my_string[:5]
print(char)
# >>> Hello

my_string = "Hello World"
char = my_string[::1]
print(char)
# >>> Hello World

my_string = "Hemlo World"
char = my_string[::2] #every second step from existing
print(char)
# >>> HmoWrd


my_string = "Hello World"
char = my_string[::1]
print(char)
# >>> Hello World


my_string = "Hello World"
char = my_string[::-1]
print(char)
# >>> dlroW olleH


# *******************************************
## Cancatenate string
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
# >>> Hello World

# ****************************************** Iterating
greeting = "Hello"
for i in greeting:
    print(i)
# >>>H
# >>>e
# >>>l
# >>>l
# >>>o

greeting = "Hello"
if "e" in greeting:
    print('yes')
else:
    print('no')
# >>> yes

greeting = "Hello"
if "ell" in greeting:
    print('yes')
else:
    print('no')
# >>> yes


# **************************************
## Remove white space character
my_string = "    Hello world   "
my_string = my_string.strip()
print(my_string)
# >>> Hello world

my_string = 'Hello World'
print(my_string.startswith('Hello'))
# >>> True

my_string = 'Hello World'
print(my_string.endswith('Hello'))
# >>> False

my_string = 'Hello World'
print(my_string.find('o'))
# >>> 4

my_string = 'Hello World'
print(my_string.find('lo'))
# >>> 3

# *************************************
## If it not find substring it returns (-1)
my_string = 'Hello World'
print(my_string.find('pp'))
# >>> -1


my_string = 'Hello World'
print(my_string.count('o'))
# >>> 2

my_string = 'Hello World'
print(my_string.count('p'))
# >>> 0

my_string = 'Hello World'
print(my_string.replace('World', 'Universe'))
# >>> Hello Universe

# *************************************************
################################### String Method
my_string = 'How, are you doing'
my_list = my_string.split()
print(my_list)
# >>> ['How,', 'are', 'you', 'doing']


my_string = 'How, are you doing'
my_list = my_string.split(" ")
print(my_list)
# >>> ['How,', 'are', 'you', 'doing']


my_string = 'How, are, you, doing'
my_list = my_string.split(" ")
print(my_list)
# >>> ['How,', 'are,', 'you,', 'doing']


my_string = 'How, are, you, doing'
my_list = my_string.split(",")
print(my_list)
# >>> ['How', ' are', ' you', ' doing']

# ***********************************
######### .JOIN() Method
my_string = 'How, are, you, doing'
my_list = my_string.split(",")
print(my_list)
new_string = ''.join(my_list)
print(new_string)
# >>> ['How', ' are', ' you', ' doing']
# >>> How are you doing

# ***********************************
#########
my_list = ['a'] * 6
print(my_list)
# >>> ['a', 'a', 'a', 'a', 'a', 'a']

#************************************
my_list = ['a'] * 6
print(my_list)
my_string = ''
for i in my_list:
    my_string = my_string + i
print(my_string)
# >>> ['a', 'a', 'a', 'a', 'a', 'a']
# >>> aaaaaa

######  OR
my_list = ['a','a','a','a','a','a']
print(my_list)
my_string = ''.join(mylist)
print(my_string)


# ************************************* Use_ timeit method
from timeit import default_timer as timer
my_list = ['a'] * 6
print(my_list)

#bad
start = timer()
my_string = ''
for i in my_list:
    my_string = my_string + i
stop = timer()
print(stop-start)
# >>> 1.579999843670521e-05

#Good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
# >>> ['a', 'a', 'a', 'a', 'a', 'a']
# >>> 8.170000000973232e-05
# >>> 4.300000000512227e-06


# ***************************************
from timeit import default_timer as timer
my_list = ['a'] * 1000000
# bad
start = timer()
my_string = ''
for i in my_list:
    my_string = my_string + i
stop = timer()
print(stop-start)

# Good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
# >>> 0.21447079999961716
# >>> 0.00919390000126441

# *************************************
from timeit import default_timer as timer
my_list = ['a'] * 6
print(my_list)
my_string = ''.join(my_list)
print(my_string)
# >>> ['a', 'a', 'a', 'a', 'a', 'a']
# >>> aaaaaa


# *************************************************
############################################
######################## Formating method
# %, .format(), f-string
var = "Tom"
my_string = "the variable is %s" %var
print(my_string)
# >>> the variable is Tom


var = 3
my_string = "the variable is %d" %var
print(my_string)
# >>> the variable is 3


var = 3.121
my_string = "the variable is %d" %var
print(my_string)
# >>> the variable is 3


var = 3.121
my_string = "the variable is %f" %var
print(my_string)
# >>> the variable is 3.121


var = 3.121
my_string = "the variable is %.2f" %var
print(my_string)
# >>> the variable is 3.12


# ******************************************
#### .format() method
var = 3.1234567
my_string = "the variable is {}".format(var)
print(my_string)
# >>> the variable is 3.1234567


var = 3.1234567
my_string = "the variable is {:.2f}".format(var)
print(my_string)
# >>> the variable is 3.12


var = 3.1234567
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)
# >>> the variable is 3.12 and 6

# ******************************************
# f-string method
var = 3.1234567
var2 = 6
my_string = f"the variable is {var} and {var2}"
print(my_string)
# >>> the variable is 3.1234567 and 6


var = 3.1234567
var2 = 6
my_string = f"the variable is {var*2} and {var2}"
print(my_string)
# >>> the variable is 6.2469134 and 6


#######################################################
################################################
########################## Collection module
# * collections : Counter, namedtuple, OrderedDict defaultdict, deque
# *Counter:- Counter is container that stores element as dictionary key that counts dictionary values
from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
# >>> Counter({'c': 9, 'a': 6, 'b': 6})


from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter.items())
# >>> dict_items([('a', 6), ('b', 6), ('c', 9)])

from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter.keys())
# >>> dict_keys(['a', 'b', 'c'])

from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter.values())
# >>> dict_values([6, 6, 9])


from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
# >>> Counter({'c': 9, 'a': 6, 'b': 6})
# >>> [('c', 9)]


from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
# >>> Counter({'c': 9, 'a': 6, 'b': 6})
# >>> c


from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.elements())
# >>> Counter({'c': 9, 'a': 6, 'b': 6})
# >>> c

# **********************************
# Get diffrent list
from collections import Counter
a = "aaaaaabbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(list(my_counter.elements()))
# >>> Counter({'c': 9, 'a': 6, 'b': 6})
['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b',
    'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
# >>> c

# *************************************
######## namedtuple method
# is an easy to create 
from collections import namedtuple
point = namedtuple('Point', 'x,y')
pt = point(1, -4)
print(pt.x, pt.y)


# *********************************************
##############################################
########## Orderdict is just like regular dict but they remember order the item were inserted but
#but now built in dict class has also ability to remember after python3.6
from collections import OrderedDict
Ordered_dict = OrderedDict()
Ordered_dict['b'] = 2
Ordered_dict['c'] = 3
Ordered_dict['d'] = 4
Ordered_dict['a'] = 1
print(Ordered_dict)
# >>>OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])

# *************************************
from collections import OrderedDict
Ordered_dict = {}
Ordered_dict['b'] = 2
Ordered_dict['c'] = 3
Ordered_dict['d'] = 4
Ordered_dict['a'] = 1
print(Ordered_dict)
# >>>{'b': 2, 'c': 3, 'd': 4, 'a': 1}


# ****************************************
################ Defaultdict
# Defaultdict is just like normal dict container the only diff is  it have defaul value if the key will yet not to be set
from collections import defaultdict
d = defaultdict(int) # we canalso put her float/emp list/
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['c'])
# >>> 0


from collections import defaultdict
d = {} # we canalso put her float/emp list/
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['c'])
# >>> keyerror


# *****************************************
################## Deque method
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
# >>> deque([3, 1, 2])
# >>> deque([3, 1])
# >>> deque([1])
# >>> ([])


from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.extendleft([4,5,6])
print(d)
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(3)
print(d)
# >>> deque([6, 5, 4, 3, 1, 2])
# >>> deque([2, 6, 5, 4, 3, 1])
# >>> deque([3, 1, 2, 6, 5, 4])
# >>> deque([6, 5, 4, 3, 1, 2])


# *******************************************
############################# Itertools
# itertools: product, permutations, combinations, accumulation, group by infinite iterators
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)
# >>> <itertools.product object at 0x0000020ECCF63280 >


from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))
# >>> [(1, 3), (1, 4), (2, 3), (2, 4)]


from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)
print(list(prod))
# >>> [(1, 3), (2, 3)]


from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat = 2)
print(list(prod))
# >>> [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]


from itertools import product
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))
# >>> [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

# **************************************
##### permutations
from itertools import permutations
a = [1,2,3]
perm = permutations(a, 2) # here 2 is length
print(list(perm))
# >>> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# **************************************
##### combinations
from itertools import combinations
a = [1,2,3]
perm = combinations(a, 2) # here 2 is length
print(list(perm))
# >>> [(1, 2), (1, 3), (2, 3)]


from itertools import combinations, combinations_with_replacement
a = [1,2,3]
perm = combinations(a, 2) # here 2 is length
print(list(perm))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))
# >>> [(1, 2), (1, 3), (2, 3)]
# >>> [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


# *******************************************
###################################
######### Accumulate function by default it will compute sum
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))
# >>> [1, 2, 3, 4]
# >>> [1, 3, 6, 10]


from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a, func = operator.mul)
print(a)
print(list(acc))
# >>> [1, 2, 3, 4]
# >>> [1, 2, 6, 24]

# *************************************
from itertools import accumulate
import operator
a = [1,2,5,4,3]
acc = accumulate(a, func = max)
print(a)
print(list(acc))
# >>> [1, 2, 3, 4]
# >>> [1, 2, 3, 4]


# ***********************************************
#########################
# group by functions makes iteratators that returns key and group from iterable
from itertools import groupby
def smaller_than_3(x):
    return x <3
a = [1,2,5,3,4]
group_obj = groupby(a, key= smaller_than_3)
print(group_obj)
# >>> <itertools.groupby object at 0x000002CAC7C84F90>


# **************************************
from itertools import groupby
def smaller_than_3(x):
    return x <3
a = [1,2,5,3,4]
group_obj = groupby(a, key= smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
# >>> True [1, 2]
# >>> False [5, 3, 4]


# **************************************
from itertools import groupby
def smaller_than_3(x):
    return x <3
a = [1,2,5,3,4]
group_obj = groupby(a, key= smaller_than_3)
for key, value in group_obj:
    print(key,list(value))
    
# *************************************
from itertools import groupby
def smaller_than_3(x):
    return x <3
a = [1,2,5,3,4]
group_obj = groupby(a, lambda x: x<3)
for key, value in group_obj:
    print(key,list(value))
# >>> True [1, 2]
# >>> False [5, 3, 4]


from itertools import groupby
person = [{'name':'Tim','age':25}, {'name':'Dan','age':25}, {'name':'Lisa','age':27}, {'name':'Claire','age':28}]
group_obj = groupby(person, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# >>> 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# >>> 27 [{'name': 'Lisa', 'age': 27}]
# >>> 28 [{'name': 'Claire', 'age': 28}]

# ******************************************
#####################
from itertools import count , cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
# >>> loop from 10 to 15


from itertools import count, cycle, repeat
a = [1,2,3]
for i in cycle(a):
    print(i)
# >>> infinte loop from start onwards


from itertools import count, cycle, repeat
a = [1,2,3]
for i in repeat(1):
    print(i)
# infinite loop
    

# *******************************************
# ****************************************
#################################### Lambda
# Lamda arguments: expression
add10 = lambda x: x + 10
print(add10(5))
# >>> 15

#or
def add10_func(x):
    return x + 10


mult = lambda x,y: x*y
print(mult(2,7))
# >>> 14

# *************************************
## sorting by lamda
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)
# >>> [(1, 2), (15, 1), (5, -1), (10, 4)]
# >>> [(1, 2), (5, -1), (10, 4), (15, 1)]


## ***************************************
###### Lambda as key arguments
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key = lambda x:x[1])

print(points2D)
print(points2D_sorted)
# >>> [(1, 2), (15, 1), (5, -1), (10, 4)]
# >>> [(5, -1), (15, 1), (1, 2), (10, 4)]


def sort_by_y(x):
    return[1]
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key = sort_by_y)

print(points2D)
print(points2D_sorted)
# >>> [(1, 2), (15, 1), (5, -1), (10, 4)]
# >>> [(5, -1), (15, 1), (1, 2), (10, 4)]

# sort by sum of each
points2D = [(1,2), (15,1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key = lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)
# >>> [(1, 2), (15, 1), (5, -1), (10, 4)]
# >>> [(1, 2), (5, -1), (10, 4), (15, 1)]


## *******************************************
######################### Map functions 
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# lambda arguments: expression
# map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x:x*2, a)
print(list(b))
# >>> [2, 4, 6, 8, 10]


### you can even write like this
a = [1,2,3,4,5]
c = [x*2 for x in a]
print(c)
# >>> [2, 4, 6, 8, 10]


## *****************************************
#############  Filter function 
# this function will return all the element for which function evaluate to true
# 
# lambda arguments: expression
# filter(func, seq)

a = [1,2,3,4,5]
b = filter(lambda x: x%2 == 0, a)
print(list(b))

#or
a = [1,2,3,4,5]
c = (x for x in a if x%2 ==0)
print(c)

# ********************************************
# reduce (func, seq)
# it's always has two arguments
from functools import reduce
a = [1,2,3,4,5,6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
# >>> 720


# *******************************************
#############################################
# Exceptions 
a = 5 
print(a)))
# >>> syntax error

a = 5 + '10'
print(a)
# >>> type error

import somemodule
# >>> modeule error


a = 5
b = c
# >>> NameError

f = open('some.txt')
# >>> fileError

a = [1,2,3]
a.remove(4)
print(a)
# >>> valueError

a = [1,2,3]
a[4]
print(a)
# >>> IndexError

my_dict = {'name':'Max'}
my_dict['age']
# >>> KeyError

x = -5
if x < 0:
    raise Exception('x should be positive')
# >>> Exception: x should be positive

x = 5
if x < 0:
    raise Exception('x should be positive')
# >>> 

## ******************************************
############ Second method (Use assert statement)
x = - 5
assert (x>=0)
# >>> AssertionError: x is not positive


x =  5
assert (x>=0)
# >>> 

# *****************************************
###### try and except statement
try:
    a = 5/0
except:
    print('an error happened')
# >>> an error happened

try:
    a = 5/0
except Exception as e:
    print(e)
# >>> division by zero


# *****************************
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# >>> unsupported operand type(s) for +: 'float' and 'str'


# *****************************
try:
    a = 5/0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# >>> division by zero


# ****************************
try:
    a = 5/0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')
# >>> division by zero
# >>> cleaning up...


#Error and Expections
class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x> 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
    # >>> value is too high





class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
    
def test_value(x):
    if x> 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small')  
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
# >>> value is too high


#################################################
################################ (Logging) Module
# ***********************
import logging
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')
# >>> WARNING:root:This is a warning message
# >>> ERROR:root:This is a error message      
# >>> CRITICAL:root:This is a critical message
# * it's showing only warning, error,critical it's bcz by default only messages with lable warning or aboeffuf are printied

#* if we want to show all we have to some basic configuration
# **************************************************
import logging
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('this is an info message')
logging.warning('this is an error message')
logging.error('This is an error message')
logging.critical('this is an critical message')


import logging
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %H:%M:%S')
import helper
#  it will locked the message from the helper module with name 


import logging
logger = logging.getLogger(__name__)
logger.info('hello from helper')


import logging
logger = logging.getlogger(__name__)
# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setlevel(logging.warning)
file_h.setlevel(logging.ERROR)

formatter = logging.Formatter('%(name')s - %(levelname)s - %(message)s')
stream_h.setfFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHand(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')



####################################################
###########################################
# ********************************** JSON
# Python:- dict, list/tuple, str, int/long/float, True, False, None
# JSON:-  onject,   array,  string,  number,   true,  false, null

# **************************** Serialization/encoding
# convert python object in JSON
import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person)
print(personjson)
# >>> {"name": "John", "age": 30, "city": "New York", "Haschildren": "False", "titles": ["engineer", "programmer"]}


import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4)
print(personjson)
# >>> {
# >>>     "name": "John",        
# >>>     "age": 30,
# >>>     "city": "New York",    
# >>>     "Haschildren": "False",
# >>>     "titles": [
# >>>         "engineer",        
# >>>         "programmer"
# >>>     ]
# >>> }


import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4, separators = ('; ')) #instead of column use semicolumn
print(personjson)
# >>> {
# >>>     "name" "John";        
# >>>     "age" 30;
# >>>     "city" "New York";    
# >>>     "Haschildren" "False";
# >>>     "titles" [
# >>>         "engineer";       
# >>>         "programmer"
# >>>     ]
# >>> }

#* Note better to use remains default don't use

import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4, sort_keys= True) # bydeafult its would be False
print(personjson)
# >>> {
# >>>     "Haschildren": "False",
# >>>     "age": 30,
# >>>     "city": "New York",    
# >>>     "name": "John",        
# >>>     "titles": [
# >>>         "engineer",        
# >>>         "programmer"
# >>>     ]
# >>> }


import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4, sort_keys= True) # bydeafult its would be False
print(personjson)
# >>> {
# >>>     "age": 30,
# >>>     "city": "New York",    
# >>>     "haschildren": "False",
# >>>     "name": "John",        
# >>>     "titles": [
# >>>         "engineer",        
# >>>         "programmer"
# >>>     ]
# >>> }


import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4, sort_keys= True) # bydeafult its would be False
print(personjson)

with open('person.json', 'w') as file:
    json.dump(person, file)

# it creates file person.json
# >>> {
# >>>     "Haschildren": "False",
# >>>     "age": 30,
# >>>     "city": "New York",    
# >>>     "name": "John",        
# >>>     "titles": [
# >>>         "engineer",        
# >>>         "programmer"
# >>>     ]
# >>> }

# ******************************************
#######################################
### Deserialization
# convert JSON into python object

import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4, sort_keys= True) # bydeafult its would be False

person = json.loads(personjson)
print(person)
# >>> {'Haschildren': 'False', 'age': 30, 'city': 'New York', 'name': 'John', 'titles': ['engineer', 'programmer']}


# *** Or
import json
person = {"name": "John", "age":30, "city":"New York", "Haschildren":"False", "titles":["engineer", "programmer",]}
personjson = json.dumps(person, indent= 4, sort_keys= True) # bydeafult its would be False

with open('person.json', 'r') as file: # by default it lives in read in mode
    person = json.load(file)
print(person)
# >>> {'Haschildren': 'False', 'age': 30, 'city': 'New York', 'name': 'John', 'titles': ['engineer', 'programmer']}

#* In this case we work with dictionary lets we have custom data



# *******************************************************
###################################### JSON with custm data
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User('Max',27)
userJSON = json.dumps(user)
# >>> raise TypeError(f'Object of type {o.__class__.__name__} '
# >>> TypeError: Object of type User is not JSON serializable

#* its bcz of user is not in json serilisable

# *********************************************
# we have to write a custom encoding function
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User('Max',27)

def encode_user(o):
    if isinstance(o, User): #we checked if our object is of with this is instance method whether an object is instance of our class
        return{'name':o.name, 'age':o.age, o.__class__.__name__:True} #class name as key, this'll give name of class as string, we added user class name as key
    else:
        raise TypeError('Object of type user is not JSON serialiation ')
userJSON = json.dumps(user, default = encode_user) #this now use encode_user function how to encode function
print(userJSON)
print(type(userJSON))
# >>> {"name": "Max", "age": 27, "User": true}
# >>> <class 'str'>
# so this how we encode custom object with this default arguments



#################################################
###Second way
#* So we can also impliment json custom encoder
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of type user is not JSON serialiation ')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
# userJSON = json.dumps(user, cls = UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)
print(type(userJSON))
# >>> {"name": "Max", "age": 27, "User": true}
# >>> <class 'str'>


# ****************************************
# #**** Deocde our object back
# if we want to format in normal foramt from json
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of type user is not JSON serialiation ')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
userJSON = UserEncoder().encode(user)
print(userJSON)
print(type(userJSON))
user = json.loads(userJSON)
print(user)
print(type(user))

# >>> {"name": "Max", "age": 27, "User": true}
# >>> <class 'str'>
# >>> {'name': 'Max', 'age': 27, 'User': True}
# >>> <class 'dict'>


# ***************************************
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return{'name':o.name, 'age':o.age, o.__class__.__name__:True} # here we added user class name as key
    else:
        raise TypeError('Object of type user is not JSON serialiation ')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name = dct['name'], age = dct['age'])
    return dct

user = json.loads(userJSON, object_hook= decode_user)
print(type(user))
print(user)
print(user.name) # we can accesss intances variable
# >>> {"name": "Max", "age": 27, "User": true}
# >>> <class '__main__.User'>
# >>> <__main__.User object at 0x000001DFF4B6AEF0>
# >>> Max


####################################################
################################## Random Number
import random
a = random.random() # produce random flaots range b/w 0 to 1
print(a)
# >>> 0.5430976796399063

#******************** if we have specific range
import random
a = random.randint(1, 10) #this is also inclue uperbound(10)
print(a)
# >>> 10

# ********************
import random 
a = random.randrange(1,10) #this isn't include uperbound produce below 10
print(a)

# ********************
import random 
a = random.normalvariate(0,1) #it is pick random value from normal distribution with mean of 0 and standard deviation 1
print(a)


import random
mylist = list("ABCDEFGHI")
a = random.choice(mylist)
print(a)
# >>> H


import random
mylist = list("ABCDEFGHI")
a = random.sample(mylist, 3)
print(a)
# >>> ['I', 'F', 'H']


import random
mylist = list("ABCDEFGHI")
a = random.choices(mylist, k = 3)
print(a)
# >>> ['B', 'C', 'A']


import random
mylist = list("ABCDEFGHI")
random.shuffle(mylist)  
print(mylist)
# >>> ['A', 'D', 'B', 'E', 'G', 'F', 'C', 'I', 'H']


import random

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

# >>> 0.13436424411240122
# >>> 2
# >>> 0.9560342718892494 
# >>> 1
# >>> 0.13436424411240122
# >>> 2
# >>> 0.9560342718892494 
# >>> 1

# this is use for password, security token, account authentication
import secrets
a = secrets.randbelow(10)
print(a)
# >>> 7

import secrets
a = secrets.randbits(4)
# 1111 this is 15 #means this will genrate number from range 1 too 15
print(a)
# >>> 6


import secrets
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
# >>> H

# ***************************************
######################### Numpy module
import numpy as np
a = np.random.rand(3)
print(a)
# >>> [0.74077354 0.84752729 0.54361884]


import numpy as np
a = np.random.randint(0, 10, (3,4))
print(a)
# >>> [[8 9 9 6] 
#     [9 2 5 2] 
#     [2 3 3 0]]


import numpy as np
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)
# >>> [[1 2 3] 
#      [4 5 6] 
#      [7 8 9]]
#     [[1 2 3] 
#      [4 5 6] 
#      [7 8 9]]


import numpy as np
np.random.rand(3,3)
np.random.seed(1)
print(np.random.rand(3,3))
# >>> [[4.17022005e-01 7.20324493e-01 1.14374817e-04] 
#      [3.02332573e-01 1.46755891e-01 9.23385948e-02] 
#      [1.86260211e-01 3.45560727e-01 3.96767474e-01]]


## *********************************************
################################### Decorators
#############################
# there are two types of decoraters 
# *1. functions decorators 2.class decoraters
# more common function dedcorator
# the decoraters is functions that takes an another functions as argument and extends the behaiouur of this functions

@mydecorator
def dosomething():
    pass
# OR it allows new functionality to new function

def start_end_decorator(func):
    def wrapper(): #inner function which wraps our function
        print('Start') 
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
print_name = start_end_decorator(print_name)
print(print_name())
# Start
# Alex
# End
# None



def start_end_decorator(func):
    def wrapper(): #inner function which wraps our function
        print('Start') 
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
print_name = start_end_decorator(print_name)
print_name()
# >>> Start
# >>> Alex
# >>> End 



# ****************************************
def start_end_decorator(func):
    def wrapper(): #inner function which wraps our function
        print('Start') 
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')
print_name()
# >>> Start
# >>> Alex
# >>> End 

# *************************
def start_end_decorator(func):
    def wrapper(): #inner function which wraps our function
        print('Start') 
        func()
        print('End')
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
add5(10)
# >>> TypeError: start_end_decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given

# by *arg and *kwarg we can use many arguments in a keyword arguments as i want
def start_end_decorator(func):
    def wrapper(*arg, **kwargs): #inner function which wraps our function
        print('Start') 
        func(*arg, **kwargs)
        print('End')
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
add5(10)
# >>> Start
# >>> End


# ****************************
def start_end_decorator(func):
    def wrapper(*arg, **kwargs): #inner function which wraps our function
        print('Start') 
        func(*arg, **kwargs)
        print('End')
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
result = add5(10)
print(result)
# >>> Start
# >>> End 
# >>> None

# ***********************************
def start_end_decorator(func):
    def wrapper(*arg, **kwargs): #inner function which wraps our function
        print('Start') 
        result = func(*arg, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
result = add5(10)
print(result)
# >>> Start
# >>> End
# >>> 15

# ****************************************
# Find function identity

def start_end_decorator(func):
    def wrapper(*arg, **kwargs): #inner function which wraps our function
        print('Start') 
        result = func(*arg, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
print(help(add5))
print(add5.__name__)
# >>> Help on function wrapper in module __main__:
# >>> wrapper(*arg, **kwargs)
# >>> None
# >>> wrapper

# *******************************************************
# Here python is now confuse in order to find identity it gives functions name wrapper
#* so in oreder to fix this we 
import functools
def start_end_decorator(func):
    @functools.wraps(func) # this now preserve information of my used function
    def wrapper(*arg, **kwargs): #inner function which wraps our function
        print('Start') 
        result = func(*arg, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
# print_name = start_end_decorator(print_name)
print(help(add5))
print(add5.__name__)

# >>> Help on function add5 in module __main__:
# >>> add5(x)
# >>> None
# >>> add5


# And also here funtion name
import functools
def start_end_decorator(func):
    @functools.wraps(func) # this now preserve information of my used function
    def wrapper(*arg, **kwargs): #inner function which wraps our function
        print('Start') 
        result = func(*arg, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
# print_name = start_end_decorator(print_name)
print(add5.__name__)
# >>> add5


# Templete for nice decorator
import functools
def my_decorator(func):    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #Do
        result = func(*args, **kwargs)
        #Do
        return result
    return wrapper
@start_end_decorator
def add5(x):
    return x + 5

# Now as we seen here decorator that takes a functions decorator can also takes arguments and what this means this is basically now two enough function so enough function in a function
import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times = 3)
def greet(name):
    print(f'Hello {name}')
greet('Alex')
# >>> Hello Alex
# >>> Hello Alex    
# >>> Hello Alex 


import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times = 4)
def greet(name):
    print(f'Hello {name}')
greet('Alex')
# >>> Hello Alex
# >>> Hello Alex    
# >>> Hello Alex 
# >>> Hello Alex 


# *********************************************
# Nested deocrators
import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper
@debug 
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print('greeting')
    return greeting

say_hello('Alex')

# >>> Calling say_hello('Alex')
# >>> start
# >>> greeting
# >>> End
# >>> 'say_hello' returned 'Hello Alex'

# Instead of function decorators we can also define class decorator
class CountCalls:
    def __init__ (self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):        
        print("Hi There")
        
cc = CountCalls(None)
cc()
# >>> Hi There



@CountCalls
def say_hello():
    print('Hello')
    
    
# *******************************
class CountCalls:
    def __init__ (self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):        
        self.num_calls +=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')
say_hello()
say_hello()
# >>> This is executed 1 times
# >>> Hello

#* If you run second times it gives output
class CountCalls:
    def __init__ (self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):        
        self.num_calls +=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')
say_hello()
say_hello()
# >>> This is executed 1 times
# >>> Hello
# >>> This is executed 2 times
# >>> Hello
# so we can track of how may times this is executed


# *****************************************
##########################################
####################### Generators
# generator are function that return objects that can be iteretor over, special thing generator items inside the object lazaly which mean generator items one at a time an only when you ask for it and bcz of this more effeciant than other sequence


def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
for i in g:
    print(i)
# >>> 1
# >>> 2
# >>> 3
    
# * we can also get a value one at time in the next function
def mygenerator():
    yield 1
    yield 2
    yield 3
g = mygenerator()
value = next(g)
print(value)
# >>> 1
value = next(g)
print(value)
# >>> 2
value = next(g)
print(value)
# >>> 3
value = next(g)
print(value)
# >>> StopIteration

# we can also calculate over here
def mygenerator():
    yield 1
    yield 2
    yield 3
g = mygenerator()
value = sum(g)
print(value)
# >>> 6

# **************************
# Bulit in sorted method
# this will create a return a new list all the object with sorted manner
def mygenerator():
    yield 1
    yield 2
    yield 3
g = mygenerator()
print(sorted(g))
# >>> [1, 2, 3]


# countdown takes a starting number
def countdown(num):
    print('Starting')
    while num >0:
        yield num
        num-=1

cd = countdown(4) # till here noting will be printed
value = next(cd)
print(value)
# >>> Starting
# >>> 4


def countdown(num):
    print('Starting')
    while num >0:
        yield num
        num-=1

cd = countdown(4) # till here noting will be printed
value = next(cd)
print(value)
print(next(cd))
# >>> Starting
# >>> 4
# >>> 3


def countdown(num):
    print('Starting')
    while num >0:
        yield num
        num-=1

cd = countdown(4) # till here noting will be printed
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
# Starting
# 4
# 3
# 2
# 1
# Traceback (most recent call last):
#   File "c:\VsCode\py4e\tempCodeRunnerFile.py", line 13, in <module>
#     print(next(cd))
# StopIteration

# * generaotrs are very memory effecient they save a lot of memory when you work with large data

# Example function call 1st n and it takes a number as an input and this will return a sequence with all the number starting fom zero all the but upto n
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

print(firstn(10))
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(firstn(10)))
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> 45

# So here all the number store in the list and take lot of memry
#########################################


# if we use generator instead
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
li = firstn(10)
print(li)
print(sum(li))
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> 45


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1
print(sum(firstn_generator(10)))
# >>> 45

# Now we can see how muchh stored they have taken in memory
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
li = firstn(10)

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1
print(sys.getsizeof(firstn(10)))
print(sys.getsizeof(firstn_generator(10)))
# >>> 184
# >>> 104

import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
li = firstn(10)

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
# >>> 8448728
# >>> 104

# Now lets take an anothere example
def fibonacci(limit):
    # 0 1 1 2 3 5 8
    a,b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b
fib = fibonacci(30)
for i in fib:
    print(i)
# >>> 0
# >>> 1
# >>> 1
# >>> 2
# >>> 3
# >>> 5
# >>> 8
# >>> 13
# >>> 21

    
# **************************************
# lets have look at Generator expression so Generator expression are written in the same way with list comprehesions but with parenthesis instead of sqaure brackets this is very simple and shortcut thing

mygenerator = (i for i in range(10) if i%2 ==0) 
# it's similar to list comprehenshion but use square bracket instead of parenthesis
# mygenerator = [ i for i in range(10) if i%2 ==0]
for i in mygenerator:
    print(i)
# >>> 0
# >>> 2
# >>> 4
# >>> 6
# >>> 8


mygenerator = (i for i in range(10) if i%2 ==0)
print(list(mygenerator))
# >>> [0, 2, 4, 6, 8]


#let's see the sizze of object in each one
import sys
mygenerator = (i for i in range(10000) if i%2 ==0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10000) if i%2 ==0]
print(sys.getsizeof(mylist))
# >>> 104
# >>> 41880


##############################################
#*******************************************
############## Threading VS Multiprocessing
# you can run code and parellel and speed of code
"""
(Process):-
Process: An instance of a program (e.g a python intepreter,if i'm running firefox browser)
+ A Thread is basically An entity in process
+ Takes advantage of multiple CPUs and cores
+ Separate memory space -> Memory is not shared b/w processor
+ New process is stated independently from other processes
+ Processes are interruptable/killable
+ One GIL for each process -> avoid GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread
- More memory
- IPC (inter-process communication is more complicated)

"""

# Thread
"""
Thread :- An entity within a process that can be scheduled (also known as "leightweight process)
+ All thread within a process share the same memory
+ leightweight
+ Starting a thread is faster than starting a process
+ Great for I/O -

- Threading is limited by GIL: Only one thread at a time
- No effect for CPU- INbound tasks
- Not interruptable/killable
-Careful with race conditions
"""

# GIL : Global interpreter lock
"""
- A lock that allows only onethread at a time to execute in python
- Needed in CPython because memory managment is not thread - safe 
- Avoid:
    - Use multiprocessing
    - Use a diffrent, free-threaded python implementation (jython, IronPython)
    - Use Python as a wrapper for thrid- party libraries (c/c++) -> numpy, scipy
"""

# *************************************
###################### Multiprocessing
from multiprocessing import Process
import os
import time
def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)
process = []
num_processes = os.cpu_count()

#create processes
for i in range(num_processes):
    p = Process(target = square_numbers())
    process.append(p)
    
# start
for p in process:
    p.start()

# join
for p in process:
    p.join()
    
print(' ')

#################################################
############################################
# ************************  Multi threading
from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)
        
thread = []
num_threads = 10

#create processes
for i in range(num_threads):
    t = Thread(target = square_numbers)
    thread.append(t)
    
# start
for t in thread:
    t.start()
    
# join
for t in thread:
    t.join()

print('end main')

###############################################
###########################################
# ***************************** Threading
from threading import Thread
import sys
import time
database_value = 0
def increase():
    global database_value
    local_copy = database_value
    
    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
if __name__ == "__main__":
    print('start value', database_value)
    
    thread1 = Thread(target = increase)
    thread2 = Thread(target = increase)
    
    
    thread1 = Thread(target =increase)
    thread2 = Thread(target = increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)
    
    print('End main')
    
# >>> start value 0
# >>> end value 1
# >>> End main
    
    
    

from threading import Thread, Lock
import sys
import time
database_value = 0
def increase():
    global database_value
    
    lock.acquire()
    local_copy = database_value
    
    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()
if __name__ == "__main__":
    lock = Lock()
    print('start value', database_value)
    
    thread1 = Thread(target = increase, args = (lock,))
    thread2 = Thread(target = increase, args = (lock,))
    
    
    thread1 = Thread(target =increase)
    thread2 = Thread(target = increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)
    
    print('End main')
# >>> start value 0
# >>> end value 2
# >>> End main   



from threading import Thread, Lock
import sys
import time
database_value = 0
def increase():
    global database_value
    with lock:
        local_copy = database_value
        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
    
if __name__ == "__main__":
    lock = Lock()
    print('start value', database_value)
    
    thread1 = Thread(target = increase, args = (lock,))
    thread2 = Thread(target = increase, args = (lock,))
    
    
    thread1 = Thread(target =increase)
    thread2 = Thread(target = increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)
    
    print('End main')

# >>> start value 0
# >>> end value 2
# >>> End main 


###################################################
########## how to use queue
# Queueis linear data structure that follow fifo first in first out principle
# Queue of customer 
from threading import Thread, Lock
from queue import Queue
import sys
import time

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    
    # 3,2,1 -->
    first = q.get()
    print(first)
    print('end')
# >>> 1
# >>> end

    
    
# Queue of customer 
from threading import Thread, Lock
from queue import Queue
import sys
import time

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    
    # 3,2,1 -->
    first = q.get()
    print(first)
    q.task_done()
    q.join()
    print('end main')
    
# >>> 1
    
    
    
# Queue of customer 
from threading import Thread, Lock, current_thread
from queue import Queue
import sys
import time

def worker(q,lock):
    while True:
        value = q.get()
        
        # processing...
        with lock:
            print(f'in{current_thread().name} got {value}')
        q.task_done()
        
if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    num_threads = 10
    
    for i in range(num_threads):
        thread = Thread(target=worker, args = (q,lock))
        thread.daemon = True
        thread.start()
    
    for i in range(1,21):
        q.put(i)
    q.join
        
    print('end')
    # >>> endinThread-4 (worker) got 1


#############################################################
# **************************** Multiprocessing
from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        i*i
        
if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choice for the processes number of 
    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target = square_numbers)
        processes.append(process)
        
    # start all processes
    for process in processes:
        process.start()
        
    #wait for all processes to finish
    # block the main programm until these processes are finished
    for process in processes:
        process.join()
        
        
## how can we share data b/w prosesses
from multiprocessing import Process, Value, Array
import time

def add_100(number):
    for i in range(100):
        time.sleep(0.01)
        number.value += 1
        
if __name__ == '__main__':
    shared_number = Value('i',0)
    print('Number at beginning is', shared_number.value)
    p1 = Process(target = add_100, args = (shared_number,))
    p2 = Process(target = add_100, args = (shared_number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('number at end is', shared_number.value)
# >>> Number at beginning is 0
# >>> number at end is 129
        

# ************************************************
## lock prevent other processes from accessing same time

from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()
        
if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i',0)
    print('Number at beginning is', shared_number.value)
    p1 = Process(target = add_100, args = (shared_number, lock))
    p2 = Process(target = add_100, args = (shared_number, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('number at end is', shared_number.value)
# >>> Number at beginning is 0
# >>> number at end is 200


### or yo can use lock as contest manager
from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value +=1

if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i',0)
    print('Number at beginning is', shared_number.value)
    p1 = Process(target = add_100, args = (shared_number, lock))
    p2 = Process(target = add_100, args = (shared_number, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('number at end is', shared_number.value)
# >>> Number at beginning is 0
# >>> number at end is 200





## ************************************************
### now we share arrray
from multiprocessing import Process, Value, Array, Lock
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for number in numbers:

            number +=1

if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at beginning is', shared_array[:])
    p1 = Process(target = add_100, args = (shared_array, lock))
    p2 = Process(target = add_100, args = (shared_array, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('array at end is', shared_array[:])
# >>> array at beginning is [0.0, 100.0, 200.0]
# >>> array at end is [0.0, 100.0, 200.0]


#################################################
# *************************************
from multiprocessing import Process, Value, Array, Lock
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] +=1


if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at beginning is', shared_array[:])
    p1 = Process(target = add_100, args = (shared_array, lock))
    p2 = Process(target = add_100, args = (shared_array, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('array at end is', shared_array[:])
# >>> array at beginning is [0.0, 100.0, 200.0]
# >>> array at end is [124.0, 228.0, 330.0]


#################################################
# *************************************
from multiprocessing import Process, Value, Array, Lock
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] +=1


if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at beginning is', shared_array[:])
    p1 = Process(target = add_100, args = (shared_array, lock))
    p2 = Process(target = add_100, args = (shared_array, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('array at end is', shared_array[:])
    
# >>> array at beginning is [0.0, 100.0, 200.0]
# >>> array at end is [200.0, 300.0, 400.0]

# this is how we use shared value and shared array




# ******************************************************
# we can also use a queue to exchange element b/w processes
# queue is use for processprocess safe data exchange
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
        
def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)
        
if __name__ == '__main__':
    numbers = range(1,6)
    q = Queue()
    p1 = Process(target = square, args = (numbers, q))
    p2 = Process(target = make_negative, args = (numbers, q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
# this is how we can use Queue

# >>> -1
# >>> -2
# >>> -3
# >>> -4
# >>> -5
# >>> 1 
# >>> 4 
# >>> 9 
# >>> 16
# >>> 25

# *************************************************
#### Prosses Pool :- can be use manage multiple processes, so a process pool object control pool of workprosses to which shop can be submitted and it can manage which available prosses for you and split for example data in small chunks which then can be process parellel in diffrent process
from multiprocessing import Pool

def cube(number):
    return number * number * number
        
if __name__ == '__main__':
    
    numbers = range(10)
    pool = Pool()
    
    #Important Pool method (map, apply, join, close)
    result = pool.map(cube, numbers)
    
    pool.close()
    pool.join()
    
    print(result)

# >>> [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



# To run diffrent processors with a function if we simply want one function executed by a pool
from multiprocessing import Pool

def cube(number):
    return number * number * number
        
if __name__ == '__main__':
    
    numbers = range(10)
    pool = Pool()
    
    #Important Pool method (map, apply, join, close)
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])
    
    pool.close()
    pool.join()
    
    print(result)

# >>> [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


####################################################################
####################################################################
####################################################################
# ********************************** Function Arguments in Details
"""
- The diffrence between argumnets and parameters
- Positional and keyword arguments
- Default arguments
- Variable - lenght arguments (*args and *kwargs)
- Container unpacking into function arguments
- Local vs global arguments
- Parameters passing (by value or by reference?)

"""
# ******************************************************
################## Diffrence b/w arguments & parameter
# name is parameter and alex is argumnets
def print_name(name):
    print(name)
    
print_name('Alex')


# ********************************************************
######################################################
###### Diffrence b/w positional & keyword arguments
# **********************************
def foo(a,b,c):
    print(a,b,c)
foo(1,2,3) # positional arguments 
foo(a = 1, b = 2, c = 3)  #keyword arguments
# >>> 1 2 3
# >>> 1 2 3

# When using keyword arguments only keywords matters not the possesion
def foo(a,b,c):
    print(a,b,c)
foo(c = 1, b = 2, a = 3)
# >>> 3 2 1

#*************************************
#### we can use mix of both arguments
def foo(a,b,c):
    print(a,b,c)
foo(1, b=2, c = 3)
# >>> 1 2 3

# **************************************************************
# we can't use positional arguments after keyword arguments
def foo(a,b,c):
    print(a,b,c)
    
foo(1, b = 2, 3)
# >>> SyntaxError: positional argument follows keyword argument


#************************************************************
# sometime its better to use keyword arguments bcz it makes more clear 

def foo(a,b,c, d= 4):
    print(a,b,c,d)
foo(1,2,3)
# >>> 1 2 3 4

#************************************
def foo(a,b,c = 2, d): #default arguments must be in last
    print(a,b,c,d) #non- default argument follows default argument
foo(1,2,3,7)
# >>> SyntaxError: non-default argument follows default argument


###############################################################
# **************************************************
######### Variable length arguments(args, kwargs)

def foo(a,b, *args, **kwargs): # this is tuple 
# if you marks your parameter with one star(*) *args than you can pass any number of positional arguments to your function
# if you marks your parameter with two star{"*"} **kwargs than you can pass any number of keywords arguments to this function
    print(a,b)
    for arg in (args):
        print(arg)
    # kwargs arguments is a dictionary
    for key in kwargs:
        print(key, kwargs[key])
foo(1,2, 3,4,5, six = 6, seven = 7 ) # we can pass many posinal arguments as we pass

# >>> 1 2
# >>> 3
# >>> 4
# >>> 5
# >>> six 6
# >>> seven 7 

#* So this is how we can use varaible length arguments

def foo(a, b, * args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4)
# >>> 1 2
# >>> 3
# >>> 4

# ************************************************
# force keyword arguments:- so sometimes you want have keyworkd only arguments, you can force and force that so yo can write star here

def foo(a,b, *,c,d): #So every parameter of this star must  be keyword argument
    print(a,b,c,d)
    
foo(1,2,3,4)
# >>> TypeError: foo() takes 2 positional arguments but 4 were given 


#**********************************************
#So every parameter of this star must be keyword argument
def foo(a,b, *, c,d):
    print(a,b,c,d)
foo(1,2, c=3, d) #positional arguments cannot appear after keyword argument
# >>> SyntaxError: positional argument follows keyword argument



# **********************************************
def foo(a,b, *, c,d):
    print(a,b,c,d)

foo(1,2, c=3, d =4)
# >>> 1 2 3 4


# ********************************************
def foo(*args, c, d):
    print(c,d)
foo(1,2,3,d = 4)
# >>> TypeError: foo() missing 1 required keyword-only argument: 'c'    


# ********************************************
def foo(*args, c, d):
    print(c,d)
foo(1,2,3)
# >>> TypeError: foo() missing 2 required keyword-only argument: 'c'    


# ********************************************
def foo(*args, last):
    for arg in args:
        print(args)
    print(last)
foo(1,2,3)
# >>> TypeError: foo() missing 1 required keyword-only argument: 'last' 


# ********************************************
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)
foo(1,2,3,last=100)
# >>> 1
# >>> 2
# >>> 3
# >>> 100


# ********************************************
# so this how you can unforce to have only keyword argument
def foo(*args):
    for arg in args:
        print(arg)

foo(1,2,3)
# >>> 1
# >>> 2
# >>> 3



#**********************************************
###########################################
# Now lets talk about unpacking arguments
def foo(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
foo(my_list)
# >>> TypeError: foo() missing 2 required positional arguments: 'b' and 'c'


def foo(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
foo(*my_list)
# >>> 0 1 2

#*************************************
# it also work with tuple here
def foo(a,b,c):
    print(a,b,c)
my_list = (0,1,2)
foo(*my_list)
# >>> 0 1 2


#*************************************
# length of container must be match number of parameter
def foo(a,b,c):
    print(a,b,c)
my_list = (0,1,2,3)
foo(*my_list)
# >>> TypeError: foo() takes 3 positional arguments but 4 were given  


#***************************************
#Now if we have dictionary then it must have key with same name as your parameter name here
def foo(a,b,c):
    print(a,b,c)

my_dict = {'a':1,'b':2, 'c':3}
foo(**my_dict)
# >>> 1 2 3


# ***************************************
def foo(a,b,c):
    print(a,b,c)

my_dict = {'e':1,'b':2, 'c':3}
foo(**my_dict)
# >>> TypeError: foo() got an unexpected keyword argument 'e'


# ************************************************
#################################################
# Local vs global variable
def foo():
    x = number
    print('number inside function:', x)
    
number = 0
foo()
# >>> number inside function: 0



# *********************************************************
def foo():
    x = number
    number = 3 # this will do here creat a local variable that is now diffrent than this global variable(number = 0 )

    print('number inside function:', x)
number = 0 
foo()  # this will a raise error here bcz then
# >>> UnboundLocalError: local variable 'number' referenced before assignment



# *******************************************
# if we want to modified it then we have to first say global varible
def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)
    
number = 0
foo()
print(number)
# >>> number inside function: 0
# >>> 3


#*******************************************************
# what will happen if we don't write this global here
def foo():
    number = 3
number = 0
foo()
print(number)  
# >>> 0 (number here still zero here even after function call where we set number is equal 3)
# this is bcz we here craete a new local variable (number = 3) so this is nothing to do with gloabal variable and its only live inside function and not modified gloabal variable
# so if you want ot modified here global variable you have to write global a=variable here




#***************************************************
def foo():
    global number
    number = 3
    
number = 0
foo()
print(number)
# >>> 3


# *********************************************************
########################################################
############################ Parameter parsing

"""
* parameter parse is actualy reference to an object but reference is passed by value there is diffrence between mutable and unmutable data type

* mutuble object can be changed with in method
* if you rebind the reference in method then outer reference will still point orignal object.

"""

def foo(x): 
    x = 5 #Note here what happen "Var is integer this is immutable data type so it cant be changed an instead this will craete a local varible call x here (x = 5),  that is nothing to do with this (var = 10), this is the same with global and local variable diffrence so "
var = 10
foo(var)
print(var)
# >>> 10   :-this will stil prtint 10 even if we assign x is equal to 5 (x = 5), what happen here var is an integer this is an immutable type so it cant be change and instead this will create local a variable called x (x = 5) here.



def foo(a_list):
    a_list.append(4)
    
my_list = [1,2,3] #immutable integer in this list can be changed
foo(my_list)
print(my_list)
# >>> [1, 2, 3, 4]
# so mutable object can be modified within a function also immutubale object can be changed



def foo(a_list):
    a_list.append(4)
    a_list[0] = -100
    
my_list = [1,2,3] #immutable integer in this list can be changed
foo(my_list) # so this will change a global list here
print(my_list)
# >>> [-100, 2, 3, 4]



# but what is not possible here
# if we rebind mmutable refrence here
def foo(a_list):
    a_list = [200, 300, 400]  # this bcz we rebind the reference here, so this is now a local variable a list with this new value this is nothing to do again global variable
    a_list.append(4)
    a_list[0] = -100 # like here and if we rebind the reference in the method the outer refrence will not be changed
    
my_list = [1,2,3] #global list
foo(my_list)
print(my_list)
# >>>[1, 2, 3]

# mutable object can be changed immutable can not be changed but immutable object contain with a mutable object can be changed

# like here (a_list[0] = -100) and if we rebind the reference in the method the outer refrence (my_list = [1,2,3]) will not be changed 

def foo(a_list):
    a_list += [200, 300, 400]
my_list = [1,2,3]
foo(my_list)
print(my_list)
# >>> [1, 2, 3, 200, 300, 400]

# now my outer list or global list (my_list = [1,2,3]) got affected by this


def foo(a_list):
    a_list = a_list + [200, 300, 400]
my_list = [1,2,3]
foo(my_list)
print(my_list)
    # >>> my_list = [1,2,3]

#######################################################
# ************************************************* Notable points here
# the id function returns the unique identifier of the object, which can be used to check if two variables refer to the same object in memory.
a_list = [100, 200, 300]
id_before = id(a_list)
a_list += [400, 500, 600]
id_after = id(a_list)

print(id_before == id_after) 
# >>> Output: True
"""
The output of the code shows that the value of a_list remains the same after using the '+=' operator, which means that the same list object is being modified.

"""

a_list = [100, 200, 300]
id_before = id(a_list)
a_list = a_list + [400, 500, 600]
id_after = id(a_list)
print(id_before == id_after) 
# >>> Output: False

"""
The output of the code shows that the value of 'a_list' is now different, which means that a new list object has been created and assigned to 'a_list'.
"""

#So
"""
In Python, the id function is a built-in function that returns a unique identifier for an object. The identifier is an integer that is guaranteed to be unique and constant for this object during its lifetime. This can be useful for determining if two objects are the same or not, since two objects with the same identifier are guaranteed to be the same object in memory.
"""
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a)) # Output: 140733634479320
print(id(b)) # Output: 140733634479272

print(a == b) # Output: True
print(a is b) # Output: False


#################################################################
# *****************************************************
#### Asterisk Operator (*******************)
result = 5 * 7 # multiplication
print(result)
# >>> 35


result = 2**4 #power operation
print(result)
# >>> 16


zeros = [0] * 10
print(zeros)
# >>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


zeros = [0,1] * 10
print(zeros)
# >>> [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


zeros = "AB" * 10
print(zeros)
# >>> ABABABABABABABABABAB

# ***********************************
# next use * for args and kwargs
def foo(a,b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs: #Is dictionary
        print(key, kwargs[key]) #dictionary value
        
foo(1,2,3,4,5, six = 6, seven = 7)
# >>> 1
# >>> 3      
# >>> 4      
# >>> 5      
# >>> six 6  
# >>> seven 7


def foo(a,b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs: #Is dictionary
        print(key, kwargs[key]) #dictionary value
        
foo(1,2,3,4,5, six = 6, seven = 7)
# >>> 1 2
# >>> 3      
# >>> 4      
# >>> 5      
# >>> six 6  
# >>> seven 7


def foo(a,b, *, c): # mast item must be keyword argument
    print(a,b,c)
    
foo(1,2,3)
# >>> TypeError: foo() takes 2 positional arguments but 3 were given  


def foo(a,b, *, c):
    print(a,b,c)
    
foo(1,2,c = 3)
# >>> 1 2 3



#****************************************************
# We can also use astrisk for argument unpacking 
"""
The * operator is used to "unpack" the elements of an iterable (such as a list) into separate positional arguments. In this case, my_list gets unpacked into separate arguments a, b, and c for the function foo.
"""

def foo(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
foo(*my_list)
# >>> 0 1 2


#Otherwise
def foo(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
foo(my_list)
# >>> TypeError: foo() missing 2 required positional arguments: 'b' and 'c'


def foo(a,b, *, c):
    print(a,b,c)
    
foo[0,1,2]
# >>> TypeError: 'function' object is not subscriptable


def foo():
    return 42

print(foo()[0]) 
# >>> Raises TypeError: 'function' object is not subscriptable



def add(a, b):
    return a + b

print(add[0]) 
# >>> Raises TypeError: 'function' object is not subscriptable



def my_function():
    return [1, 2, 3]

result = my_function()
print(result[0]) 
# >>> Output: 1

# Trying to access an item in a function object
print(my_function()[0])
# >>> Raises TypeError: 'function' object is not subscriptable


"""
In Python, a "subscriptable type" is a type of object that can be indexed and accessed using square brackets ([]). The most common examples of subscriptable types are lists, tuples, and dictionaries.
"""
a_list = [1, 2, 3, 4, 5]
print(a_list[0]) # Output: 1
print(a_list[1]) # Output: 2
print(a_list[2]) # Output: 3
# >>> 1
# >>> 2
# >>> 3
    
"""
In general, any object that implements the __getitem__ method can be considered a subscriptable type in Python. The __getitem__ method allows an object to be indexed and accessed using square brackets.

"""

def foo(a,b,c):
    print(a,b,c)
    
my_dict = {'a':1, 'b':2, 'c': 3}
foo(**my_dict)



def foo(a,b,c):
    print(a,b,c)
    
my_dict = {'a':1, 'b':2, 'c': 3}
foo(*my_dict)
# >>> a b c
"""
However, this code will raise a TypeError because the * operator can only be used to unpack the elements of an iterable (such as a list or tuple), not a dictionary. Dictionaries are not iterable in the same way as lists or tuples.

To pass the values of the dictionary as separate arguments to the function, you can use the ** operator instead. This operator is used to unpack the key-value pairs of a dictionary into separate keyword arguments.
"""


def foo(a,b,c):
    print(a,b,c)
    
my_dict = {'e':1, 'b':2, 'c': 3}
foo(**my_dict)
# >>> TypeError: foo() got an unexpected keyword argument 'e'


# then the * is use for unpacking container so it can unpack element of list tuple sets into the single and remaing elements
numbers = [1,2,3,4,5,6]
*beginning, last = numbers
print(beginning)
print(last)
# >>> [1, 2, 3, 4, 5]
# >>> 6


# this is aways unpack your elements in list if i've a tuple here then unpacking work but it will still list here
numbers = (1,2,3,4,5,6)
*beginning, last = numbers
print(beginning)
print(last)
# >>> [1, 2, 3, 4, 5]
# >>> 6


numbers = (1,2,3,4,5,6)
beginning, *last = numbers
print(beginning)
print(last)
# >>> 1
# >>> [2, 3, 4, 5, 6]


numbers = (1,2,3,4,5,6)
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)
# >>> 1
# >>> [2, 3, 4, 5]  
# >>> 6



numbers = (1,2,3,4,5,6)
beginning, *middle, secondlast, last = numbers
print(beginning)
print(secondlast)
print(middle)
print(last)
# >>>1
# >>>5        
# >>>[2, 3, 4]
# >>>6        


# *******************************************
# we can also use "*" operator to merge iterable into the list
my_tuple = (1,2,3)
my_list = [4,5,6]
new_list = [*my_tuple, *my_list]
print(new_list)
# >>> [1, 2, 3, 4, 5, 6]


#*********** we can also use here set
my_tuple = (1,2,3)
my_set = {4,5,6}
new_list = [*my_tuple, *my_set]
print(new_list)
# >>> [1, 2, 3, 4, 5, 6]



# *********** we can also merge dictionary
dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
# >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}



# ***************************************************
########################################
# Shallow vs Deep Copying

# Assignment operater
org = 5
cpy = org
cpy = 6
print(cpy)
print(org)
# >>> 6
# >>> 5


# * but when we deal with mutable object
org = [0,1,2,3,4]
cpy = org # this does not make actual copy
cpy[0] = -10
print(cpy)
print(org)
# >>> [-10, 1, 2, 3, 4]
# >>> [-10, 1, 2, 3, 4]


####
org = [0,1,2,3,4]
cpy = org # this does not make actual copy
print(org)
cpy[0] = -10
print(cpy)
# >>> [0, 1, 2, 3, 4]
# >>> [-10, 1, 2, 3, 4]


"""
shallow copy: one level deep, only references of nested chuld objects 
deepcopy: full independent copy
"""

# ************************************************** shallow copy
import copy
org = [0,1,2,3,4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)
# >>> [-10, 1, 2, 3, 4]
# >>> [0, 1, 2, 3, 4]


#
import copy
org = [0,1,2,3,4]
cpy = org.copy()
cpy[0] = -10
print(cpy)
print(org)
# >>> [-10, 1, 2, 3, 4]
# >>> [0, 1, 2, 3, 4]


#
import copy
org = [0,1,2,3,4] # this work fine ifour element is only one level deep
cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)
# >>> [-10, 1, 2, 3, 4]
# >>> [0, 1, 2, 3, 4]


import copy
org = [[0,1,2,3,4], [5,6,7,8,9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)
# >>> [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
# >>> [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]


import copy
org = [[0,1,2,3,4], [5,6,7,8,9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)
# >>> [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]] 
# >>> [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]] # Orignal did not get affected

#so this diff b/w shallow and deep copy
# we can use this method also with list dict, tuple as well as custom object "clas"


import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person('Alex', 27)
p2 = p1

p2.age = 28
print(p2.age)
print(p1.age)
# >>> 28
# >>> 28

# Both got affected bcz this is not actual copy

#******************************************************
# But if we use swallow copy here 
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person('Alex', 27)
p2 = copy.copy(p1)

p2.age = 28
print(p2.age)
print(p1.age)

# >>> 28
# >>> 27

# orignal person did not get affected

# but again now if we have deep structre
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
            
p1 = Person('Alex', 57)
p2 = Person('joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
# >>> 56
# >>> 56


"""
This code defines two classes, "Person" and "Company".

The "Person" class has a constructor method __init__ which takes two parameters, name and age, and sets two attributes self.name and self.age to the corresponding parameter values.

The "Company" class also has a constructor method __init__ which takes two parameters, boss and employee, and sets two attributes self.boss and self.employee to the corresponding parameter values.

After defining these classes, the code creates two instances of the "Person" class, p1 and p2, with different name and age values.

Then, a new instance of the "Company" class, company, is created with p1 and p2 as its boss and employee attributes, respectively.

The code then uses the copy module to create a shallow copy of the company instance, which is stored in the company_clone variable.

A shallow copy is a new object which references the same data as the original object, but does not create new copies of the referenced objects. In this case, company_clone is a new instance of the "Company" class that has the same boss and employee objects as company.

Next, the age of the boss of the company_clone instance is updated to 56 by setting company_clone.boss.age to 56.

Finally, the code prints the age of the boss attribute of company_clone (which is 56) and the entire company instance, which includes the updated boss age value of 56.

To answer your other question, in this code company and company_clone are instances of the "Company" class, which is a type of object.
"""

import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
            
p1 = Person('Alex', 57)
p2 = Person('joe', 27)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
# >>> 56
# >>> 55

#So this is diffrence between shallow and deep copy
# *******************************************************
#################################################
########################### Context managers
#1st method (recommended way)
with open('notes.txt', 'w') as file:
    file.write('Some todooo...')

# Or
# secind method
file = open('nodes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close()
    
    
from threading import lock
lock = Lock()
lock.acquire()
# ....
lock.release() # never forget to realese if we use acwuire


with lock: # a better way to do this and also much simpler is with lock this automatically acquire our lock when we enter this
    pass
    


# now lets how we can implement contest manager in custem object(class) 
class ManagedFile():
    def __init__(self, filename):
        print('init')
        self.filename = filename
        
    def __enter__(self): #enter method
        print('enter') # here we want allocate our resource
        self.file = open(self.filename, 'w')
        return self.file #return allocated method
    
    def __exit__(self, exc_type, exc_value, exc_traceback): #exit method                                                
        if self.file: # if it is not none
            self.file.close()
            
        print('exit')
        
with ManagedFile('notes.txt') as file: #when our object is created inti method get called , so enteri sprinted so our resource got allocated "self.file = open(self.filename, 'w')"
    print('do some stuff...')
    file.write('some todoo....')
    
    
# >>> init
# >>> enter
# >>> do some stuff...
# >>> exit




class ManagedFile():
    def __init__(self, filename):
        print('init')
        self.filename = filename
        
    def __enter__(self): #enter method
        print('enter') # here we want allocate our resource
        self.file = open(self.filename, 'w')
        return self.file #return allocated method
    
    def __exit__(self, exc_type, exc_value, exc_traceback): #exit method                                                
        if self.file: # if it is not none
            self.file.close()
            print('exc:', exc_type, exc_value)
        print('exit')
        
with ManagedFile('notes.txt') as file: 
    print('do some stuff...')
    file.write('some todoo....')
print('continuing')
# >>> init
# >>> enter
# >>> do some stuff...
# >>> exc: None None             (No exception here exception value and exception type is None)
# >>> exit 
# >>> continuing 


#***************************************************
# Now if we try something that would not work
class ManagedFile():
    def __init__(self, filename):
        print('init')
        self.filename = filename
        
    def __enter__(self): #enter method
        print('enter') # here we want allocate our resource
        self.file = open(self.filename, 'w')
        return self.file #return allocated method
    
    def __exit__(self, exc_type, exc_value, exc_traceback): #exit method                                                
        if self.file: # if it is not none
            self.file.close()
            print('exc:', exc_type, exc_value)
        print('exit')
        
with ManagedFile('notes.txt') as file: 
    print('do some stuff...')
    file.write('some todoo....')
    file.somemethod()
print('continuing')

# >>> init
# >>> enter
# >>> do some stuff...
# >>> exc: <class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'somemethod'
# >>> exit
# >>> Traceback (most recent call last):
# >>> File "c:\VsCode\py4e\tempCodeRunnerFile.py", line 20, in <module>
# >>> file.somemethod()
# >>> AttributeError: '_io.TextIOWrapper' object has no attribute 'somemethod'



#* this raise exception its still conclose our file even if there is exception in this case attribute error then we can exit function we would not reach here "continue"
class ManagedFile():
    def __init__(self, filename):
        print('init')
        self.filename = filename
        
    def __enter__(self): #enter method
        print('enter') # here we want allocate our resource
        self.file = open(self.filename, 'w')
        return self.file #return allocated method
    
    def __exit__(self, exc_type, exc_value, exc_traceback): #exit method                                                
        if self.file: # if it is not none
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
            print('exc:', exc_type, exc_value)
        return True
        print('exit') # Note it doesnt printed
        
with ManagedFile('notes.txt') as file: 
    print('do some stuff...')
    file.write('some todoo....')
    file.somemethod()
    
# print('continuing')
# init
# enter
# do some stuff...
# Exception has been handled
# exc: <class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'somemethod'
# continuing\\
    
"""
his code defines a context manager called ManagedFile that opens a file in write mode when used in a with statement. The with statement is used to ensure that a resource is acquired and released in a controlled manner. The code under the with block executes while the file is open and once the block exits, the file is automatically closed.

When you use the with statement to create an instance of the ManagedFile class, the __enter__ method is called, and it returns the file object that is created by opening the specified file. Then, the block of code under the with statement is executed, which simply writes some text to the file. Finally, when the block of code completes, the __exit__ method is called, which closes the file.
"""
"""
Regarding the print('exit') statement inside the __exit__ method, it does not print anything because it is placed after the return statement. In Python, when a function encounters a return statement, it immediately exits the function and returns the specified value. Any code placed after the return statement will not be executed. Therefore, in this case, the print('exit') statement will never be executed.

"""


#*********
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f #this is a genrator this will first make sure allocate our resource then try to yeild our resource by yielding it will temporary suspend its own execution
    finally:
        f.close()
def open_managed_file('notes.txt') as f:
    f.write('some todooo.....')

my_list = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
my_list = [sorted(sublist, key=lambda x: x) for sublist in my_list]
print(my_list)
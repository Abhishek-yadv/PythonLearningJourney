######################################################
################################################
##### In Python Bodmas is remember left to right 
### Python for everybody
# Commond D for same selection

"""
when a function encounters a return statement, it immediately exits the function and returns the specified value.
Any code placed after the return statement will not be executed.
"""

"""
Code,Software,Program
A sequence of stored instructions;-
* it is a little piece of our intelligence in the computer
* WE figure something out and then we encode it and then give it to someone else to save them the time and energy of figurung it out

A piece of creative art;- 
* Particularly when we do a good job on user experience
"""

###############################
### Elements of python

"""
* Vacabulary/Words :- Variable and reserved words
* Sentence :- Valid syntax patterns
* Story structure :-constructing a program for a purpose

"""

##############################
### Reserved Words

"""
* You cannot use reserved wordsas variables names/ identifiers 
False    class     return     is       finally
None     if        for        lambda   continue
True     def       from       while    nonlocal
and      del       global     not      with
as       elif      try        or       yield 
assert   else      import     pass
break    except    in         raise

"""

############################
### Sentences or Lines

from lib2to3.pgen2 import literals


x = 2  # Assignment statement
x = x + 2 #Assignment with expression
print(x)  #Print statement

################################
### Python Script

"""
* Interactive python is good for experiments and programs of 3 - 4 lines long
* Most programs are much longer, so we type them into a file and tell python to run the commands in the fil.
* In a sense, we are "giving Python a script"
* As a convention, we are "giving python a script 
* As a convention, we add ".py" as the suffix on the end of these files to indicate they contain python.

"""

################################
### Interactive versus Script

"""
Interactive
* You type directly to python one line at a time and it responds

Script
* You enter a sequence of statements(lines) into a file using a text editor and tell python to execute the statements in the file
"""

#@
name = input("Enter file: ")
handle = open(name, 'r')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


################################
### Constants

"""
* Fixed values such as numbers, letters, and strings,are constant because their values does not change
* Numeric constant are as you except
* String constant use single quotes (') or double quotes (")

"""
print(123)
#>>> 123
print(98.6)
#>>> 98.6
print('Hello world')
#>>> Hello world


### Reserved Words

"""
* You cannot use reserved wordsas variables names/ identifiers 
False    class     return     is       finally
None     if        for        lambda   continue
True     def       from       while    nonlocal
and      del       global     not      with
as       elif      try        or       yield 
assert   else      import     pass
break    except    in         raise

"""

#########################################
### Variables

"""
* A Variable is a named place in the memory where a programmer can store data
*  -and later retrieve the data using the variables "name" .
* Programmers get to choose the names of the variables
* You can change the contents of a variable in a later statement

x = 12.2
y = 14
"""

#########################################
### Python variable Name Rules

""" 
* Must start with a letterr or underscore_
* Must consist of letters, numbers, and underscore_
* Case Sensitive

Good: Must start with a letterror underscore_
Ex: spam eggs spam23 _speed

Bad: Must consist of letters, numbers, and underscore_  
Ex: 23spam #sign var.12

Diffrent: Case Sensitive
Ex: spam Spam SPAM

"""

###########################################
### Mnemonic Variables Names:

# We name variables to help us remember what we intend to store in them("mnemonic" = "memory aid")

#exmmple
asdasdas = 23
sgsfdfd = 23.12
sadas = asdasdas + sgsfdfd
print(sadas)
a = 23
b = 23.12
c = a+b
print(c)

######################################
### Sentences or lines
x = 2     # Assignment statement
x = x + 2 #Assignment with expression
print(x)  #Print statement

# Variable  Operators  Constants  ReservedWord


##########################################
### Assignment Statements
"""
* We assign a value to a variable using the assignment statement(=)

* An assignment statement consists of an expression on the right - hand side and a variable to the store the result
x = 3.9 *x* (1-x)

"""


############################################
############################################
### Numeric Expressions
"""
* Because of the lack of mathmatical 
* Asterisk is multiplication
* Exponential looks diffrent than in math
    + Addition
    - Subtraction
    * Multiplication
    / Division
    ** power
    % reminders
"""
xx= 2
xx=xx+2
print(xx)
#>>>4

yy = 440 * 12
print(yy)
#>>> 5280

zz = yy/1000
print(zz)
#>>> 5.28

jj = 23
kk = jj%5
print(kk)
#>>>3

print(4*3)
#>>>12

############################
###Order of Evaluation

"""
* When we string operators toether - python must know which one to do first
* This is called "operator precedence"
* Which operator "takes precedence" over the others

"""

x = 1 + 2 * 3 - 4/5 ** 6


##############################################
#operator precedence Rules
"""
Highest precedencerule to lowest precedence rule:
* Parentheses are always respected        Parentheses
* Exponential(raise to power)             Power
* multiplication, Division, and Reminder  Multiplication
* Addition, Subtraction                   Addition
* Left to right                           left to right 
"""
x = 1 + 2 ** 3/4 * 5
print(x)
#>>>11
""" 1 + 2 ** 3/4 * 5
 =  1 + 8/4 * 5
 =  1 + 2 * 5
 =  11

"""

#####################################
###Type
# What does "type" Mean ?
"""
* In Python variables, literals, and constants have a "type"
* Python knows the diffrence between an integer number and a string
* for example "+" means "addition" if something is number and "concatenate" if something is a string

"""
"""
>>> Dic = 1 + 4
>>> print(Dic)
5

>>> eee = "hello " + "there"
>>> print(eee)
hello there
"""

################################
###Type Matters
"""
* Python knows what "type" everything is 
* Some operations are prohibited
* You cannot "add 1" to a string
* We can ask python what type something is by using the type() function 
>>> eee = "hello " + "there"
>>> eee = eee + 1
Traceback (most recent call last):
file "<stdin>", line 1, in
<module> TypeError: cannot convert 'int' object to str implicity

>>> type(eee)
<class 'str'>
>>> type('hello')
<class 'str'>
>>> type(1)
<class 'int'>

"""

################################
###Several Type of numbers

"""
* Numbers have two main types
* Integers are whole numbers:
    -14, -2, 0, 1, 100, 401233
* Floating numbers have decimal parts:
    -2.5, 0.0, 98.6, 14.0

* There are other number types - they are variations on float and integer
"""

"""
>>> xx = 1
>>> type(xx)
<class 'int'>

>>> type(temp)
<class 'float'>

>>> type(1)
<class 'int'>

>>> type(1.0)
<class 'float'>
"""

###################################
### Type conversions
"""
* When you put and integer and floating point in an expression,
*  -the integer is implicity converted to a float
* you can control this with the following built in function int() and float()

print(float(99)+100)
>>>199.0

i = 42
print(type(i))
>>><class 'int'>

f = float(i)
print(f)
42.0
print(type(f)
>>> <class 'int'>
"""

# Note :-Integer division produces a floating point result
print(10/2)
5.0
print(9/2)
4.5
print(99/100)
0.99
print(10.0/2.0)
5.0
print(99.0/100.0)
0.99

####################################
### String Conversions
"""
* You can also use int() and float() to convert between strings and integers
* You will get an error if the string does not contain numeric characters

"""
#@
sval = '123'
print(type(sval))
#>>> class 'str'>

print(sval + 1)
"""Traceback (most recent call last):
File "<stdin>", line1 in <module> 
TypeError: Cannot convert 'int' object to string implicity

"""
#@
ival = int(sval)
print(type(ival))
#>>> <class 'int'>
print(ival + 1)
#>>>124

#@
nsv = "hello bob"
niv = int(nsv)
"""Traceback (most recent call last):
File "<stdin>", line1 in <module> 
TypeError: Invalid literals for int() with base 10:'x' 
"""

##############################
### User input

"""
#* We can instruct python to pause and read data from the user the input() function

#* The input() function returns a string 
"""

#@
nam = input("Who are you? ")
print("I am ", nam)

##################################
### Converting user input
"""
#* I we want to read a number from the user, we must convert it from a string to a number using a type conversion function
#* Later we will deal with bad input data
"""
#@
inp = input("Europe floor?")
usf = int(inp) + 1
print('US floor', usf)


################################
### Comments in Python
"""
#* Anything after a # is ignored by Python
#* Why comment?
    * Describe what is going to happen in a sequence of code
    * Document who wrote the code or other ancillary information
    * Turn off a line of code - perhaps temporary

"""

# get the name of the file and open it
#@
name = input("Enter file: ")
handle = open(name, 'r')

# Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)


################################
################################
###  Conditional Steps
#@
# Program:               Output
x = 5
if x < 10:              
    print('smaller')    # smaller
if x > 20:
    print('Bigger')     
    
print('finish')          # finis


################################
### Comparison Operators

"""
#* Boolean expression ask a question aboutand produce yes or no results which we use to control program flow
#* Boolean expression using comparison operators evaluate to True/False or Yes/No results
#* Comparison operator look at variables but do not change the variables

<  Less than operator
<= Less tham or equal to operator
== Equal to
>= Greater than or equal
>  Greater than
!= Not equal
"""

################################
### Comparison operators
# One way Decision
x = 5
if x ==5:                #Before 5
    print('Is 5')        #Is 5
    print('Is Still 5')  # Is Still 5
    print('Thisrd 5')    # Third 5
print('Afterwards 5')    # Afterwards 5
if x ==6:                #Before 6
    print('Is 6')        #Is 6
    print('Is Still 6')  # Is Still 6
    print('Third 6')     #Third 6
print('Afterwards 6')    # Afterwards 6
    
    
################################
### Indentation
"""

#* Increase indent after an if statement or for statement(after:)
#* Maintain indent to indicate indente the scope of the the block(which lines are affected by the if/for)
#* Reduce indent back to the level of the if statement or for statement(after:) to indicate indicate the end of the block
#* Black lines are ignored - they do not affect indentation
#* Comments on a line by themselves are ignored with regard to indentation 

"""
#@
x = 5
if x > 2:
    print("Bigger thnan 2")
    print("Still bigger")
print("Done with 2")

for i in range(5):
    print(i)
    if x > 2:
        print("Bigger thnan 2")
    print("Done with i",i)
print("All done")

################################
#### Nested Decision
#@
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print("All done")


###########################################
### Two-way Decision with else:
##
x = 4
if x> 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')


########################################
######################Chapter 3
###Conditional Execution
#More conditional structure

### Multi-way Decision
#@
x = 5
if x < 2:
    print('Smaller')
elif x < 10:
    print("Medium")
else:
    print("Bigger")
print('All done')

####################################
### The try/Except Structure
"""
#* You surround a dangerous section of code with try and except .
#* if the code in the try works - the except is skipped
#* if the code in the try fails - the except- it jumps to the except section
"""
#@
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print("First",istr)

#@
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print("Second",istr)


###############################
#### try/except
#@
astr = "Bob"
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1
    
print("Done",istr)

###############################
#### Sample try/except
#@
rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1
    
#@
if ival > 0:
    print("Nice work")
else:
    print("Not a number")
    

#################################
#############################
#########################
#######Chapter 4 Functions
#We call these reusable pieces of code "Functions"
#@
def thing():
    print("Hello")
    print("Fun")
thing()  #Hello
        #Fun

print("Zip")
thing()  #Hello
        #Fun


################################
######### Python Functions
######

"""
#* There are two kinds of functions in python.
    *Builtin functions that are provided as part of python 
    #* Ex:- print(),input(),output(),float(),double(),int()
    
    *Functions that we define ourselves and then use
    
#* We treat the built-in functions as "new" reserved words words
    #* (Ex:- we avoid them as variable names)
    
"""

###############################
#############Functions Defiition
"""
#* In Python a function is some reusable code that takes arguments as input,
# *  -does some computation and then return a result or results

# * We define a function using the def reserved Word

#* We call/invoke the function by using the function name, parentheses, and arguments in an expression

"""
#@
big = max("Hello world")    #Argument is hello world

big = max("Hello world")
print(big)

tiny = min("Hello world")
print(tiny)


#####################################
####################
# A function is some stored code that we use. A functions tales some input and produces an output
# Max Functions
big = max("Hello world")
print(big)


###############################
###Type Conversions
"""
#* When you put an integer and floating point in an expression, the integer is implicity converted to a float.
#* You can control this with the built in functions int() and float()

"""
#@
print(float(99)/100)
# >>>0.99

#@
i = 42
type(i)
# >>> <class 'int'>

#@
f = float(i)
print(f)
# >>> 42.0

#@
type(f)
# >>> <class 'float'>

#@
print(1+2*float(3)/4)
#>>> -2.5


###############################
#########string conversions
"""
#* You can also use int() and float() to convert between strings and integers.
#* You will get an error if the string does not contain numeric characters.

"""
#@
sval = '123'
print(type(sval))
#>>> <class 'str'>
print(sval + 1)
"""traceback (most recent call last):
File "<stdin>", line1, in <module>
TypeError: cannot concatenate stringsand "int"
"""
#@
ival = int(sval)
print(type(ival))
# >>> <class 'int'>
print(ival + 1) 
# >>> 124

#@
nsv = 'hello bob'
niv = int(nsv)
"""
Traceback (most recent call last):
File "<stdin>", line1, in <module >
ValueError: invalid literals for integers
"""

###############################
###########Functions 

### Building our own functions
"""
#* We create a new function using the def keyword followed by optional parameters in parentheses.
#* We indent the body of the function
#* This defines the function but does not execute the body of the function 

"""
#@
def print_lyrics():
    print("I'am a lumberjack, and I'm okay.")
    print('I seep all night and i work all day.')


x = 5
print("Hello")
def print_lyrics():
    print("I'am a lumberjack, and I'm okay.")
    print("I sleep all night and i work all day.")
    
print('Yo')
x = x + 2
print(x)

################################
#########################
#Definations and uses
"""
#* Once we have defined a function, we can call(or invoke) as many times as we like
#* This is the store and reuse pattern

"""
x = 5
print("hello")

def print_lyrics():
    print("I'm a lumberjack, and i'm okay.")
    print("I sleep all night and i work all day ")
    
print("yo")
print_lyrics()
x = x + 2
print(x)

# >>>hello
# >>>yo
# >>>I'm a lumberjack, and i'm okay.      
# >>>I sleep all night and i work all day 
# >>>7


################################
############Arguments
"""
#* An arguments is a value we pass into the functionas its input when we call the function
#* We use arguments so we can direct the function to do diffrent kinds of work when we call it at diffrent times
#* We put the arguments in parentheses after the name of the function
"""
bog = max("Hello word")  # Here hello word is the Arguments


################################
############ Parameters
"""
#* A parameter is a variable which we use in the function definition.
    #*it is a "handle" that allows the code in the function to access the arguments for a particular function invocation.
"""

def great(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print("Hello")
great('en')
great('es')
great('fr')
# >>>Hello
# >>>Hola   
# >>>Bonjour

##############################
#@ Return Value
"""
Often a function will take its arguments, do some computation and return a value,
to be used as the value of the function call in the calling expression. the return keyword is used for this.

"""
def greet():
    return("hello")
print(greet(),"Abhishek")
print(greet(),"Sally") 


##############################
#@ Return Value
"""
#* A "fruitful" function is one that produces a results(or return values) of
#* The return statement ends the function execution and "send back" the result of the function.
"""

def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'Bonjar'
    else:
        return 'hello'
print(greet('en'),"Glenn")  
# >>> Hello Glenn
print(greet('es'),"Sally")
# >>>Hola Sally    
print(greet('fr'),"Michael")
# >>>Bonjour Michael


##############################
#@ Multiple Parameters/Arguments

"""
#* We can define more than one parameter in the function definition
#* We simply add more arguments when we call the function
#* We match the number and order of arguments and parameters

"""

def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print(x)

#@ VOID(non-fruitful) Functions
"""
#* When a function does not return a value, we call it a "void"(non fruitful) function
#* Functions that return values are "fruitful" functions
#* Void functions are "not fruitful"

"""


#@To function or not to function
"""
#* Organize your code into "paragraphs" - capture a complete thought and "name it
#* Don't repeat yourself- make it works once and them reuse it
#* if something gets too long or complex, breaks it up into logical chunks and put those chunks in functions
#* make a library of common stuff that you do over and over- perhaps share this with your friends...
# """

################################
####Loops and iteration
#Chapter 5 

#@ Repeated Steps
# Program:
n = 5             #5            
while n > 0:      #4                 
    print(n)      #3            
    n = n - 1     #2                     
                  #1   
print("Blast off")                                 
print(n)          #0      


"""
Loops (repeated steps) have iteration variables change each time through the loop.
Often these iteration variables go through a sequence of numbers.

"""

#@ An infinite loop
n = 5
while n > 0:
    print("lather")
    print("Rinse")
print("Dry off")

#@ Breaking Out of loops
"""
#* The break statement ends the current loop and jumps to the statement immediately following the loop
#* it is a like a loop test that can happen anywhere in the body of loop
"""

while True:                    # >>>hello there
    line = input('>')          # hello there         
    if line == 'done':         # >>>finished    
        break                  # finished
    print(line)                # >>> done
print("Done!")                 # Done!


##########################################
### Finishing an iteration with continue
"""
The continue statement ends the current iteration and jumps to top of the loop and starts the next iteration.

"""
while True:
    line = input('> ')
    if line[0] =='#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
    
#@ Indefinite loop
"""
#* while loops are called "indefinite loops" because they keep going untill a logical condition becomes False

#* The loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be "infinite loops"

#* Sometimes it is a little harder to be sure if a loop will terminate
"""

###########################################
################### Loops and iteration
#@ Definate loop

"""
#* Quite often we have a list of items of the line in a file effectively a finite set of things
#* We can write a loop to run the loop once for each of the items in set using the python for construct
#* these loops are called "definite loops" because they exist an exact number of times
#* we say that " define loops iterate through the members of a set
"""

#@ A Simple Definite Loop
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')

"""
Definite Loop(for loops ) have explicit iteration variables that change each time through a loop.
these iteration variables are move through the sequence of set. 

"""

#@ A Definite Loop with string
friends = ['Joseph', 'Glenn', 'Selly']
for friend in friends:
    print("Happy new year:",friend)
print("Done")

########################################
##############################
## Looking at word "In"
"""

#* The iteration variable "iterates" through the sequence of words(ordered set)
#* The block(body) of code is executed once for each value in the sequence
#* The iteration variable moves through all of the values in the sequence in the sequence

"""

for i in [5,4,3,2,1]: #here i is iteration variable
    print(i)
    
##############################
#### Loops idioms:
#### What we Do in Loops
# Note: Even though these examples are simple the patterns apply to all kinds of loops.


##############################
## Chapter 5
#Loops and iteration(Loops idioms)
"""
The trick is "knowing" something about the whole loop
when you are stuck writing code
that only sees one entry at a time
"""

"""
Set some variables initial values

for thing in data:

look for something or do something to each entry separately updating a variable

Look at the variables
"""

#@ Looping through a set
print('before')
for i in [9,41,12,3,74,15]:
    print(thing)
print('After')

#@ What is largest Numbers
largest_so_far = -1
print("Before",largest_so_far)    #Before         
for the_num in [9,41,12,3,74,15]:  #9 9         
    if the_num > largest_so_far:   #41 41            
        largest_so_far = the_num   #41 12         
    print(largest_so_far, the_num) #41  3            
                                   #74  74

print('After', largest_so_far)     #74  15
                                   #After 74

"""
We make a variable that contains the largest value we have seen so far.
if the current number we are looking at is larger, it is the new largest value we have seen so far.

"""

##############################
## Loops and iteration(More Loops Patterns
zork = 0
print('Before',zork)
for thing in [9,42,12,3,74,15]:
    zork += 1
    print(zork, thing)
print('After',zork)
"""
>>> Before 0
>>> 1 9
>>> 2 42
>>> 3 12
>>> 4 3
>>> 5 74
>>> 6 15
>>> After 6
"""
"""
To add up a value we encounter in a loop, we introduce a sum variable start at 0 and we add the value
to the sum each time through the loop.
"""

#@ Finding the Average in a Loop
count = 0
sum = 0
print('Before', count,sum)
for value in [9,41,12,3,74,15]:
    count+=1
    sum = sum + value
    print(count,sum,value)
print('After', count,sum, sum/count)

"""
>>>1 9 9     
>>>2 50 41   
>>>3 62 12   
>>>4 65 3    
>>>5 139 74  
>>>6 154 15
After 6 154 25.666666666666668
"""

# An average just combines the counting and sum patterns and divides when the loop is done. 

#@ Filetering in a loop
print('Before')                   # Before   
for value in [9,41,12,3,74,15]:     
    if value > 20:                   # Large number 41
        print('Large number', value) # Large number 74   
print('After')                       # After

#@ we use an if statement in the loop to catch/filter the values we are looking for.


#@ Searching Using a Boolean
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

# >>> Before False
# >>> False 9     
# >>> False 41    
# >>> False 12    
# >>> True 3      
# >>> True 74     
# >>> True 15
# >>> After True


#@
found = False
print('Before',found)
while found == False :
    for value in [9,41,12,3,74,15]:
        if value == 3:
            found = True
            print(found,value)
            break
        print(found,value)
print('After',found)


#@ How to find the smallest value
smallest_so_far =-1
print('Before',smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num < smallest_so_far :
        smallest_so_far = the_num
        print(smallest_so_far,the_num)

print('After',smallest_so_far)

""" 
#* >>> Before -1
#* >>> After -1
"""

#@ Finding the smallest value
smallest_so_far =-1
print('Before',smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num < smallest_so_far :
        smallest_so_far = the_num
        print(smallest_so_far,the_num)

print('After',smallest_so_far)
""" 
#* >>> Before -1
#* >>> After -1
"""

################################
# None type has only one number 
# None is constant and often used to indicate empty
"""
"is" is stronger than equal sign

"""
smallest = None
print('Before')
for value in [3,41,12,9,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print('After',smallest)
"""
#* >>>Before
#* >>>3 3 
#* >>>3 41
#* >>>3 12
#* >>>3 9 
#* >>>3 74
#* >>>3 15
#* >>>After 3
"""
############################################
#### The "is" and "is not" Operators 
"""
#* Python has an is operator that can be used in logical expressions
#* implies "is the same as"
#* Similar to, but stronger than ==
#* "is not" also is a logical operator operator
#* "is" is stronger than == operator
"""

smallest = None
print('Before')
for value in [3,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
    
    
print('After',smallest)


################################
###################Chapter 6
########### String

"""
#* A string is a sequence of characters
#* A string literals uses quotes 'hello' or "Hello"
#* For string, means "concatenate"
#* when a string contains numbers, it is still a string
#* We can convert numbers in a string into a number using int()

"""
str1 = "hello"
str2 = "world"
bob = str1 + str2
print(bob)
# >>> Hello World

str3 = '123'
str3 = str3 + 1
print(str3)
"""Traceback (most recent call last):
File "<stdin>", line1 in <module>
TypeError: cannot concatenate 'str' and 'int' objects
"""
x = int(str3) + 1
print(x)
# >>>124

################################
#@  Reading and Converting
"""
#* We prefer to read data in using string and then parse and convert the data as we need
#* This gives us more control over error situations and/or bad user input
#* Raw input numbers must be converted from strings
"""
#@
name = input('Enter: ')   # Enter : Chuck
print(name)
# >>> Chuck

#@
apple = input('Enter: ') # Enter:100
x = apple - 1
print(x)
"""
Traceback (most recent call last):
File "<stdin>", line1 in <module>
TypeError: unsupperted operand type(s) for -: "str" and 'int'
"""
#@
apple = input('Enter: ') # Enter:100
x = int(apple) - 10
print(x)
# >>>90

#@ Looking inside Strings

"""
#* We can get at any single characters in a string using an index specification in square brackets
#* The index value must be integer and start with 0
#* The index value can be an expression that is computed

"""

#@
fruit = 'banana'
letter = fruit[1]
print(letter)
# >>>a

#@
fruit = 'banana'
x = 3
w = fruit[x-1]
print(w)

# A Character Too Far
"""
#* You will get a python error if you attempt to index beyond the end of a string .
#* So be careful when constructing index values and slices
"""
zot = 'abc'
print(zot[5])
"""
Traceback (most recent call last): File "<stdin>",line 1, in <module>
IndexError: string index out of range
"""

##############################
#@ String Have Length
#* the built-in function len gives us the length of a string .

fruit = 'banana'
print(len(fruit))
# >>>6

############################
#@ Len Function
"""
A function is some stored code that we use. A function takes some input and produces an output. 
"""

fruit = 'banana'
x = len(fruit)
print(x)
# >>>6

################################
###Looping through strings

"""Using a while statement and an iteration variable,
and the len function, we can construct a loop to look at each of the letters in a string individually"""

fruit = 'banana'
index = 0
while index< len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index + 1

#@ Other way define loop (Second loop)
"""
* A definite loop using a for statement is more elegent
* the iteration variable is completely taken care of by the for loop

"""
fruits = 'banana'
for letter in fruits:
    print(letter)

#or
index = 0
while index< len(fruit):
    letter =fruit[index]
    print(letter)
    index+=1


#@ Looping and counting
"""
This is a simple loop that loops through each letter
in a string and counts the number of times the loop encounters the 'a' character.
"""

word  = 'banana'
count = 0
for letter in word:
    if letter == "a":
        count +=1
print(count)


################################
#@ Looking deeper into "in"
"""
* The iteration variable "iterates" through the sequence (ordered set)
* The block (body) of code is executed once for each value in the sequence
* The iteration variable moves through all of the values in the sequence
"""
# iteration variable here is letter 
for letter in 'banana':
    print(letter)
    
"""
* the iteration variable "iterates" through tha string and the block of code,
*- is executed once for each value in the sequence

"""
#####################################
################ Chapter 6 (String)
#More strings operations

#@ Slicing String
"""
* We can also look at any continuous section of a string using aclon operator
* The second number is one beyond the end of the slice- "up to but not including"
* First number is included
* if the second number is beyond the end of the string, it stops at the end .

"""

s = 'Monty Python'
print(s[0:4])
# >>> mont

print(s[6:7])
# >>> p

print(s[6:20]) # it did not given traceback decided to stop in last
# >>> Python

print(s[:2])
# >>> Mo

print(s[8:])
# >>>thon

print(s[:])
# >>> Monty Python

###############################
# String Concatenation
"""
When the + operator is applied to string , it means "concatenation"

"""
a = "Hello"
b = a + "There"
print(b)
#>>> HelloThere

c = a + ' ' + 'There'
print(c)
#>>> Hello There


###################################
#@ Using in as a logical Operator
"""
* The in keyword can also be used to check to see if one string is "in" another string
* The "in" expression is a logical expression that returns True or False and can be used in an "if" statement
"""
#@ 
fruit = 'banana'
'n' in fruit
True

#@
'm' in fruit
False

#@ 
'nan' in fruit
True

#@
if 'a' in fruit:
    print('Found it')
# >>> Found it

#@
fruits = "banana"
if 'n' in fruits:
    print("Yes")
else:
    print("Not available")
# >>> yes

#@
fruits = "banana"
if 'j' in fruits:
    print("Yes")
else:
    print("Not available")
# >>> Not available


###########################
#@  String comparison
if word == 'banana':
    print('All right, bananas ')
    
if word < 'banana':
    print('Your word,' + word +', comes before banana')
elif word > 'banana':
    print('Your word,' + word +', comes before banana')
else:
    print('All right, bananas.')
    
################################
#@ String Library
"""
#* Python has a number of string function which are in the string library
#* These functions are already built into every string - we invoke them by
#* -  appending the function to the string variable
#* These functions do not modify the original string, instead they return
#* - a new string that has been altered
"""

#@
great = 'Hello Bob'
zap = greet.lower()
print(zap)
# >>>hello bob

#@
great = 'Hello Bob'
print(great)
# >>> Hello bob

print("Hi There")

#############################
#@ 
stuff = "Hello world"
type(stuff)
#>>> <class 'str'
dir(stuff)
['capitalize','casefold','center','count','encode','endswith','expandtabs','find','format','format_map','index','isalnum','isalpha','isdecimal',
    'isdigit','isidentifier','islower','isnumeric','isprintable','isspace',
    'istitle','isupper','join','ljust','lower','lstrip',
    'maketrans','partition','replace','rfind','rindex','rjust',
    'rpartition','rsplit','rsrtip','split','splitlines',
    'startwith','strip','swapcase','title','translate','upper','zfill']

stuff = 'Hello world   '
print(stuff.rjust)

#@ Some important string method
""" str.capitalise(),
str.center(width[, fillchar])
str.endswidth(suffix[,start[,end]])
str.find(sub[,start[,end]])
str.lstrip([chars])
str.replace(old,new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()
"""

#@ Searching a String

#* We use the find( ) function to search for a substring within another string
#* find() finds the first occurrence of the substring
#* if the substring is not found, find() returns -1
#* Remember that string postion starts at zero 

#@
fruit = 'banana'
pos = fruit.find()
print(pos)
# >>>2

#@
aa = fruit.find()
print(aa)
# >>>-1

#@ Making everything UPPER CASE
#* You can make a copy of a string in lower case or upper case
#* Often when we are searching for a string using find() we first convert the string to lower case so we can search a string regardless of case

great = 'Hello Bob'
nnn = greet.upper()
print(nnn)
# >>> HELLO BOB

www = greet.lower()
print(www)
# >>> hello bob

###############################
### Search and Replace
#* The replace() function is like a "search and replace" operation in a word processer
#* it replaces all occurrences of the search string with the replacement string

#@ 
greet = 'Hello bob'
nstr = greet.replace('Bob')
print(nstr)
# >>> Hello jane
nstr = greet.replace('o','x')
print(nstr)
# >>> Hellx bxb

#@ Stripping Whitespace
#* Sometimes we want to take a string and remove whitespace at the beginning and/or end
#* lstrip() and rstrip() remove whitespace at the left or right
#* strip() removes both beginning and ending whitespace

#@
greet = "  Hello Bob   "
greet.lstrip()
# >>>"  Hello Bob   "

#@
greet = "   Hello Bob  "
greet.rstrip()
# >>> '  Hello Bob'

#@ 
greet = "  Hello Bob  "
greet.strip()
# >>> "Hello Bob"


#################################
#@ Prefixes
line = " Please have a nice day "
line.startswith('Please')
# >>> True

line.startswith('p')
# >>> False


#################################
#@ Parsing and extracting

data = 'From stephan.marquard@uct.ac.za. Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# >>> 21

sppos = data.find('',atpos)
print(sppos)
# >>> 31

host = data[atpos+1 : sppos]
print(host)
# >>> uct.ac.za



##################################
############### Chapter 7
### Reading File

#@ File processing
#* A text file can be thought of as a sequence of lines


#@ Opening A File
"""
* Before we can read the contents of the file, we must tell Python which file
*    -we are going to work with and what we will be doing with the file
* This is done with the open() function
* Open() returns a "File handle" - a variable used to perform operations on the file
* Similar to "File -> Open" in a Word Processor

"""

#################################
#@ Using open()
#* handle = open(filename, mode)
#* returns a handle use to manipulate the file
#* filename is a string
#* mode is optional and should be "r" if we planning to read the file and "w" if we are going to write to the file


#@ What is a Handle
fhand = open('mbox.txt')
print(fhand)

#@ When Files are missing
fhand = open('stuff.txt')
"""
Traceback(most recent call last): 
    File "<stdin>", line1, in <module>
    FileNotFoundError: [Error 2] No such file or directory: 'stuff.txt'
    
"""

##################################
###########The newline character
"""
* we use a special character called the "newline" to indicate when a lin 
* We represent it as \n in strings
* newline is still one character
"""
#@
stuff = 'Hello\n world'
print(stuff)
# >>> Hello
# >>> World!

#@
stuff = 'X\nY'
print(stuff)
print(len(stuff))
"""
>>> X
>>> Y
>>> 3
"""

##############################
###########File Precessing
#* A text file can be thought of as a sequnce of line
#* A text file has newlines at the end of each line


###############################
###### Reading Files
#Reading Files in python
"""
* A file handle open for read can be treated as a sequence
*  -of string where each line in the file is a string in the sequence.
* We can use the for statement to iterate through a sequence
* Remember -a sequence is an ordered set.
"""

#@
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
    

#####################################
#@ Counting lines in a files
"""
* open a file read - only
* Use a for loop to read each line
* Count the lines and print out the number of lines
"""

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count', count)

####################################
#@ Reading the *Whole* File 
"""
* We can read the whole file(newlines and all) into a single string .
"""

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
# >>> 94626
print(inp[:20])
# >>> mbox-short.txt


##################################
####@ Searching through a file
#* We can put an if statement in our for loop to only print lines that meet some criteria

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith("From "):
        print(line) #Here print function add a new line at the end of line
"""
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

>>> From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008

>>> From zqian@umich.edu Fri Jan  4 16:10:39 2008

>>> From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
...
...
"""



#############################
#####Searching Through a File(Fixed)
"""
* We can strip the whitespace from the right-hand side of the string using rstrip() from the string library
* The newline is considered "white space" and is stripped
"""
#@
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
"""
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
>>> From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
>>> From zqian@umich.edu Fri Jan  4 16:10:39 2008
>>> From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
"""

#####################################
#@ Skipping with continue
""" 
* We can conveniently skip a line by using the continue statement
"""
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    print(line)
"""
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
>>> From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
>>> From zqian@umich.edu Fri Jan  4 16:10:39 2008
>>> From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
....
....
"""

#######################################
#@ Using "in" to select lines
"""
* We can look for a string anywhere "in" a line as our selection criteria
"""
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)
"""
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
>>> From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
>>> From zqian@umich.edu Fri Jan  4 16:10:39 2008
>>> From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
"""

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject: "):
        count = count + 1
print("There were ",count,"Subject lines in", fname)
"""
>>> Enter the file name: mbox.txt
>>> There were 1797 Subject lines in mbox.txt
"""

#@ Handling Bad file
fname = input("Enter the fname: ")
try:
    fhand = open(fname)
except:
    print("File cannot be open: ")
    quit()

count = 0
for line in fhand:
    if line.startswith("Subject"):
        count = count + 1
    print(line)
    
##################################
### Chapter 8
# * Algoriths : - A set of rules or steps used to solve a program
# * Data Structures:- A particular way of organizing data in a computer

#@ What is not a "Collection"
"""
* Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten.
""" 

# $Python
x = 2
x = 4
print(x)
# >>>4
    
##############################
#@ What is collection
"""
* A collection allows us to put many values in a single "Variable"
* A collection is nice because we can carry all many values around in one convinient package
"""

Friends = ["Joseph", "Glenn", 'Sally']
carryon = ["socks", "shirt", "perfect"]

#########################
### List Constants
"""
* List constant are surrounded by square brackets and element in the list is seprated by comma
* A list element can be any python object - even another list
* A list can be empty
"""
print([1,24,76])
# >>> [1,24,76]

print(["red","yellow","Blue"])
# >>> ["red","yellow","Blue"]

print(["red","24","98.6"])
# >>>["red","24","98.6"]

print([1,[5,6],7])
# >>>[1,[5,6],7]

print([])
# >>>[]

#@ We already use list
for i in [5,4,3,2,1]:
    print(i)
print("Blastoff")


#Lists and definite loops - best pals
friends = ["Joseph", "Glenn","Sally"]
for friend in friends:
    print("Happy New Year: ",friend)
print('done')
"""
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
"""

z = ["Joseph","Glenn","Sally"]
for x in z:
    print("Happy New Year: ",x)
print("Done!")

#@ Looking inside Lists
#* Just like strings, we can get at any single element in a list using index specified in square brakets

friends = ["Joseph","Glesnn","Sally"]
print(friends[1])
# >>> Glenn

############################
### Liasts are Mutable(Changable)
"""
* Strings are " immutable" - we cannot change the contents of a string - we must make a new sstring to make any change
* Lists are "mutable" - we can change an element of a list using the index operator
"""

fruit = "Banana"
fruit[0] = "b"
"""
Traceback
TypeError: "str" object does not support item assignment
support item assignment
"""

#@
x = fruit.lower()
print(x)
# >>> Banana

#@
lotto = [2,14,26,41,63]
print(lotto)
# >>>[2,14,26,41,63]

#@
lotto[2] = 28
print(lotto)
# >>>[2,14,28,41,63]

################################
#@ How long is a list
"""
* The len() function takes a list as a parameters and returns the number of elements in the list
* Actually len() tells us the number of elements of any set or sequence(Such as a string....)
"""
greet = "Hello Bob"
print(len(greet))
# >>>9

x = [1,2,"j"]
print(len(x))
# >>>4

##########################
##Using the range function
"""
* The range function returns a list of numbers that range from zero to one less than the parameter
* We can construct an index loop using for and an integer iterator
"""
#@
print(range(4))
# >>> [0,1,2,3]


#@
friends = ["Joseph", "Glenn","Sally"]
print(len(friends))
# >>> 3

#@
friends = ["Joseph", "Glenn","Sally"]
print(range(len(friends)))
# >>>[0,1,2]

#@ A tale of two loops
friends = ["Joseph","Glenn","Sally"]
for friend in friends:
    print("Happy new Year:", friend)

for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year:",friend)
    
##################################
################# Chapter 8(Lists)
#@ Loop operations
# Concatenating lists using +
"""
* We can create a new list by adding two existing lists together
"""
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# >>>[1,2,3,4,5,6] 
print(a)
# >>>[1,2,3]

#@ Concatenating lists using
#* We can create a new list by adding two existing lists together
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# >>> [1,2,3,4,5,6]

print(a)
# >>> [1,2,3]


#@ Lists can be sliced using ":"
t = [9,41,12,3,74,15]
print(t[1:3])
# >>> [41,12]
print(t[:4])
# >>>[9,41,12,3]
print(t[3:])
# >>> [3,74,15]
print(t[:])
# >>> [9,41,12,3,74,15]

"""
#* Remember: Just like in strings, the second number is "up to but not including"
"""
#@ List Method
x = list()
print(type(x))
# >>> <type 'list'>
print(dir(x))
"""
['__add__', '__class__', '__class_getitem__', '__contains__',
'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__',
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
'__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'clear', 'copy', 'count',
'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

"""
#* Some important method regarding list
["append", "count","extend","index","insert",
"pop","remove","reverse","sort"]
"""

#####################################
#@ Building a List from Scratch
"""
* We can create an empty list and then add elements using the append method
* The list stays in order and new elements are added at the end of the list
"""

#@
stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
#>>> ["book",99]

#@
stuff = list()
stuff.append("cooking")
print(stuff)
#>>> ["Book","99","cookie"]

############################
#@ Is something in a list ?
"""
* Python provides two operators that let you check if an item is in a list
* These are logical operators that return True or False
* They do not modify the list
"""

some = [1,9,21,10,16]
print(9 in some)
# >>> True

print(15 in some)
# >>> False

print(20 not in some)
# >>> True

################################
#@ Lists are in Order
"""
* A lists can hold many items and keeps those items in the order,
* -until we do something to change the order
* A list can be sorted (i.e. change its order)
* The sort method(unlike in strings) means "sort yourself"
"""
friends = ["Joseph","Glenn","sally"]
friends.sort()
print(friends)
# >>> ["Glenn","Joseph","Sally"]
print(friends[1])
# >>> Joseph


##################################
#@ Built-in functions and Lists
"""
* There are a number of functions built into python that take lists as parameters
* Remember the loops we built?  These are much simpler
"""
#@
nums = [3,41,12,9,74,15]
print(len(nums))
# >>> 6

#@ 
nums = [3,41,12,9,74,15]
print(max(nums))
# >>> 74

#@
nums = [3,41,12,9,74,15]
print(min(nums))
# >>> 3

#@
nums = [3,41,12,9,74,15]
print(sum(nums))
# >>> 154

#@
nums = [3,41,12,9,74,15]
print(sum(nums)/len(nums))
# >>> 25.6

#@ 
total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count
print("Average: ",average)

#@
numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print(average)


#@
import random
numlist = list()
count = 0
while True:
    num = random.randint(1,10003228294642443)
    numlist.append(num)
    count = count + 1
    if len(numlist) == 100000: break
    average = sum(numlist)/count
print("Average",average)
    
###################################
#@ Chapter 8(Strings vs Lists)
## Best Friends: Strings and Lists
abc = "With three words"
stuff = abc.split()
print(stuff)    
# >>> ["With","three","words"]
print(len(stuff))
# >>> 3
print(stuff[0])
# >>> With

"""
* Split breaks a string into parts and produces a list of strings. We think of these as words. 
* -We can access a particular word or loop through all the words
For ex:-
"""
#@
abc = "With three words"
stuff = abc.split()
print(stuff)
for w in stuff:
    print(w)
"""
>>>
["with","three","words"]
wtih
three
words
"""

abc = "With three words"
stuff = abc.split()
print(stuff)
# >>>["With","three","words"]
print(len(stuff))
# >>> 3
print(stuff[0])
# >>> With

"""
* Note:- In split when you don't specify a delimeter, multiple spaces are treated like one delimeter
* We can even specify which delimeter character use in the spliting
"""
#@
line = "A lot    of spaces"
etc = line.split()
print(etc)
# >>>["A","lot","of","spaces"]

#@
line = "first;second;third"
thing = line.split()
print(thing)
# >>>['first;second;third']
print(len(thing))
# >>> 1



#@
line = "first;second;third"
thing = line.split(";")
print(thing)
print(len(thing))
# >>> 3

#* Split jobs is used to spaces and split the string based in spaces
#* - but we can even decide delimeter for spliting

#
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    print(words[2])
"""
>>> Sat
>>> Fri
>>> Fri
>>> ...
>>> ...
>>> ...
>>> Thurs
"""
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
words = line.split()
print(words)
# >>> ["From", "stephen.marquard@uct.ac.za","Sat", "Jan","5","09:14:16", "2008"]


####################################
#@ The Double Split Pattern
"""
#* Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again 
"""
#@
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])

################################
###### Chapter 8(Lists)
#@ String, Files, LIsts and the Guardian pattern

#@
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    words = line.split()
    print(words)
    if words[0] != "From":
        continue
    print(words[2])
    
#@
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    words = line.split()
    print("Words: ",words)
    if words[0] !="From":
        print("Ignore")
        continue
    print(words[2])
    

#@
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    print(line)
    words = line.split()
    if len(words) <1:
        continue
    if words[0] !="From":
        print("Ignore")
        continue
    print(words[2])
    
"""
* Note:- There is diffrence in "" and " "
"""
#@
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line == '':
        print("Skip Blank")
        continue
    words = line.split()
    print("Words:", words)
    if words[0] != "From":
        print("Ignore")
        continue
    print(words[2])


#@ 
fhan = open("mbox-short.txt")
for line in fhan:
    line = line.rstrip()
    words = line.split()
    #guardian
    if len(words) < 1:
        continue
    if words[0] != "From":
        continue
    print(words[2])

#@
fhan = open("mbox-short.txt")
for line in fhan:
    line = line.rstrip()
    words = line.split()
    # guardian a bit stringer
    if len(words) < 3:
        continue
    if words[0] != "From":
        continue
    print(words[2])
"""
Sat
Fri
Fri
..
..
Thurs
"""

#@
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != "From":
        continue
    print(words[2])
        
        
#################################
#################
########## Chapter 9(Dictionary)

#@ What is collection
"""
* A collection is nice because we can put more than one value and carry them all around in one convenient package
* We have a bunch of values in a single "variable"
* We do this by having more than one place "in" the variabe
* We have ways of finding the diffrent places in the variable
"""

#@ What is not a "Collection"?
#* Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten .
# Python
x = 2
x = 4
print(x)
# >>>4

############################
# A Story of two collections
"""
* List:-
        A linear collection of values that stay in order
* Dictionary:-
            A "Bag" of value, each with its own label

"""

"""
* Dictionaries:
* Dictionaries are python's most powerfull data collection
* Dictionaries allows us to do fast database- like operations in python
* Dictionaries have diffrent names in diffrent languages
    * Associative Array - Perl/PHP
    * Properties or Map or Hashmap - Java
    * Property Bag - C#/.Net
    

"""

##################################
#@ Dictionaries
"""
* Lists index their entries based on the position in the list
* Dictionaries are like bags- no order
* So we index the things we put in the dictionary with a "lookup tag"
"""

purse = dict()
purse["money"] = 12
purse["Candy"] = 3
purse["tissues"] = 75
print(purse)
# >>>{'money': 12, 'Candy': 3, 'tissues': 75}

print(purse['Candy'])
# >>> 3
purse['Candy'] = purse['Candy'] + 2
print(purse)
# >>>{'money': 12, 'Candy': 5, 'tissues': 75}

###################################
#@ Comparing Lists and Dictionaries
"""
* Dictionaries :-
*                Dictionaries are like lists except that use keys,
*                instead of numbers to look up values
"""
#@
lst = list()       #       List           
lst.append(21)     # Key        Value         
lst.append(183)    # [0]            21                                     
print(lst)         #                         
# >>> [21,183]     # [1]            183               
lst[0] = 23        #                          
print(lst)         #                         
[23,183]           #                       

#@
Dic = dict()                       #     Dictionary                                                                                                  
Dic['age'] = 21                    # Key          Values                                                                                                  
Dic['course'] = 182                # ["course"]     182                                                                                                           
print(Dic)                         #                                                                                                        
# >>> {'age': 21, 'course': 182}   # ["age"]         21                                      
Dic['age'] = 23                    #                                                                                                             
print(Dic)                         #                                                                                                        
# >>> {'age': 23, 'course': 182}   #                                                                                                                              

#@ Dictionary Literals(Constants)
"""
* Dictionary literals use curly braces and have a list of "Key: value" pairs
* You can make an empty dictionary using empty curly braces
"""
dic = {"chuck": 1,"fred":42,"jan":100}
print(dic)
# >>> {'chuck': 1, 'fred': 42, 'jan': 100}

emp_dic = []
print(emp_dic)
# >>>[]

##############################
#@ Dictionary Counting

#@ Many Counters with a Dictionary
"""
One common use of dictionaries is counting
how often we "see" something
"""
dic = dict()
dic["csev"] = 1
dic["cwen"] = 1
print(dic)
#>>> {'csev': 1, 'cwen': 1}

dic['cwen'] = dic["cwen"] + 1
print(dic)
# >>>{'csev': 1, 'cwen': 2}


#@ Dictionary Tracebacks
"""
* It is error to reference a key which is not in the dictionary
* We can use the "in" operator to see if a key is in the dictionary
"""
dic = dict()
print(dic['csev'])
"""
Tracebacks(most recent call last)
    files "<stdin>", line 1, in <module>
KeyError: 'csev'
"""
if 'csev' in dic:
    print("True")
else:
    print("False")
    
###################################
# When We See a New Name
"""
When we encounter a new name, we need to add a new entry in the dictionary and if this the second or later time we have seen the name,
we simply add one to the count in the dictionary under that name
"""

counts = dict()
names = ['csev','cwen','csev','zquian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
# {'csev': 2, 'cwen': 2, 'zquian': 1}

###################################
#@  The get method for dictionaries
"""
* the patters of cheking to see if a key is already in a dictionary and assuming a default value
*  -if the key is not there is so comman that there is method called get() that does this for us
"""
# Default value if key does not exist(and no traceback)


counts = dict()
names = ['csev','cwen','csev','zquian','cwen']
for name in names:
    if name in counts:
        x = counts[name]
    else:
        x = 0 #Deault value
x = counts.get(name,0)
print(x)

#####################################
## Simplified counting with get()
"""
we can use get() and provide a default value of zero when the key is not yet
in the dictionary - and then just add one
"""
#@
counts = dict()
names = ["csev","cwen","csev","zqian","cwen"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

######################################
#####Chapter 9(Dictionaries)
#Counting words in text
#Counting Patterns

"""
The general pattern to counts the words in a line of text is to split
the line into words, then loop through words and use a dictionary to track
the count of each word independently .
"""
counts = dict()
print("Enter a line of text: ")
line = input("")
words = line.split()
print("Words: ",words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word,0) + 1
print("Counts", counts)

"""
the clown ran after the car and the car ran into the tent and the tent fell 
down on the clown and the car
>>> Words:  ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 
>>> 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']
>>> Counting...
>>> Counts {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
"""

######################################
####### Definite Loops and Dictionary
"""
Even though dictionaries are not stored in order,we can write loop that goes
through all the entries in a dictionary - actually goes through all of the keys in the dictionary
and looks up the values .
"""
counts = {"chuck":1,"fred":42, "jan":100}
for key in counts:
    print(key,counts[key])
"""
chuck 1
fred 42
jan 100
"""

########################################
## Retrieveing lists of Keys and Values
#* You can get a list of keys, values or items(both) from a dictionary
dic = {"chuck":1,"fred":42, "jan":100}
print(list(dic))
# >>>['chuck', 'fred', 'jan']
print(dic.keys())
print(dic.values())
print(dic.items())

"""
>>> dict_key(['chuck', 'fred', 'jan'])
>>> dict_values([1, 42, 100])
>>> dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])
"""

######################################
### Bonus: Two Iteration Variable
"""
* We loop through the key-value pairs in a dictionary using "two" iteration variables
* Each iteration, the first variable is the key and the
* - second variable is the corresponding value for the key 
"""

dic = {'chuck':1,'fred':42, 'jan':100}
for ky, val in dic.items():
    print(ky,val)
    
"""
chuck 1
fred 42
jan 100
"""

#@
name = input("Enter file: ")
handle = open(name)
counts = dic()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


############################################
########### Chapter 9 (Dictionaries)
# Counting Word frequency using a Dictionary
#@
fname = input("Enter file: ")
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)
for lin in hand:
    lin = lin.rstrip()
    print(lin)
    words = lin.split()
    for word in words:
        print(word)
"""
>>> the clown ran after the car and the car ran into the tent and the tent fell 
>>> down on the clown and the car
>>> the
>>> clown
>>> ran
>>> after
>>> 
>>> ...
>>> ...
>>> ...
>>> and
>>> the
>>> car
"""

#@
fname = input("Enter a file: ")
if len(fname) < 1: fname = "clown.txt"
hand = open(fname)
di = dict()
for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        if word in di:
            di[word] = di[word] + 1
        else:
            di[word] = 1
            print("**New**")
        print(word,di[word])
print(di)

"""     
>>> **New**
>>> the 1  
>>> **New**
>>> clown 1
...
...
...
>>> clown 2
>>> and 3
>>> the 7
>>> car 3
"""


#@
di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    words = line.split()
    # print(words)
    for word in words:
        print(w)
        if word in di :
            di[word] = di[word] + 1
            print("**Exixting**")
        else:
            di[word] = 1
            print("**NEW**")
        print(dic[word])
print(di)

"""
>>> **New**
>>> the 1  
>>> **New**
>>> the 5
>>> tent 2
>>> **New**
>>> ....
>>> ....
>>> ....
>>> the 6
>>> clown 2
>>> and 3
>>> the 7
>>> car 3
>>> {}
"""


#@
fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)
dic = dict()
for line in hand:
    line = line.rstrip() 
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        print("**",word,dic.get(word,-99))
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
        print(word, dic[word])

"""
>>> ** the -99  
>>> the 1       
>>> ** clown -99
>>> clown 1
>>> ...
>>> ...
>>> ...
>>> the 5
>>> clown 2
>>> ** and 2
>>> and 3
>>> ** the 6
>>> the 7
>>> ** car 2
>>> car 3
"""

#@
fname = input("Enter file: ")
fhand = open(fname)
di = dict()
for line in fhand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for w in words:
        # if the key is not there the count is zero 
        oldcounts = di.get(w,0)   #   in single line     
        print(w,"old", oldcounts) #    it would be     
        newcount = oldcounts + 1  # di[word] = di.get(w,0) + 1      
        di[w] = newcount         # print(w,'new',newcount)      
        # in single line
        di[w] = di.get(w,0) + 1
        print(w, "new",newcount)
        # print(w,di[w])
print(di)

"""
>>> the old 0  
>>> the new 1  
>>> clown old 0
>>> clown new 1
>>> ....
>>> ....
>>> ....
>>> the new 13
>>> car old 4
>>> car new 5
>>> {'the': 14, 'clown': 4, 'ran': 4, 'after': 2, 'car': 6, 'and': 6, 'into': 2, 'tent': 4, 'fell': 2, 'down': 2, 'on': 2}
"""

#@
fname = input("Enter File: ")
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)
dic = dict()
for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    #print(words)
    for word in words:
        # idioms: retieve/create/update count
        dic[word] = dic.get(word,0) + 1
        print(word,'new', dic[word])
print(dic)

"""
>>> new 1  
>>> clown new 1
>>> ran new 1  
>>> after new 1
>>> ....
>>> ....
>>> ....
>>> car new 3
>>> {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 
>>> 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
"""   

#@
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
        # print(word,'new', dic[word])
print(dic)

"""
>>> {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 
>>> 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
"""


#####################################
#@ Now we want to find the most common word
fname = input("Enter the file name: ")
if len(fname) < 1 : fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
        # print(word,'new',dic[word])
# print(dic)
for k,v in dic.items():
    print(k,v)
"""
>>> the 7  
>>> clown 2
>>> ran 2  
...
...
>>> fell 1
>>> down 1
>>> on 1
"""

#@
fname = input("Enter the file name: ")
if len(fname) < 1 : fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # Idioms retrieve/create/update
        dic[word] = dic.get(word,0) + 1
# Now we want to find the most common word
largest = -1
for k,v in dic.items():
    print(k,v)
    if v > largest:
        largest = v
print("Done", largest)
"""
>>> the 7  
>>> clown 2
>>> ran 2  
>>> after 1
>>> ...
>>> ...
>>> ...
>>> down 1
>>> on 1
>>> Done 7
"""

#@
fname = input("Enter a name: ")
if len(fname) < 1: fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
largest = -1
theword = None
for k,v in dic.items():
    print(k,v)
    if v > largest :
        largest = v
        theword = k
print("Done",theword,largest)        


"""
>>> the 7  
>>> clown 2
>>> ran 2
...
...
>>> down 1
>>> on 1
>>> Done car 7
"""



#@ 
fname = input("Enter a name: ")
if len(fname) < 1: fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # idiom: retrieve/create/update
        dic[word] = dic.get(word,0) + 1
# print(di)
# now we want to find the most common word
largest = -1
theword = None
for k,v in dic.items():
    if v > largest:
        largest = v
        theword = k
print("Done",theword,largest)
        

###########################################
#@ Chapter 10(Tuples)
"""
* Tuples are another kind of sequence that function much like a list
*  -they have elements which are indexed starting at 0
"""
x = ("Glenn","Sally","Joseph")
print(x[2])     # for items in y:
# >>> Joseph    #     print(y)                                        
y = (1,9,2)     # ....                                           
print(y)        # ....                                        
# >>>(1,9,2)    #  1                                           
print(max(y))   #  9                                            
# >>> 9         #  2                                      
                # >>>

######################################
## but... Tuples are "immutable"
"""
Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

"""
# List         String                          Tuple
x = [9,8,7]   # y = "ABC"                      # z = (5,4,3)                                                                         
x[2] = 6      # y[2] = 'D'                     # z[2] = 0                                                                        
print(x)      #Traceback:'str'object doesn't   # Traceback:'str'object                                                                                           
[9,8,6]       #-Support item Assignment        # doesn't item Assignment
#              >>>                               >>>

#####################################
#@ Things not to do with tuples
#@
x = (3,2,1)
x = x.sort()
print(x)
# >>> AttributeError: 'tuple' object has no attribute 'sort'

#@
x = (3,2,1)
x = x.append(4)
print(x)
# >>>AttributeError: 'tuple' object has no attribute 'append'

#@
x = (3,2,1)
x = x.reverse()
print(x)
# >>>'tuple' object has no attribute 'reverse'

# A Tale of Two Sequences
l = list()
print(dir(l))
"""
['__add__', '__class__', '__class_getitem__', '__contains__',
'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__',
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__','__repr__', 
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
'__str__', '__subclasshook__',

'append', 'clear', 'copy', 'count',
'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

#@
t = tuple()
print(dir(t))
"""
['__add__', '__class__', '__class_getitem__', '__contains__',
'__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__',
'count', 'index'] 
"""

##################################
#@ Tuples are more efficient
"""
* Since Python does not have to build tuple structures to be modifiable,
* - they are simpler and more efficient in terms of memory use and performance than lists
* So in our program when we are making "temporary variable" we prefer tuples over lists

"""

###################################
#@ Tuples and Assignment
"""
* We can also put a tuple on the left-hand side of an assignment statement.
* We can even omit the parentheses
"""
#@
(x,y) = (4,"fred")
print(y)
# >>> fred

#@
(a,b) = (99,98)
print(a)
# >>> 99

## Tuples and Dictionary
#  The items() method in dictionary returns a list of(key,value) tuples
dic = dict()
dic["csev"] = 2
dic["cwen"] = 4
for (k,v) in dic.items():
    print(k,v)
...
"""
>>> csev 2
>>> cwen 4
"""
tups = dic.items()
print(tups)
# >>> dict_items([('csev',2),('cwen',4)])

########## Tuples are comprable
""" The comparison operators work with tuples and other sequences.
if the first item is equal, python goes on to the element, and so on untill it finds elements
that differ
"""
#@
if (0,1,2) < (5,1,2):
    print(True)
else:
    print(False)
# >>> True

#@
if (0,1,2) > (5,1,2):
    print(True)
else:
    print(False)
# >>> False

#@
if (0,1, 2000000) < (0,3,4):
    print(True)
else:
    print(False)
# >>> True

#@
if ('Jones','Sally') < ('Jones','Sam'):
    print(True)
else:
    print(False)
# >>> True

#@
if ('Jones','Sally') > ('Adams','Sam'):
    print(True)
else:
    print(False)
# >>> True

######################################
#Sorting Lists of Tuples
"""
* We can take advantage of the ablity to sort a list of tuple get to sorted version of a dictionary
* First we sort the dictionary by the key using items() method and sorted function
"""
#@
d = {'a': 10,'b':1,'c':22}
print(d.items())
# >>> dict_items([('a', 10), ('b', 1), ('c', 22)])

#@
print(sorted(d.items()))
# >>> [('a', 10), ('b', 1), ('c', 22)]

##########################
##### Using sorted()
"""
* We can do this even more directly using the built-in function sorted that takes a sequence
* - as a parameter and returns a sorted sequeence
"""
d = {"a":10,"b":1,"c":22}
t = sorted(d.items())
print(t)
# >>> [('a', 10), ('b', 1), ('c', 22)]
for k,v in sorted(d.items()):
    print(k,v)
"""
    >>> [('a', 10), ('b', 1), ('c', 22)]
    >>> a 10
    >>> b 1 
    >>> c 22
"""

############################
#@ Sort by values instead of keys
"""
* If we could construct a list of tuples of the form (value,keys) we could sort by value
* We do this with a for loop that create a lsit of tuples
"""
#@
c = {"a": 1, "b": 2, "c": 3}
tmp = list()
for k,v in c.items():
    tmp.append(v,k) #Append takes only one arguments 
print(tmp)          #So we need to make one lke ((v,k))
# >>> TypeError: list.append() takes exactly one argument (2 given) 

#@
c = {"a":1, "b":2,"c":3}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
# >>> [(1, 'a'), (2, 'b'), (3, 'c')]

#@
c = {"a":1,"b":2,"c":3}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
tmp = sorted(tmp, reverse = True) #Note
print(tmp)
# >>> [(3, 'c'), (2, 'b'), (1, 'a')]

#@
fhand = open("romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key,val in counts.items():
    lst.append((key,val))
lst = sorted(lst,reverse = True)
for val, key in lst[:10]:
    print(key,val)
"""
>>> 1 yonder 
>>> 1 with   
>>> ...
>>> ...
>>> 1 sick
>>> 1 pale
"""

##Even Sorter Version
#@
c = {"a":10,"b":1,"c":22}
print(sorted([(v,k) for k,v in c.items()])) 
# >>> [(1, 'b'), (10, 'a'), (22, 'c')]

"""
* List comprehension create a dynamic list. in this case,
*- we make a list of reversed tuples and then sort it.
"""


##############################################
##############################################
############ Chapter 10(Tuples)
#@ Sorting a dictionary using Tuples
fname = input("Enter File: ")
if len(fname) < 1: fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fname:
    line = line.strip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
print(dic)
x = sorted(dic.items())
print(x)
"""
{'c': 1, 'l': 1, 'o': 1, 'w': 1, 'n': 1, '.': 1, 't': 2, 'x': 1}
[('.', 1), ('c', 1), ('l', 1), ('n', 1), ('o', 1), ('t', 2), ('w', 1), ('x', 1)]
"""

##@
fname = input("Enter File: ")
if len(fname) < 1: fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.strip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
print(dic)
tmp = list()
for k,v in dic.items():
    print(k,v)
    newt = (v,k)
    tmp.append(newt)

print("Flipped",tmp)

"""
>>> Enter File: clown.txt
>>> {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
>>> the 7
>>> clown 2
>>> ...
>>> ...
>>> down 1
>>> on 1
>>> Flipped [(7, 'the'), (2, 'clown'), (2, 'ran'), (1, 'after'), (3, 'car'), (3, 'and'), (1, 'into'), (2, 'tent'), (1, 'fell'), (1, 'down'), (1, 'on')]
"""

#@
fname = input("Enter File: ")
if len(fname) < 1: fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.strip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
print(dic)
tmp = list()
for k,v in dic.items():
    print(k,v)
    newt = (v,k)
    tmp.append(newt)
print("Flipped",tmp)
tmp = sorted(tmp)
print("sorted",tmp)
"""
Enter File: clown.txt
{'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
the 7
clown 2
...
....
down 1
on 1
Flipped [(7, 'the'), (2, 'clown'), (2, 'ran'), (1, 'after'), (3, 'car'), (3, 'and'), (1, 'into'), (2, 'tent'), (1, 'fell'), (1, 'down'), (1, 'on')] 
sorted [(1, 'after'), (1, 'down'), (1, 'fell'), (1, 'into'), (1, 'on'), (2, 'clown'), (2, 'ran'), (2, 'tent'), (3, 'and'), (3, 'car'), (7, 'the')] 
"""


#########################################
#########@ Good concept
fname = input("Enter file name: ")
if len(fname) < 1: fname = "clown.txt"
fhand = open(fname)
dic = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
# print(dic)
tmp = list()
for k,v in dic.items():
    newt = (v,k)
    tmp.append((newt))
# print("Flipped",tmp)
tmp = sorted(tmp, reverse = True)
# print('Sorted', tmp[:5])
print(tmp)
for v,k in tmp[:5]:
    print(k,v)

#########################################
#########################################
################## Chpater 11 (Regular Expressions)
#@ Regular Expressions( Really clever " wild card " expressions for matching and parsing string)
"""
In computing, a regular expression, also referred to as "regex" or "regexp",
provides a concise and flexible means for matching string of text,
such as particular characters, words, pr patterns of characters,
words, or patterns of characters.
A regular expression is written in a formal language that can be interpreted by a regualr expressionn processor.
"""

# Understanding Regular Expressions
"""
* Very powerful and quite cryptic
* Fun once you understand them
* Regular expressions are a language unto themselves
* A language of "marker characters" - programming with characters
* It is kind of an "old school" language - compact
"""

# Regular Expression Quick Guide 
"""
" ^ " Matches the beginning of a line
" $ " Matches the end of the line
" . " Matches any character
" \s " Matches whitespace
" \S " Matches any non-whitespace character
" * " Repeats a character zero or more times
" *? " Repeats a character zero or more times (non- greedy)
" + " Repeats a character one or more times
" +? " Repeats a character one or more times (non-greedy)
" [aeiou] " Matches a single character in the listed set
" [^XYZ] " Matches a single character not in the listed set
" [a-z0-9] " The set of characters can include a range
" ( " Indicates where string extraction is to start
" ) " Indicates where string extraction is to end
"""

############################################
## The Regular Expression Module
"""
* Before you can use regular expressions in your program, you must import the library using "import re"
* You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
* You can use re.findall() to extract portions of a string that match your regular expression,
* -a combination of find() slicing: var[5:10]
"""

#@
# Using re.search() like find()
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.find('From') >=0:
        print(line)
"""
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
From: stephen.marquard@uct.ac.za
From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
...
...
...
From: cwen@iupui.edu
From cwen@iupui.edu Thu Jan  3 16:23:48 2008
From: cwen@iupui.edu
"""


#@
import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search('From',line):
        print(line)
"""
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
From: stephen.marquard@uct.ac.za
From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
...
...
...
From cwen@iupui.edu Thu Jan  3 16:23:48 2008
From: cwen@iupui.edu
"""
#@
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.strip()
    if line.startswith('From: '):
        print(line)
"""
>>> From: stephen.marquard@uct.ac.za
>>> From: louis@media.berkeley.edu
>>> ...
>>> ...
>>> ...
>>> From: cwen@iupui.edu
>>> From: cwen@iupui.edu
"""

#@
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From',line):
        print(line)
"""
>>> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
>>> From: stephen.marquard@uct.ac.za
>>> ...
>>> ...
>>> ...
>>> From cwen@iupui.edu Thu Jan  3 16:23:48 2008
>>> From: cwen@iupui.edu
"""

"""
* We fine-tune what is matched by adding special character to the string
"""

###################################
#@ Wild -Card Characters
"""
* The dot character matches any character
* If you add the asterisk character, the character is "any number of times"
"""
"""
>>> X-Sieve: CMU Sieve 2.3                   #*       
>>> X-DSPAM - Result: Innocent               #* ^X. *:          
>>> X-DSPAM - Confidence: 0.8475             #*  ^ (match the start of the line)           
>>> x-Content-Type-Message-Body: text/plain  #*  . (match any character)
>>>                                         #*   * (many times)               
                                        #*                   
                                        #*                   
"""

################################################
#@ Fine-Tuning Your Match
"""
* Depending on how "clean" your data is and purpose of your application,
*- you may want to narrow your match down a bit
"""

"""
>>> X-Sieve: CMU Sieve 2.3               #*   ^X.*:                 
>>> X-DSPAM-Result: Innocent             #*   ^ Match the start of the line              
>>> X-Plane is behind schedule: two weeks#*   . Match any character
                                        #*    follow by :
"""

"""
                                         #*     * many times
>>> X-Sieve: CMU Sieve 2.3               #*   ^X-\S+:                 
>>> X-DSPAM-Result: Innocent             #*   ^ Match the start of the line              
>>> X-Plane is behind schedule: two weeks#*   \S Match any non-whitespace character   
                                        #*     + One or more times and followed by :
"""

###
#@ Wild-Card Characters
"""
* The dot character matches any character
* If you add the asterisk character, the character is "Any number times"
"""
"""
>>> X-Sieve: CMU Sieve 2.3
>>> X-DSPAM- Result: Innocent
>>> X-DSPAM-Confidence: 0.8475

"""


###########################################
### Chapter 11(From Matching to extracting)
# Matching and extracting Data
"""
* re.search() returns a True/False depending on whether the string matches the regular expression
* If we actually want the matching strings to be extracted, we use re.findall()
"""
#@
# [0-9]+ (one or more digits)
import re
x = "my 2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+',x) # 0-9 means one digit
print(y)
# >>> ['2', '19', '42']
# if you going to find nothing you will get empty list

###############################
#@ When we use re.findall(), it returns a list of zero or more substring that match the regular expression
import re
x = "My 2 favorite number are 19 and 42"
y = re.findall('[0-9]+',x)
print(y)
# >>>['2', '19', '42']

y = re.findall('[AEIOU]+',x)
print(y)
# >>> []

#######################################
### Warning: Greedy Matching
"""
* The repeat characters(* and +) push outward in both directions(greedy) to match the largest possible string
"""
import re                        #    ^F.+:           
x = "From:Using the: character"  # ^F first character in the match is an F                                    
y = re.findall('^F.+:',x)        #  .+ match any charcter and One or more charcters                             
print(y)                         #   : Last character in the match is a:       
# >>> ['From:Using the: ']       #                                

##############################
### Non- Greedy Matching
"""
Not all regular expression repeat codes are greedy!
if you add a "?" character, the + and * chill out a bit...
"""
import re                         # ^F.+ ?:                                                    
x = "From: Using the : character" # First character in the match is an F                                                                          
y = re.findall('^F.+?:',x)        # .+? One or more character not greedy                                                                    
print(y)                          # : Last character in the match is                                                  
# >>>['From:']                                                                             

# Note:- Non-greedy is more reasonable default

################################################
# Fine - Tuning String Extraction
""" 
* You can refine the match for re.findall() and separately determine
*-which portion of the match is to be extracted by using parantheses
"""
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> ['stephen.marquard@uct.ac.za']
"""
'\S+@\S+'
"""

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('.@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> ['d@uct.ac.za']

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('.@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> ['d@uct.ac.za']

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^.@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> []

#@ 
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^s.+@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> []

#@ 
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^ From(\S+@\S+)',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> []

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^s+@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> []

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x) ## \S At least one non-whitespace character from both side
print(y)
# >>> ['stephen.marquard@uct.ac.za']


#######################################
#######################################
#######################################
###### Note:-
"""
# * Parentheses are not part of the match - but they tell where to start and stop,
* -what string to extract
"""
#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x)
print(y)
# >>>['stephen.marquard@uct.ac.za']

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^From(\S+@\S+)',x)
print(y)
# >>> ['stephen.marquard@uct.ac.za']


#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^From \S+@\S+',x)
print(y)
# >>> ['From stephen.marquard@uct.ac.za']

#@
import re
x =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall(' \S+@\S+',x)
print(y)


#######################################
### String parsing
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# >>> 21

#@
sppos = data.find('',atpos)
print(sppos)
# >>> 31

#@
host = data[atpos + 1 : sppos]
print(host)
# >>> uct.ac.za

## Double Split pattern
#@
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = data.split()
email = words[1]
piece = email.split('@')
print(piece[1])
# >>> uct.ac.za

#@
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# >>> 21

#@
sppos = data.find('',atpos)
print(sppos)
# >>> 31

#@
host = data[atpos + 1 : sppos]
print(host)
# >>> uct.ac.za

# Sometime we split a line one way, and then grab one of the piece of the line
# and split that piece again
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces)
# >>>['stephen.marquard', 'uct.ac.za']

##############################################
### The Regex Version
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin) # [^ ] match non-blank character
print(y)
# >>> ['uct.ac.za']

#@
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@\S*',lin) # [^ ] match non-blank character
print(y)
# >>> ['@uct.ac.za']

#@
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@[^\S]*',lin) # [^ ] match non-blank character
print(y)
# >>> ['@']

#@
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@(^\S)*',lin) # [^ ] match non-blank character
print(y)
# >>> ['']


#@
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@(^\S)*',lin) # [^ ] match non-blank character
print(y)
# >>> []


##################################################
#Note :-
### Even Cooler Regex Version
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall("^From .*@([^ ]*)",lin)
print(y)
# >>> [uct.ac.za']


#@
import re
fhand = open("mbox-short.txt")
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:',max(numlist))
# >>>Maximum: 0.9907


####################################
####################################
##Escape character
"""
* If you want a special regular expression character to just behave normally(most of the time)
* -you prefix it with '\'
"""

import re 
x = "we just received $10.00 for cookies."
y = re.findall('\$[0-9.]+',x)
print(y)
# >>> ['$10']


######################################
######################################
####################(Chapter 12)
## Network programs
"""
Transport control Protocol(TCP)
* Built on top of IP(Internet Protocol)
* Assumes IP might lose some data stores and restransmits data if it seems to be lost
* Handles "Flow control" using a transmit window
* Provide a nice reliable pipe
"""

#################################
# TCP Connections/Sockets

"""
In computer networking, an internet socket or network socket is an endpoint of a bidirectional
inter-process communication flow across an internet protocal-based computer network, socket internet
"""

####################################
## TCP Port Numbers
"""
* A port is an application - specific or process - specific software communications endpoint
* it allows multiple networked applications to coexist on the same server
* There is a list of well-known TCP port numbers
"""

"""
Incoming E-mail : 25                             
Login : 23                         
Web server : 80 and 443                          
Personal Mail Box : 109 and 110                           

"""

#############################
#@ Comman TCP Port
"""
* Telnet(23) - Login      * IMAP(143/220/993) - Mail Retrieval                 
* SSH(22) - Secure Login  * POP(109/110) - Mail Retrieval
* HTTP(80)                * DNS(53) - Domain Name
* HTTPS(443) - Secure     * FTP(21) - File Transfer                      
* SMTP(25) - Mail                           
"""

#Sockets in Python
"""
* Python has built-in-supprt library(socket) for TCP Sockets
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Note: Here is socket its short of like unopen file handle, its outword looking thing that it not yet connected
# (socket.AF_INET):- (this creae socket bt doesnot associate);- this say we gonna make socket that goes across internet 
# (socket.SOCK_STREAM):- which mean that its series of character that come one after other rather than series of blocks of text 
mysock.connect(("data.pr4e.org", 80)) # (data.pr4e.org is (Host)) (80 is (port))



######################################################
#####################################################
### Chapter 12(Networked Programs):-Application protocalls
"""
* Since TCP(and Python) gives us a reliable socket,what do we want to do with the socket?
* What problem do we want to solve

*Application Protocols
* -----Mail
* -----World Wide Web
"""

#@
"""
(HTTP)HTTP-Hypertext Transfer Protocol :-
* The dominant Application Layer Protocol on the internet
* Invented for the web - to retrieve HTML,Image,Documents etc
* Extended to be data in addition to documents- RSS, Web Services,
* - etc... Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close the Connection
"""

#@
"""
* The HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents.
*- from servers over the internet
"""

#@
"""
What is a protcol
* A set of rules that all parties follow so we can predict each other's behaiour
* And not bump into each other
* .... On two-way roads in USA, drive on the right-hand side of road
* .... On two-way roads in the UK, drive on the left-hand side of road
"""

"""    
        http://wwww.dr-chuck.com/page1.html
*protocol        *host           *document

"""

################################
#@ Getting Data From The Server
"""
*
Each the user clicks on an anchor tag with an href= value to switch to a new page,
the browser makes a connection to the web server and issues a
"GET" request- to GET the content of the page at the specified URL

*
The server returns the HTML document to the Browser which formats
and displays the document to the user

"""

######################################
#@ Internet Standards
"""
* The standards for all of the Internet protocols(Inner working) are developed by an organization
* Interet Engineering Task Force(IETF)
* www.ietf.org
* Standard are called "RFCs" - "Request for Comments"
"""

##########################################
#@ Making an HTTP request
"""
* Connect to the server like www.dr-chuck.com
* Request a document(or the default document)
... Get http://www.dr-chuck.com/page1.html HTTP/1.0
... Get http://www.mlive.com/ann-arbor/HTTP/1.0
... Get http://www.facebook.com HTTP/1.0
"""

###############################
###############################
#################
#@ Chapter 12(Networked Program)
# Write a web browser
# An HTTP Request in python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode()) 
mysock.close()
"""
>>> HTTP/1.1 400 Bad Request
>>> Date: Mon, 03 Oct 2022 03:09:20 GMT        
>>> Server: Apache/2.4.18 (Ubuntu)
>>> Content-Length: 308
>>> Connection: close
>>> Content-Type: text/html; charset=iso-8859-1
>>> 
>>> <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
>>> <html><head>
>>> <title>400 Bad Request</title>
>>> </head><body>
>>> <h1>Bad Request</h1>
>>> <p>Your browser sent a request that this server could not understand.<br />
>>> </p>
>>> <hr>
>>> <address>Apache/2.4.18 (Ubuntu) Server at do1.dr-chuck.com Port 80</address>
>>> </body></html>
"""


#########################################
#########################################
## Chapter 12(Network Programs)
# Code example(socket1.py)
#@ About Characters and strings

#@@@
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romoe.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
"""
>>> HTTP/1.1 400 Bad Request
>>> Date: Mon, 03 Oct 2022 12:07:18 GMT        
>>> Server: Apache/2.4.18 (Ubuntu)
>>> Content-Length: 308
>>> Connection: close
>>> Content-Type: text/html; charset=iso-8859-1
>>> <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
>>> <html><head>
>>> <title>400 Bad Request</title>
>>> </head><body>
>>> <h1>Bad Request</h1>
>>> <p>Your browser sent a request that this server could not understand.<br />
>>> </p>
>>> <hr>
>>> <address>Apache/2.4.18 (Ubuntu) Server at do1.dr-chuck.com Port 80</address>
>>> </body></html>
"""


#@
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
"""
>>> HTTP/1.1 200 OK
>>> Date: Mon, 03 Oct 2022 12:08:47 GMT
>>> Server: Apache/2.4.18 (Ubuntu)
>>> Last-Modified: Sat, 13 May 2017 11:22:22 GMT
>>> ETag: "a7-54f6609245537"
>>> Accept-Ranges: bytes
>>> Content-Length: 167
>>> Cache-Control: max-age=0, no-cache, no-store, must-revalidate
>>> Pragma: no-cache
>>> Expires: Wed, 11 Jan 1984 05:00:00 GMT
>>> Connection: close
>>> Content-Type: text/plain
>>> 
>>> But soft what light through yonder window breaks
>>> It is the east and Juliet is the sun
>>> Arise fair sun and kill the envious moon
>>> Who is already sick and pale with grief
"""

#@
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
"""
>>> HTTP/1.1 200 OK
>>> Date: Mon, 03 Oct 2022 12:12:56 GMT
>>> Server: Apache/2.4.18 (Ubuntu)
>>> Last-Modified: Sat, 13 May 2017 11:22:22 GMT
>>> ETag: "a7-54f6609245537"
>>> Accept-Ranges: bytes
>>> Content-Length: 167
>>> Cache-Control: max-age=0, no-cache, no-store, must-revalidate
>>> Pragma: no-cache
>>> Expires: Wed, 11 Jan 1984 05:00:00 GMT
>>> Connection: close
>>> Content-Type: text/plain
>>> 
>>> But soft what light through yonder window breaks
>>> It is the east and Juliet is the sun
>>> Arise fair sun and kill the envious moon
>>> Who is already s
>>> ick and pale with grief
"""

#############################################
#############################################
#@ Chapter 12 (Network Programs)-(Characters and strings)
"""
* Represemting Simple Strings
1. Each character is represented by a number between 0 and 256 stored in 8 bits of memory
2. We refer to "8 bits of memory as a "byte" of memory-(i.e. my disk drive contains 3 terabytes of memory)
3. The ord() function tells us the numeric value of a simmle ASCII character
"""
print(ord("a"))
# >>> 97
print(ord("b"))
# >>> 98
print(ord("c"))
# >>> 99

#@ Multi- Byte Characters
"""
* To represent the wide range of character must handle we represent characters with more than one byte
* UTF-16 Fixed length - Two bytes
* UTF-32 Fixed length - Four bytes
* UTF-8 --1-4 bytes
    * Upwards compatible with ASCII
    * Automatic direction between ASCII and UTF-8
    * ASCII file is also UTF-8
* UTF-8 is recommended practice for encoding data to be exchanged between systems
"""

#@ Two kinds of strings in python
"""
* In Python 3, all strings internally are unicode
* Working with string variables in python programs and reading data from files usually "just works"
* When we talk to a network resource using sockets or talk to a databases we have to encode & decode data(usually to UTF-8) 

"""

## Python Strings to bytes
"""
* When we talk to an external resource like a network sockets, we send a byte
*-so we need to encode python3 strings into a given character encoding

*When we read data from an external resource, we must decode it based in the character set so it is
*- properly represented in python3 as a string
"""
while True:
    data = mysock.recv(512)
    if (len(data)) < 1:
        break
    mystring = data.decode()
    print(mystring)
    
###################################
#@ An HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
"""
>>> HTTP/1.1 200 OK
>>> Date: Mon, 17 Oct 2022 13:59:04 GMT
>>> Server: Apache/2.4.18 (Ubuntu)
>>> Last-Modified: Sat, 13 May 2017 11:22:22 GMT
>>> ETag: "a7-54f6609245537"
>>> Accept-Ranges: bytes
>>> Content-Length: 167
>>> Cache-Control: max-age=0, no-cache, no-store, must-revalidate
>>> Pragma: no-cache
>>> Expires: Wed, 11 Jan 1984 05:00:00 GMT
>>> Connection: close
>>> Content-Type: text/plain
>>> 
>>> But soft what light through yonder window breaks
>>> It is the east and Juliet is the sun
>>> Arise fair sun and kill the envious moon
>>> Who is already s
>>> ick and pale with grief
"""

############################################
##### Chapter 12 (Network Programs)
#@ Making HTTP Easier with urllib
"""
Since HTTP is so common,we have a library that does all that socket work for us and makes webpages look like file.
"""
import urllib.request,urllib.parse,urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
"""
>>> But soft what light through yonder window breaks
>>> It is the east and Juliet is the sun    
>>> Arise fair sun and kill the envious moon
>>> Who is already sick and pale with grief
""" 

#@ 
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""
{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1,
'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2,
'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1,
'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}
"""

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
print(words)
"""
['Who', 'is', 'already', 'sick', 'and', 'pale', 'with', 'grief']
"""

####################################
#Reading Web Pages
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
# 
"""
>>> <h1>The First Page</h1>
>>> <p>
>>> If you like, you can switch to the
>>> <a href="http://www.dr-chuck.com/page2.htm">
>>> Second Page</a>.
>>> </p>
"""

##########################################
# Code Example (urllib1.py) and (urlwords.py)
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.data.py4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


##########################################
##########################################
## Chapter 12(network programs) - (Parsing HTML)
# What is Web Scraping
"""
* When a program or script pretend to be a browser and retrieves web pages,looks at those web pages, extracts information and then looks at more web pages .
* Search engines scrape web pages - we call this "spidering the web" or "web crawling"
"""

"""
Why Scrape?:-
* Pull data - particularly social data - who links to who?
* Get ypur own data back out of some system that has no "export capabilty"
* Monitor a site for new information
* Spider the web to make database for a search engine
"""

#######################################
#######################################
# Scraping Web Pages
"""
* There is some controversy about web page scraping sites are a bit snippy about it
* Republishing copyrighted information is not allowed
* Violating terms of service is not allowed
"""

###########################################################################
###########################################################################
# The Easy Way - Beautiful Soup
"""
* You could do string searches the hard way
* or you can use the free software library called BeutifulSoup from www.crummy.com
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter -') #http://www.dr-chuck.com/page(1/2).html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
# >>>http://www.dr-chuck.com/page2.htm
    
#@ Summary
"""
* The TCP/IP gives us pipes/sockets between applications
* We designed application protocals to make use of these pipes
* HyperText Transfer Protocol(HTTP) is simple yet powerfull protocol
* Python has good support for socket, HTTP, and HTML parsing
"""

######################################
########################
#@Networked [Programs] Code Example
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certficate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ') #http://www.dr-chuck.com
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(htlm,'html.parser') # get error if you done htlm here bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: htlm.parser. Do you need to install a parser librry?
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
"""
>>> Enter - http://www.dr-chuck.com
>>> https://www.learnerprivacy.org/
>>> https://www.si.umich.edu/
>>> https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1159280
>>> https://www.learnerprivacy.org
>>> ....
>>> 
>>> ....
>>> ....
>>> https://www.youtube.com/watch?v=FJ078sO35M0
>>> http://afs.dr-chuck.com/citoolkit
>>> https://twitter.com/drchuck
"""
    
    
###############################################
###############################################
### Using Web Services (Chapter 13)
"""
* With the HTTP Request/Response well understood and well supported,
* - there was a natural move toward exchanging data between programs using these protocols
* We needed to come up with an agreed way to represent data going between applications and across networks
* there are two commonly used formats: XML and JSON
"""
# Sending Data across the "Net"
"""
                        {    
PHP Array       <->     "name" : "chuck"      <-> JavaScript Object                                    
Python Dictionary <->    "phone":"303-4456"    <-> Java HashMap                               
                        }
"""

# Agreeing on a "Wire Format"
"""
                Weired protocol
            |    <person>       | (XML)                                                         
            |        <name>     |                                                      
            |            Chuck  |       De-Serialize                                             
Python  <-->|        </name>    |    <--> Java HashMap                                                  
Dictionary  |        <phone>    |                                                          
            |            3034456|                                                     
            |        </phone>   |                                                    
            |    </person>      |                                                 
            |                   |                                            
"""

# XML is more precious than 

#######################################
######### Chapter 13(Using Web Services) XML
# Marking up data to send across the network
#@
"""
XML stand for eXtensible Markup Language
* Primary purpose is to help information systems share structure data
* It started as a simplified subset of the standard Generalized Markup Language(SGML), and is designed to be relatively human- legible
"""

#@
"""
XML Terminology
* Tags - indicate the beginning and ending of elements
* Attributes - Keyword/value pairs on the opening tag of XML
* Serialize/De-Serialize :- Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner
"""

#@
"""
XML Basic
Start Tag              <peson>                                                                                                                            
End Tag                 <name>Chuck</name>                                                                                                         
                        <phone type="int">                                                                                                                                                                                                                        
Text Content              +1 7343034456                                                                                                                           
                        </phone>                                                                                                                
Attribute               <email hide = "yes" />                                                                                                                         
                                                                                                                                        
Self Closing Tag       </person>                                                                                                                                 
"""

# its very much likely to html but diffrence is here we can name headinf whatever we want not like in html h1, h2 blaw ....

#@ WhiteSpace
"""
*Line ends do not matter white space is generally discarded
* - on text elments. We indent only to be readable
<peson>                
 <name>Chuck</name>    
 <phone type="int">                            
   +1 7343034456       
 </phone>              
 <email hide = "yes" />                        
</person>              
"""

"""
<person>
 <name>Chuck</name.
 <phone type="intl"> +1 7343034456</phone>
 <email hide = "yes"/>
</person>
"""


#XML "Elements" (or Nodes)
"""
                   <people>
                    <person>
                        <name>Chuck</name>
                        <phone>303 4456</phone>                                                                                                             
                    </person>                                                                                                                
Simple Element 
                    </person>                                                                                                                                      
Complex Element        <name>Noah</name>                                                                                                                                       
                       <phone>622 7421</phone>                                                                                                             
                    </person>                                                                                                             
                  <people
"""

#XML as a Tree
"""
<a>                        a                         
 <b>X</b>                                                 
 <c>                  b          c                     
  <d>Y</d>                                                 
  <e>Z</e>            x        d      e                       
 </c>                                                 
</a>                           y      z               
Element Text
"""

#XML Text and Attribute
"""

<a>                  a                                   
 <b w="5">X</b>                                                     
 <c>               b         c                                  
  <d>Y</d>                                                     
  <e>Z</e>       5    x    d    e                                 
 <c>                                                     
<a>                        y    z                       


"""

#   XML as Path
"""
<a>                              a
 <b/>                        b        c
 <c>        /a/b      X                             
  <d>Y</d>  /a/c/d    Y      X      d     e        
  <e>Z</e>  /a/c/e    Z                          
 </c>                               Y     Z
</a>  
Element          Text
"""

######################################
#@ Chapter 13 (Using Web Services) 
# Code Example XML1.py and XML2.py
#@
import xml.etree.ElementTree as ET
data = """
<person>
  <name>Chuck</name>
  <phone type = "intl">
    +1 734 303 4456
   </phone>
   <email hide = "yes"/>
</person> """
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr',tree.find('email').get('hide'))

"""
>>> Name: Chuck
>>> Attr yes 
"""

#############@
import xml.etree.ElementTree as ET
input = """
<stuff>
    <users>
        <user x ="7">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x= "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
"""
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name',item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribute',item.get('x'))
"""
>>> User count: 2
>>> Name Chuck   
>>> Id 001       
>>> Attribute 7  
>>> Name Brent   
>>> Id 009       
>>> Attribute 7
"""

#@
import xml.etree.ElementTree as ET
input = """
<stuff>
    <users>
        <user x ="7">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x= "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
"""
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name',item.find('name'))
    print('Id',item.find('id'))
    print('Attribute',item.get('x'))
"""
User count: 2
Name <Element 'name' at 0x00000250323C7380>
Id <Element 'id' at 0x00000250323C7330>    
Attribute 7
Name <Element 'name' at 0x00000250323C7470>
Id <Element 'id' at 0x00000250323C7420>    
Attribute 7
"""

#############################################
#####################################
### Chapter 13(Using Web Services) XML Schema
#* Describing a "contract" as to what is acceptable XML.
"""
XML Schema
* it is a languge that is allow you decide or whether not an particular xml documents meets a contract arrangement 
* it is itself schema
* Description of the ;egal format of an XML document
* Expressed in terms of constraints on the structure and content documents
* Often used to specify a "contract" between systems- "My system will only accept XML that conforms to this particular Schema."
* If a particular piece of XML meets the specifiaction of the Schema-it is said to "validate"

                            XML Validation

XML 
Document  --------\         -_-
                        Validator
XML Schema -------..../
Contract

                                                      XML Validation
XML Document
<person>
 <lastname>Severance</lastname>
 <age>17</age>
 <dateborn>2001-04-17</dateborn>
</person>
                                                            -_-    Validator
XML Schema Contract
<xs:complexType name = "person">
 <xs:sequence>
  <xs:element name="lastname"type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="databorn" type="xs.date"/>
 </xs:sequence>
</xs:complexType>
"""
# XML Schema is particular format of xml that render an opinion about xml supposed to look like
"""
Many XML Schema Language
* Document Type Definition(DTD)
* -http://en.wikipedia.org/wiki/Document_Type_Definition
* Standard Generalized Markup Language(ISO 8879:1986 SGML)
* -http://en.wikipedia.org/wiki/SGML
* XML Schema from W3C -(XSD)
* -http://en.wikipedia.org/wiki/XML_Schema_(W3C)
"""

#@ XSD XML Schema (W3C spec)
#* We will focus on the world wide web consortium(w3c) version
#* it is often called "W3C Schema" Because "Schema" is considered generic
#* More commonly it is called XSD because the file names end with .xsd
"""
XSD Structure
            <person>
            |  <lastname>Severance</lastname>
    element |  <age>17</age>
            |  <dateborn>2001-04-17</dateborn>
            </person>
xs:element                    
                    
xs:sequence     <xs:complexType name = "person">
    sequence->   <xs:sequence>
                |  <xs:element name = "lastname"type="xs:string"/>
    element     |  <xs:element name = "age"type = "xs:integer"/>
                |  <xs:element name = "dateborn" type = "xs:date"/>
                <xs:sequence>
                </xs:complexType>                                                              
#* You do not read thi file there is softaware that read all and cheque return True False
"""

#@ XSD Constraints
"""
<xs:element name="person">
 <xs:complexType
  <xs:sequence>
  @<xs:element name ="full_name" type = "xs:string"
    minOccurs="1" maxOccurs="1"/>
  $<xs:element name="child_name" type="xs:string"
      minOccurs="0" maxoccurs="10"/>
  <xs:sequence>
 </xs:complexType>
</xs:element>

                            <person>
                            @<full_name>Tove Refsnes</full_name>
                        $|  <child_name>Hege</child_name>
                        $|- <child_name>State</child_name>
                        $|  <child_name>Jim</child_name>
                             </person>
                                        
                                        
"""

#@
"""
xs:element name="customer" type = "xs:string"/>
xs:element name="start type="xs:date"/>
xs:element name="startdate" type="xs:dateTime"/>
xs:element name = "prize" type="xs:decimal"/>
xs:element name = "weeks" type="xs:integer"/>


                    <customer>John Smith</customer>
                    <start>2002-09-24</start>
                    <startdate>2002-05-30T09:30:10Z</startdate>
                    <prize>999.50</prize>
                    <weeks>30</weeks>
"""

#ISO 8601 Date/Time Form
"""
2002-05-30T09:30:10Z
"""

#@
"""
<? xml version="1.0" encoding="utf-8"? >
<xs:schema elementFormDefault = "qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <xs:element name="Address">
  <xs:complexType>
   <xs:sequence>
    <xs:element name="Recipient" type="xs:string"/>
    <xs:element name="Hoouse" type="xs:string"/>
    <xs:element name="Street" type="xs:string"/>
    <xs:element name="Town" type="xs:string"/>
    <xs:element minOccurs="0" name = "Country" type="xs:string"/>
    <xs:element name="PostCode" type="xs:string"/>
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value = "FR" />
          <xs:enumeration value = "DE" />
          <xs:enumeration value = "ES" />
          <xs:enumeration value = "UK" />
          <xs:enumeration value = "US" />
        </xs:restriction>
      </xs:simpleType
    </xs:element
   </xs:sequence
  </xs:complexType
 </xs:element
</xs:element
          
"""

#@
import xml.etree.ElementTree as ET
# XML would come from some servers on other side network we would give XML
data = ''' <person>
<name>Chuck</name>
<phone type="int1">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
# >>> Name: Chuck
# >>> Attr: yes


##@
import xml.etree.ElementTree as ET
input = """
<stuff>
    <users>
        <user x="2">
           <id>001</id>
           <name>Chuck</name>
        </user>
        <user x="7">
           <id>009</id>
           <name>Brent</name>
        </user>
    </users>
</stuff> """
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(lst)
print('User count:',len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribute',item.get("x"))
"""
>>> [<Element 'user' at 0x000001E361307380>, <Element 'user' at 0x000001E361307470>]
>>> User count: 2
>>> Name Chuck   
>>> Id 001       
>>> Attribute 2  
>>> Name Brent
>>> Id 009
>>> Attribute 7
"""

#@
import xml.etree.ElementTree as ET
input = ''' <stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:',len(lst))
for items in lst:
    print("Name",items.find('name').text)
    print("ID",items.find('id').text)
    print('Attribute',items.get("x"))
"""
>>> User count: 2
>>> Name Chuck   
>>> ID 001       
>>> Attribute 2  
>>> Name Brent   
>>> ID 009       
>>> Attribute 7
"""

####################################
###### Chapter 13(Using Web Services)
## Javascript Object Notation
'''
* Dougles Crockford "Discovered" JSON
* Object literal notation in javascript
'''
# XML is better for rich and hierarrachal documents
# JSON is best for just pulling data out of system and moving data beetween system with minimul fast

#@
import json
data = """{
    "name":"Chuck",
    "phone":{
        "type":"intl",
        "number": "+1 734 303 4456"
    },
    "email" : {
        "hide":"yes"
    }
}"""
info = json.loads(data)
print('Name:',info["name"])
print("Hide:",info["email"]["hide"])
"""
>>> Name: Chuck   
>>> Hide: yes 
"""

#@
import json
data = """{
    "name":"Chuck",
    "phone":{
        "type":"intl",
        "number": "+1 734 303 4456"
    },
    "email" : {
        "hide":"yes"
    }
}"""
info = json.loads(data)
print('Name:',info["name"])
print("Phone:", info["phone"]["type"])
print("Phone:", info["phone"]["number"])
"""
>>> Name: Chuck
>>> Phone: intl
>>> Phone: +1 734 303 4456
"""

#@
import json
input = """[
    {"id":"001",
    "x":"2",
    "name":"chuck"},
    {"id":"009",
    "x":"7",
    "name":"chuck"}
    ]"""
lst = json.loads(input)
print("User count:",len(lst))
for item in lst:
    print("Name:", item['name'])
    print("ID:", item['id'])
    print("Attribute:", item['x'])
"""
>>> User count: 2
>>> Name: chuck  
>>> ID: 001      
>>> Attribute: 2 
>>> Name: chuck  
>>> ID: 009      
>>> Attribute: 7
"""

################################
################################
#### Chapter 13 Using Web Services
# Code Example (json1.py)(json2.py)
#Service Oriented App
#@
import json
data = '''
{
    "name" : "Chuck",
    "phone":{
        "type":"int",
        "number":"+1 734 303 4456"
    },
    "email" : {
        "hide":"yes"
    }
}
'''
info = json.loads(data)
print('Name:', info["name"])
print('email:', info["email"]["hide"])
"""
>>> Name: Chuck
>>> email: yes
"""

#@
import json
input = """
[
    {"id":"001",
    "x" : "2",
    "name":"Chuck"
    },
    {"id":"009",
    "x":"7",
    "name":"Chuck"
    }
]
"""
info = json.loads(input)
print('User count:',len(info))
for item in info:
    print('Name',item['name'])
    print('ID',item['id'])
    print('Attribute',item['x'])
"""
>>> User count: 2
>>> Name Chuck   
>>> ID 001       
>>> Attribute 2  
>>> Name Chuck   
>>> ID 009       
>>> Attribute 7
"""

#@ Service Oriented Approach 
"""
* Most non-trival web applications use services
* They use services from other applications
    * Credit Card Charge
    * Hotel Reservation systems
* Services publish the "rules" application must follow to make use of the service(API)
"""

#@ Multiple Systems
"""
* Initially-two systems cooperate and split the problem
* As the data/service become useful-multiple applications want to use the information/application
"""


###########################################
###########################################
###########################################
############ Chapter 13(Using Web Services)/Web Services
"""
#Application Program Interface
the API itself is largely abstract in that it specifies interface and controls the behavior of the objects
specified in that interface. the software that provides the functionality described by an API is said to be an
"implementation" of the API. An API is typically defined in terms of the programming language used to build an application.
"""


#@
import urllib.request, urllib.parse, urllib.error
import json
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
while True:
    address = input("Enter Location: ") #http://maps.googleapis.com/maps/api/geocode/json?address=Ann + Arbor%2C + MI
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'address':address})
    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] !='OK':
        print('==== Failure To Retrieve====')
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["result"][0]["geometry"]["location"]["lng"]
    print("lat",lat,"lan",lng)
    location = js['result'][0]['formatted_address']
    print(location)
    
#@API
{
    "status":"ok",
    "results":[
        {
            "geometry":{
                "location_type":"APPROXIMATE",
                "loaction":{
                    "lat":42.2808256,
                    "lng":-83.7430378
                }
                
            },
            "address_components":[
                {
                    "long_name":"Ann Arbor",
                    "types":[
                        "locality",
                        "political"
                    
                    ],
                    "short_name":"Ann Arbor"
                    
                }
                
            ],
            "formatted_address":"Ann Arbour,MI,USA",
            "types":[
                "locality",
                "political"
            ]
        }
        
    ]
}


################################################
############# Chapter 13(Using Web Services)
####API Security and Rate Limiting
### Code Example geoson.py
#In Url encoding % means comma and = means space" "]

"""
API Security and Rate Limiting
* The compute resources to run these APIs are not "free"
* The data provided by these APIs is usually valuable
* The data providers might limmt the number of request per day, demand an API "Key", or even charge for useage
* They might change the rules as things progress...
"""

####@twwiter1.py
import urllib.request, urllib.parse, urllib.error
import ssl
import twurl
import json
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    print()
    acct = input('Enter Twitter Account: ')
    if (len(acct)) < 1 : break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name':acct,'count':'5'})
    print('Retrieving',url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining',headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js,indent=4))
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ',s[:50])

#@ twurl.py
import urllib.request, urllib.parse, urllib.error
import oauth
import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['l0Wao1qFvsODbEktnqzhRSgcj'],
                                   secrets['vY7TsJ5BYOzCX8DW6Qat9JScItOxnhYym6VbKvXl5FXu3WOllZ'])
    token = oauth.OAuthToken(secrets['715774453423206401-EMTjOMmmDBEWRaTcTOgz6CEbfz83gqs'], secrets['g8y6BMLdOqww1SUryzLB0giRIui05FBPSvVEaCmLE2XFM'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()


def test_me():
    print('* Calling Twitter...')
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)
    headers = dict(connection.getheaders())
    print(headers)





"""
Summary
* Service Oriented Architecture-allow an application to be broken into parts and distribution across network 
* An Application Program Interface(API) is a contract for interaction
* Web Services provide infrastructre for application cooperating(an API) over a network-SOAP and REST are two styles of web Services
* XML and JSON are serialization formats
"""


################################################
################################################
############# Chapter 13(Using Web Services)
### Code Example (twitter1.py) and (twitter2.py)

#@ Hidden.py
# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings
#@ Hidden.py
def oauth():
    return {"consumer_key": "744FKmHX5MX7iOxpXhU4mdCTq",
            "consumer_secret": "wchGCnIZjneopTyPHUfJRWIvjRzWn853pDTbLunddbUq7QAaNd",
            "token_key": "715774453423206401-WI4jFoFhTKQhYWH7f48KbqpFgkGx4dt",
            "token_secret": "mx8WQftS6wn9jkgotqa3huOALpVvR5QmL03lULF2Yd2Rq"}


######################################
######################################
#@twitter test twtest
import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count': '2'})
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)
print("Decoeded format")
print(data.decode())
# print(data.read().decode()) # Byte object has no attribute read

print ('======================================')
headers = dict(connection.getheaders())
print(headers)
"""
* Calling Twitter...
>>> https://api.twitter.com/1.1/statuses/user_timeline.json?oauth_consumer_key=744FKmHX5MX7iOxpXhU4mdCTq&oauth_timestamp=1665486702&oauth_nonce=28108511&oauth_version=1.0&screen_name=drchuck&count=2&oauth_token=715774453423206401-WI4jFoFhTKQhYWH7f48KbqpFgkGx4dt&oauth_signature_method=HMAC-SHA1&oauth_signature=7tBa07JMKYwPqCo7Ygj%2Fd2TQo%2Bc%3D    
>>> b'[{"created_at":"Tue Oct 11 00:39:42 +0000 2022","id":1579632802349604865,"id_str":"1579632802349604865","text":"RT @LorenaABarba: Took an after-lunch stroll in the @sfiscience library and found this gem from Barbara Oakley https:\\/\\/t.co\\/N4jgI8hcOF","truncated":false,"entities":{"hashtags":[],"symbols":[],"user_mentions":[{"screen_name":"LorenaABarba","name":"Lorena Barba","id":369758524,"id_str":"369758524","indices":[3,16]},{"screen_name":"sfiscience","name":"Santa Fe Institute","id":90258002,"id_str":"90258002","indices":[52,63]}],"urls":[],"media":[{"id":1579549874357473286,"id_str":"1579549874357473286","indices":[111,134],"media_url":"http:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","media_url_https":"https:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","url":"https:\\/\\/t.co\\/N4jgI8hcOF","display_url":"pic.twitter.com\\/N4jgI8hcOF","expanded_url":"https:\\/\\/twitter.com\\/LorenaABarba\\/status\\/1579549929223368704\\/photo\\/1","type":"photo","sizes":{"small":{"w":510,"h":680,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":1536,"h":2048,"resize":"fit"},"medium":{"w":900,"h":1200,"resize":"fit"}},"source_status_id":1579549929223368704,"source_status_id_str":"1579549929223368704","source_user_id":369758524,"source_user_id_str":"369758524"}]},"extended_entities":{"media":[{"id":1579549874357473286,"id_str":"1579549874357473286","indices":[111,134],"media_url":"http:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","media_url_https":"https:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","url":"https:\\/\\/t.co\\/N4jgI8hcOF","display_url":"pic.twitter.com\\/N4jgI8hcOF","expanded_url":"https:\\/\\/twitter.com\\/LorenaABarba\\/status\\/1579549929223368704\\/photo\\/1","type":"photo","sizes":{"small":{"w":510,"h":680,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":1536,"h":2048,"resize":"fit"},"medium":{"w":900,"h":1200,"resize":"fit"}},"source_status_id":1579549929223368704,"source_status_id_str":"1579549929223368704","source_user_id":369758524,"source_user_id_str":"369758524"}]},"source":"\\u003ca href=\\"http:\\/\\/twitter.com\\/download\\/iphone\\" rel=\\"nofollow\\"\\u003eTwitter for iPhone\\u003c\\/a\\u003e","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":10185562,"id_str":"10185562","name":"Charles Severance","screen_name":"drchuck","location":"iPhone: 37.868347,-122.255997","description":"I am on the faculty @UMSI, work on the open source @sakaiproject, and teach free programing courses starting with Python at https:\\/\\/t.co\\/x2UuItaiEL","url":"https:\\/\\/t.co\\/lA47SgfY0B","entities":{"url":{"urls":[{"url":"https:\\/\\/t.co\\/lA47SgfY0B","expanded_url":"https:\\/\\/www.dr-chuck.com","display_url":"dr-chuck.com","indices":[0,23]}]},"description":{"urls":[{"url":"https:\\/\\/t.co\\/x2UuItaiEL","expanded_url":"http:\\/\\/online.dr-chuck.com","display_url":"online.dr-chuck.com","indices":[124,147]}]}},"protected":false,"followers_count":27082,"friends_count":865,"listed_count":686,"created_at":"Mon Nov 12 16:33:12 +0000 2007","favourites_count":96,"utc_offset":null,"time_zone":null,"geo_enabled":true,"verified":false,"statuses_count":31608,"lang":null,"contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"131516","profile_background_image_url":"http:\\/\\/abs.twimg.com\\/images\\/themes\\/theme14\\/bg.gif","profile_background_image_url_https":"https:\\/\\/abs.twimg.com\\/images\\/themes\\/theme14\\/bg.gif","profile_background_tile":true,"profile_image_url":"http:\\/\\/pbs.twimg.com\\/profile_images\\/1275030553994178566\\/hL94BCHB_normal.jpg","profile_image_url_https":"https:\\/\\/pbs.twimg.com\\/profile_images\\/1275030553994178566\\/hL94BCHB_normal.jpg","profile_banner_url":"https:\\/\\/pbs.twimg.com\\/profile_banners\\/10185562\\/1592825992","profile_link_color":"009999","profile_sidebar_border_color":"EEEEEE","profile_sidebar_fill_color":"EFEFEF","profile_text_color":"333333","profile_use_background_image":true,"has_extended_profile":true,"default_profile":false,"default_profile_image":false,"following":false,"follow_request_sent":false,"notifications":false,"translator_type":"none","withheld_in_countries":[]},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Mon Oct 10 19:10:24 +0000 2022","id":1579549929223368704,"id_str":"1579549929223368704","text":"Took an after-lunch stroll in the @sfiscience library and found this gem from Barbara Oakley https:\\/\\/t.co\\/N4jgI8hcOF","truncated":false,"entities":{"hashtags":[],"symbols":[],"user_mentions":[{"screen_name":"sfiscience","name":"Santa Fe Institute","id":90258002,"id_str":"90258002","indices":[34,45]}],"urls":[],"media":[{"id":1579549874357473286,"id_str":"1579549874357473286","indices":[93,116],"media_url":"http:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","media_url_https":"https:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","url":"https:\\/\\/t.co\\/N4jgI8hcOF","display_url":"pic.twitter.com\\/N4jgI8hcOF","expanded_url":"https:\\/\\/twitter.com\\/LorenaABarba\\/status\\/1579549929223368704\\/photo\\/1","type":"photo","sizes":{"small":{"w":510,"h":680,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":1536,"h":2048,"resize":"fit"},"medium":{"w":900,"h":1200,"resize":"fit"}}}]},"extended_entities":{"media":[{"id":1579549874357473286,"id_str":"1579549874357473286","indices":[93,116],"media_url":"http:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","media_url_https":"https:\\/\\/pbs.twimg.com\\/media\\/FeuwPe4XEAY2jJf.jpg","url":"https:\\/\\/t.co\\/N4jgI8hcOF","display_url":"pic.twitter.com\\/N4jgI8hcOF","expanded_url":"https:\\/\\/twitter.com\\/LorenaABarba\\/status\\/1579549929223368704\\/photo\\/1","type":"photo","sizes":{"small":{"w":510,"h":680,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":1536,"h":2048,"resize":"fit"},"medium":{"w":900,"h":1200,"resize":"fit"}}}]},"source":"\\u003ca href=\\"http:\\/\\/twitter.com\\/download\\/iphone\\" rel=\\"nofollow\\"\\u003eTwitter for iPhone\\u003c\\/a\\u003e","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":369758524,"id_str":"369758524","name":"Lorena Barba","screen_name":"LorenaABarba","location":"Washington, DC","description":"Engineering professor, computational scientist, jazz buff, techie, academic writer & font geek. Editor: @cisemag @JOSS_TheOJ @OpenEngr @ReScienceEds @JOSE_TheOJ","url":"https:\\/\\/t.co\\/B8qdhqg7Xk","entities":{"url":{"urls":[{"url":"https:\\/\\/t.co\\/B8qdhqg7Xk","expanded_url":"http:\\/\\/about.me\\/lorenabarba","display_url":"about.me\\/lorenabarba","indices":[0,23]}]},"description":{"urls":[]}},"protected":false,"followers_count":9329,"friends_count":1322,"listed_count":402,"created_at":"Wed Sep 07 22:10:00 +0000 
>>> 2011","favourites_count":6972,"utc_offset":null,"time_zone":null,"geo_enabled":true,"verified":false,"statuses_count":12959,"lang":null,"contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"FAFAFA","profile_background_image_url":"http:\\/\\/abs.twimg.com\\/images\\/themes\\/theme18\\/bg.gif","profile_background_image_url_https":"https:\\/\\/abs.twimg.com\\/images\\/themes\\/theme18\\/bg.gif","profile_background_tile":true,"profile_image_url":"http:\\/\\/pbs.twimg.com\\/profile_images\\/1870376708\\/Barba-Lorena-2011a-square_normal.png","profile_image_url_https":"https:\\/\\/pbs.twimg.com\\/profile_images\\/1870376708\\/Barba-Lorena-2011a-square_normal.png","profile_banner_url":"https:\\/\\/pbs.twimg.com\\/profile_banners\\/369758524\\/1591611091","profile_link_color":"CD2305","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"F6F6F6","profile_text_color":"333333","profile_use_background_image":false,"has_extended_profile":true,"default_profile":false,"default_profile_image":false,"following":false,"follow_request_sent":false,"notifications":false,"translator_type":"none","withheld_in_countries":[]},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":1,"favorite_count":18,"favorited":false,"retweeted":false,"possibly_sensitive":false,"lang":"en"},"is_quote_status":false,"retweet_count":1,"favorite_count":0,"favorited":false,"retweeted":false,"possibly_sensitive":false,"lang":"en"},{"created_at":"Mon Oct 10 21:14:43 +0000 2022","id":1579581214851485696,"id_str":"1579581214851485696","text":"RT @JenMsft: A senior developer, walking a junior developer through the legacy code base \\n\\n\\"One day, this will all be yours\\" https:\\/\\/t.co\\/t\\u2026","truncated":false,"entities":{"hashtags":[],"symbols":[],"user_mentions":[{"screen_name":"JenMsft","name":"Jen Gentleman \\ud83c\\udf3a","id":3309105596,"id_str":"3309105596","indices":[3,11]}],"urls":[]},"source":"\\u003ca href=\\"https:\\/\\/mobile.
>>> Decoeded format
>>> ======================================
>>> {'date': 'Tue, 11 Oct 2022 11:11:45 GMT', 'perf': '7626143928', 'pragma': 'no-cache', 'server': 'tsa_f', 'status': '200 OK', 'expires': 'Tue, 31 Mar 1981 05:00:00 GMT', 'set-cookie': 'guest_id=v1%3A166548670579329163; Max-Age=63072000; Expires=Thu, 10 Oct 2024 11:11:46 GMT; Path=/; Domain=.twitter.com; Secure; SameSite=None', 'content-type': 'application/json;charset=utf-8', 'cache-control': 'no-cache, no-store, must-revalidate, pre-check=0, post-check=0', 'last-modified': 'Tue, 11 Oct 2022 11:11:45 GMT', 'x-transaction': '0b46919d49af72a5', 'content-length': '17757', 'x-access-level': 'read', 'x-frame-options': 'SAMEORIGIN', 'x-transaction-id': '0b46919d49af72a5', 'x-xss-protection': '0', 'x-rate-limit-limit': '900', 'x-rate-limit-reset': '1665487370', 'content-disposition': 'attachment; filename=json.json', 'x-app-rate-limit-limit': '100000', 'x-app-rate-limit-reset': '1665570700', 
>>> 'x-content-type-options': 'nosniff', 'x-rate-limit-remaining': '895', 'x-twitter-response-tags': 'BouncerCompliant', 'strict-transport-security': 'max-age=631138519', 'x-app-rate-limit-remaining': '99994', 'x-response-time': '422', 'x-connection-hash': '7f4bd5127d53ddc1c6a1f50aea2610f6e5897301141cf2044fcd4e82e69e55a3', 'connection': 'close'}
"""



"""
>>> Enter Twitter Account:abhishek__AI
>>> Retrieving https://api.twitter.com/1.1/statuses/user_timeline.json?oauth_consumer_key=744FKmHX5MX7iOxpXhU4mdCTq&oauth_timestamp=1665486466&oauth_nonce=11251245&oauth_version=1.0&screen_name=abhishek__AI&count=2&oauth_token=715774453423206401-WI4jFoFhTKQhYWH7f48KbqpFgkGx4dt&oauth_signature_method=HMAC-SHA1&oauth_signature=rSSLr%2BwAbxVlqTGzcOHPDctruSE%3D
>>> [{"created_at":"Sat Oct 08 14:12:58 +0000 2022","id":1578750302463086592,"id_str":"1578750302463086592","text":"RT @Ronald_vanLoon: Google finds that as #ArtificialIntelligence gets more advanced it gets more aggressive\nby @wef\n\n#AI #MI #DataScien
>>> Remaining 899

"""

"""
>>> Enter Twitter Account:drchuck
>>> Retrieving https://api.twitter.com/1.1/statuses/user_timeline.json?oauth_consumer_key=744FKmHX5MX7iOxpXhU4mdCTq&oauth_timestamp=1665486596&oauth_nonce=10322829&oauth_version=1.0&screen_name=drchuck&count=2&oauth_token=715774453423206401-WI4jFoFhTKQhYWH7f48KbqpFgkGx4dt&oauth_signature_method=HMAC-SHA1&oauth_signature=dDT8mVasgC42bAH7K2%2FHChFX9dk%3D
>>> [{"created_at":"Tue Oct 11 00:39:42 +0000 2022","id":1579632802349604865,"id_str":"1579632802349604865","text":"RT @LorenaABarba: Took an 
>>> after-lunch stroll in the @sfiscience library and found this gem from Barbara Oakley https:\/\/t.co\/N4jgI8hcOF"
>>> Remaining 897

"""

#################################
################ twitter2.py
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
TWITTER_URL= 'https://api.twitter.com/1.1/friends/list.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account: ')
    if (len(acct)) < 1: break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name':acct,'count':'5'})
    print('Retrieving',url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    js = json.loads(data)
    print(json.dumps(js, indent = 2))
    print('Remaining',headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   *No status found')
        s = u['status']['text']
        print(' ', s[:50])

"""
>>>   @Notnotaburner2 People cut on Doordash and Uber Ea
>>> Vaibhu31012842
>>>    *No status found
>>> Traceback (most recent call last):
>>>   File "c:\VsCode\py4e\tempCodeRunnerFile.py", line 33, in <module>  
>>>     s = u['status']['text']
>>> KeyError: 'status'
"""        

###########################################
##@ Removing key error
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
TWITTER_URL= 'https://api.twitter.com/1.1/friends/list.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account: ')
    if (len(acct)) < 1: break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name':acct,'count':'5'})
    print('Retrieving',url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    js = json.loads(data)
    print(json.dumps(js, indent = 2))
    print('Remaining',headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   *No status found')
            continue
        s = u['status']['text']
        print(' ', s[:50])
        
"""
>>> Enter Twitter Account: abhishek__AI
>>> Retrieving https://api.twitter.com/1.1/friends/list.json?oauth_consumer_key=744FKmHX5MX7iOxpXhU4mdCTq&oauth_timestamp=1665534054&oauth_nonce=15860517&oauth_version=1.0&screen_name=abhishek__AI&count=5&oauth_token=715774453423206401-WI4jFoFhTKQhYWH7f48KbqpFgkGx4dt&oauth_signature_method=HMAC-SHA1&oauth_signature=1FWBLtllJC6l8ZoJm3GB0e1L0bw%3D  
>>> {
>>>   "users": [
>>>     {
>>>       "id": 1246136668014301184,
>>>       "id_str": "1246136668014301184",
>>>       "name": "App Economy Insights",
>>>       "screen_name": "EconomyApp",
>>>       "location": "San Francisco, CA",
>>>       "description": "\u2022 App Economy Investor\n\u2022 French in Silicon Valley\n\u2022 Gaming industry veteran\n\u2022 Contributor on 
>>> Seeking Alpha\n\u2022 Previously @PwC and @BandaiNamcoUS",
>>>       "url": "https://t.co/M90ORMCg4o",
>>>       "entities": {
>>>         "url": {
>>>           "urls": [
>>>             {
>>>               "url": "https://t.co/M90ORMCg4o",
>>>               "expanded_url": "https://seekingalpha.com/author/app-economy-insights",
>>>               "display_url": "seekingalpha.com/author/app-eco\u2026",              "indices": [
>>>                 0,
>>>                 23
>>>               ]
>>>             }
>>>           ]
>>>         },
>>>         "description": {
>>>           "urls": []
>>>         }
>>>       },
>>>       "protected": false,
>>>       "followers_count": 37364,
>>>       "friends_count": 352,
>>>       "listed_count": 476,
>>>       "created_at": "Fri Apr 03 18:05:20 +0000 2020",
>>>       "favourites_count": 1323,
>>>       "utc_offset": null,
>>>       "time_zone": null,
>>>       "geo_enabled": true,
>>>       "verified": false,
>>>       "statuses_count": 2480,
>>>       "lang": null,
>>>       "status": {
>>>         "created_at": "Tue Oct 11 19:26:24 +0000 2022",
>>>         "id": 1579916343742062592,
>>>         "id_str": "1579916343742062592",
>>>         "text": "@Notnotaburner2 People cut on Doordash and Uber Eats first, it doesn\u2019t mean they are starving \ud83d\ude06",        
>>>         "truncated": false,
>>>         "entities": {
>>>           "hashtags": [],
>>>           "symbols": [],
>>>           "user_mentions": [
>>>             {
>>>               "screen_name": "Notnotaburner2",
>>>               "name": "Notaburner2",
>>>               "id": 1437930278807351298,
>>>               "id_str": "1437930278807351298",
>>>               "indices": [
>>>                 0,
>>>                 15
>>>               ]
>>>             }
>>>           ],
>>>           "urls": []
>>>         },
>>>         "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
>>>         "in_reply_to_status_id": 1579912849157410817,
>>>         "in_reply_to_status_id_str": "1579912849157410817",
>>>         "in_reply_to_user_id": 1437930278807351298,
>>>         "in_reply_to_user_id_str": "1437930278807351298",
>>>         "in_reply_to_screen_name": "Notnotaburner2",
>>>         "geo": null,
>>>         "coordinates": null,
>>>         "place": {
>>>           "id": "5a110d312052166f",
>>>           "url": "https://api.twitter.com/1.1/geo/id/5a110d312052166f.json",
>>>           "place_type": "city",
>>>           "name": "San Francisco",
>>>           "full_name": "San Francisco, CA",
>>>           "country_code": "US",
>>>           "country": "United States",
>>>           "contained_within": [],
>>>           "bounding_box": {
>>>             "type": "Polygon",
>>>             "coordinates": [
>>>               [
>>>                 [
>>>                   -122.514926,
>>>                   37.708075
>>>                 ],
>>>                 [
>>>                   -122.357031,
>>>                   37.708075
>>>                 ],
>>>                 [
>>>                   -122.357031,
>>>                   37.833238
>>>                 ],
>>>                 [
>>>                   -122.514926,
>>>                   37.833238
>>>                 ]
>>>               ]
>>>             ]
>>>           },
>>>           "attributes": {}
>>>         },
>>>         "contributors": null,
>>>         "is_quote_status": false,
>>>         "retweet_count": 0,
>>>         "favorite_count": 2,
>>>         "favorited": false,
>>>         "retweeted": false,
>>>         "lang": "en"
>>>       },
>>>       "contributors_enabled": false,
>>>       "is_translator": false,
>>>       "is_translation_enabled": false,
>>>       "profile_background_color": "F5F8FA",
>>>       "profile_background_image_url": null,
>>>       "profile_background_image_url_https": null,
>>>       "profile_background_tile": false,
>>>       "profile_image_url": "http://pbs.twimg.com/profile_images/1246136989818077184/df6iA4_B_normal.jpg",
>>>       "profile_image_url_https": "https://pbs.twimg.com/profile_images/1246136989818077184/df6iA4_B_normal.jpg",
>>>       "profile_banner_url": "https://pbs.twimg.com/profile_banners/1246136668014301184/1656782898",
>>>       "profile_link_color": "1DA1F2",
>>>       "profile_sidebar_border_color": "C0DEED",
>>>       "profile_sidebar_fill_color": "DDEEF6",
>>>       "profile_text_color": "333333",
>>>       "profile_use_background_image": true,
>>>       "has_extended_profile": true,
>>>       "default_profile": true,
>>>       "default_profile_image": false,
>>>       "following": true,
>>>       "live_following": false,
>>>       "follow_request_sent": false,
>>>       "notifications": true,
>>>       "muting": false,
>>>       "blocking": false,
>>>       "blocked_by": false,
>>>       "translator_type": "none",
>>>       "withheld_in_countries": []
>>>     },
>>>     {
>>>       "id": 1540980192054837248,
>>>       "id_str": "1540980192054837248",
>>>       "name": "vibhi",
>>>       "screen_name": "Vaibhu31012842",
>>>       "location": "",
>>>       "description": "Everyone is beautiful in their own way why cozz god makes no mistakes\u2764",
>>>       "url": null,
>>>       "entities": {
>>>         "description": {
>>>           "urls": []
>>>         }
>>>       },
>>>       "protected": false,
>>>       "followers_count": 2,
>>>       "friends_count": 29,
>>>       "listed_count": 0,
>>>       "created_at": "Sun Jun 26 08:48:56 +0000 2022",
>>>       "favourites_count": 0,
>>>       "utc_offset": null,
>>>       "time_zone": null,
>>>       "geo_enabled": false,
>>>       "verified": false,
>>>       "statuses_count": 0,
>>>       "lang": null,
>>>       "contributors_enabled": false,
>>>       "is_translator": false,
>>>       "is_translation_enabled": false,
>>>       "profile_background_color": "F5F8FA",
>>>       "profile_background_image_url": null,
>>>       "profile_background_image_url_https": null,
>>>       "profile_background_tile": false,
>>>       "profile_image_url": "http://pbs.twimg.com/profile_images/1545812550033498114/r6L1CYxU_normal.jpg",
>>>       "profile_image_url_https": "https://pbs.twimg.com/profile_images/1545812550033498114/r6L1CYxU_normal.jpg",
>>>       "profile_banner_url": "https://pbs.twimg.com/profile_banners/1540980192054837248/1656843967",
>>>       "profile_link_color": "1DA1F2",
>>>       "profile_sidebar_border_color": "C0DEED",
>>>       "profile_sidebar_fill_color": "DDEEF6",
>>>       "profile_text_color": "333333",
>>>       "profile_use_background_image": true,
>>>       "has_extended_profile": true,
>>>       "default_profile": true,
>>>       "default_profile_image": false,
>>>       "following": true,
>>>       "live_following": false,
>>>       "follow_request_sent": false,
>>>       "notifications": false,
>>>       "muting": false,
>>>       "blocking": false,
>>>       "blocked_by": false,
>>>       "translator_type": "none",
>>>       "withheld_in_countries": []
>>>     },
>>>     {
>>>       "id": 1273505391553449985,
>>>       "id_str": "1273505391553449985",
>>>       "name": "Aadit Sheth",
>>>       "screen_name": "aaditsh",
>>>       "location": "Join 14,000 others \u2192 ",
>>>       "description": "20 y/o building internet businesses. I write a 
>>> weekly blog about business & marketing. 14,000 people read it. Try it here \u2192 https://t.co/KmEaUUGDll",
>>>       "url": "https://t.co/KmEaUUGDll",
>>>       "entities": {
>>>         "url": {
>>>           "urls": [
>>>             {
>>>               "url": "https://t.co/KmEaUUGDll",
>>>               "expanded_url": "http://timebillionaires.substack.com",              "display_url": "timebillionaires.substack.com",        
>>>               "indices": [
>>>                 0,
>>>                 23
>>>               ]
>>>             }
>>>           ]
>>>         },
>>>         "description": {
>>>           "urls": [
>>>             {
>>>               "url": "https://t.co/KmEaUUGDll",
>>>               "expanded_url": "http://timebillionaires.substack.com",              "display_url": "timebillionaires.substack.com",        
>>>               "indices": [
>>>                 124,
>>>                 147
>>>               ]
>>>             }
>>>           ]
>>>         }
>>>       },
>>>       "protected": false,
>>>       "followers_count": 215826,
>>>       "friends_count": 255,
>>>       "listed_count": 3511,
>>>       "created_at": "Thu Jun 18 06:39:24 +0000 2020",
>>>       "favourites_count": 26114,
>>>       "utc_offset": null,
>>>       "time_zone": null,
>>>       "geo_enabled": false,
>>>       "verified": false,
>>>       "statuses_count": 4775,
>>>       "lang": null,
>>>       "status": {                                                                            #* for this we uses u['status']['text']
>>>         "created_at": "Tue Oct 11 23:00:09 +0000 2022",
>>>         "id": 1579970137796800512,
>>>         "id_str": "1579970137796800512",
>>>         "text": "RT @aaditsh: The 3 best things to grow your personal brand online:\n\n1. Publish daily.\n2. Make friends.\n3. Be curious 
>>> \u2014 closely analyze and\u2026",
>>>         "truncated": false,
>>>         "entities": {
>>>           "hashtags": [],
>>>           "symbols": [],
>>>           "user_mentions": [
>>>             {
>>>               "screen_name": "aaditsh",
>>>               "name": "Aadit Sheth",
>>>               "id": 1273505391553449985,
>>>               "id_str": "1273505391553449985",
>>>               "indices": [
>>>                 3,
>>>                 11
>>>               ]
>>>             }
>>>           ],
>>>           "urls": []
>>>         },
>>>         "source": "<a href=\"https://tweethunter.io\" rel=\"nofollow\">Tweet Hunter Pro</a>",
>>>         "in_reply_to_status_id": null,
>>>         "in_reply_to_status_id_str": null,
>>>         "in_reply_to_user_id": null,
>>>         "in_reply_to_user_id_str": null,
>>>         "in_reply_to_screen_name": null,
>>>         "geo": null,
>>>         "coordinates": null,
>>>         "place": null,
>>>         "contributors": null,
>>>         "retweeted_status": {
>>>           "created_at": "Tue Oct 11 14:00:04 +0000 2022",
>>>           "id": 1579834221149011968,
>>>           "id_str": "1579834221149011968",
>>>           "text": "The 3 best things to grow your personal brand online:\n\n1. Publish daily.\n2. Make friends.\n3. Be curious \u2014 closely a\u2026 https://t.co/kFwXSkAv5i",
>>>           "truncated": true,
>>>           "entities": {
>>>             "hashtags": [],
>>>             "symbols": [],
>>>             "user_mentions": [],
>>>             "urls": [
>>>               {
>>>                 "url": "https://t.co/kFwXSkAv5i",
>>>                 "expanded_url": "https://twitter.com/i/web/status/1579834221149011968",
>>>                 "display_url": "twitter.com/i/web/status/1\u2026",   
>>>                 "indices": [
>>>                   117,
>>>                   140
>>>                 ]
>>>               }
>>>             ]
>>>           },
>>>           "source": "<a href=\"https://tweethunter.io\" rel=\"nofollow\">Tweet Hunter Pro</a>",
>>>           "in_reply_to_status_id": null,
>>>           "in_reply_to_status_id_str": null,
>>>           "in_reply_to_user_id": null,
>>>           "in_reply_to_user_id_str": null,
>>>           "in_reply_to_screen_name": null,
>>>           "geo": null,
>>>           "coordinates": null,
>>>           "place": null,
>>>           "contributors": null,
>>>           "is_quote_status": false,
>>>           "retweet_count": 10,
>>>           "favorite_count": 118,
>>>           "favorited": false,
>>>           "retweeted": false,
>>> 
>>> Remaining 13
>>> EconomyApp
>>>   @Notnotaburner2 People cut on Doordash and Uber Ea
>>> Vaibhu31012842
>>>    *No status found
>>> aaditsh
>>>   RT @aaditsh: The 3 best things to grow your person
>>> OneJKMolina
>>>   RT @OneJKMolina: My truly unpopular opinion:
>>> 
>>> If y
>>> BrianFeroldi
>>>   @QCompounding I thought it was high revenue growth

"""

######################################################
################# Chapter 14(Python Object)
"""
* An Object is a bit of self-contained Code and Data
* A key aspect of the Object approach is to break the problem into smaller understandable parts(divide and conquer)
* Objects have boundries that allow us to ignore un-needed details
* We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects...
* Objects hide detail - they allow us to ignore the details of the "rest of the program".
"""
"""
* A class - A template-Dog
* Method or Message - A defined capability of a class-barks()
* Field or attribute - A bit of data in a class - length
* Objects or instance:- A particular instance of a class-lassie 
"""

#####################################
## Terminology:Class
"""
Defines tha abstract characteristics of a thing(objects),
including the things characteristics(its attributes,
fields or properties) and the things behaviours(the things it can do,
or methods, operation or features).
One might say that a class is a blueprint or factor that describes the nature of something.
For example, he class Dog would consist of traits shared by all dogs, such as breed and fur color(characteristics), and the ability to bark and sit(behaviours).

"""

## Terminology: Intance
"""
One can have an intance of a class or particular objects,
the intance is the actual object created at runtime.
In programmer jargon, the Lassie object is an instance of dog class.
the set of values of the attributes of a particular object is called its state. 
the object consists of state and behaviour thats defined in the object's class.
* Object and intances are often used interchangably
"""

## Terminology:Method
"""
An object's abilities. In language, methods are verbs. Lassie,being a Dog,
has the ability to bark. So bark() is one of Lassie's methods.
she may have other methods as well, for example sit() or eat() or walk or save_timmy().
within the program, using a method usually affects only one particular object;
all Dogs can bark, but you need only one particular dog to do the barking

"""

###################################################
################# Chapter 14(Python Objects)
##### Sample Code
"""
Class



"""
# class is reserved word
# this is the templete for making PartyAnimal object has a bit of data
class PartyAnimal:
    x = 0  # Each PartyAnimal  object has a bit of data 
    def party(self):
        self.x = self.x +1
        print("So far",self.x)
an = PartyAnimal() #Construct a PartyAnimal object and store in an 
an.party()
an.party() # PartyAnimal.party(an)
an.party()


# A Nerdy Way to Find Capabilities
"""
* The dir() command lists capabilities
* Ignore the ones with underscores these are used by python itself
* The rest are real operations that the object can perform
* It is like type()- it tells us something *about* a variable
"""
#@
x = list()
type(x)
#>>> <type 'list'>
print(dir(x))
"""
>>> ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
>>> '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
>>> '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
>>> '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
>>> '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
>>> '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
>>> 'remove', 'reverse', 'sort']
"""

#@
y = 'Hello there'
print(dir(y))
"""
PS C:\VsCode> python -u "c:\VsCode\py4e\tempCodeRunnerFile.py"
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
# an.x or an.party dot is object operator object lookup operator
#@
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
an = PartyAnimal()
print("Type", type(an))
print("Dir", dir(an))
"""
Type <class '__main__.PartyAnimal'>
Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', 'party', 'x']
"""

        
###########################################
################# Chapter 14(Objects)
## Object Lifecycle
"""
* Objects are created, used and discarded
* We have special bloks of code(method) that get called
    * At the moment of creation(constructor)
    * At the moment of destruction(destruction)
* Constructors are used a lot
* Destructors are seldom used
""" 

#@ Construcor
"""
* The primary purpose of the constructer is to set up some instance variable to have the proper initial
* -values when the object is created
"""

#@ 
class PartyAnimal:
    x = 0
    def __inti__(self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)
"""
>>> So far 1
>>> So far 2
>>> I am destructed 2
>>> an contains 42  
"""

#@
class PartyAnimal:
    x = 0
    def __init__(self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    def __del__(self):
        print('I am destructed', self.x)
an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
"""
>>> I am constructed
>>> So far 1
>>> So far 2
>>> I am destructed 2
>>> an contains 42   
"""

#@ Constructer
"""
* In object oriented programming, a constructer in class is a special block of statements called when objects are created
Many Instances
* We can create lots of objects - the class is the templete for the object
* We can store each distinct object in its own variable 
* We call this having multiple instances of the same class
* Each instance has its own copy of the instance variable
"""

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")
        
    def party(self):
        self.x = self.x + 1
        print(self.name,"party count", self.x)
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()
"""
>>> Sally constructed  
>>> Sally party count 1
>>> Jim constructed    
>>> Jim party count 1  
>>> Sally party count 2
"""
# Contructors can have additional parameters, These can be used to set up intances varibles for the particular instances of the class(i.e.. for the particular object) 

#################################################
###@ Python objects(Inheritance)
"""
* When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
* Another form of store and reuse
* Write once - reuse many times
* The new class (child) has all the capabilities of the old class(parent) - and then some more

"""
# Terminology:Inheritance
"""
* Subclasses are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.

"""

#@ Definitions
"""
* Class - a template
* Attribute - A variable within a class
* Method - A function within a class
* object - A particular instance of a class
* contructor - Code that runs when object is created
* Inheritance - The ability to extend a class to make a new class 
"""

#################################################
########### Chapter 15 (Databases)
"""
* Databases - Contains many tables
* Relation(or table) - contain tuples and attribbutes
* Tuple(or row) - a set of fields that generally represents an objects like a person or a music track
* Attribute(also colomn or field) - one of possibly many elements data corresponding to the object represented by the row
"""

# SQL
"""
* Structured Query Language is the languge we use to issue commands to the databses
* Create a table
* Retrieve some data
* Insert table
* Delete data
(CRUD)
"""

#Web Application w/Databases
"""
* Applicattion Devloper - Build the logic for the applicattion, the look and ffeel of the application - monitors the applicattion for problems
* Databases Administrater - Monitors and adjusts the daabases as the programs runs in producction
* Often both people participate in the building of the "Data Model
"""

#@ Common Databases System
"""
Three major Databases Management System in wide use
* Oracle - Large, commercial, enterprise-scale, very very tweakable
* MySql - Simpler but very fast and scalable -commercial open source
* SqlServer - Very nice - from Microsoft(Also Access)
* Many other smaller projects, free and open source
* ---HSQL, SQlite, Postgress,....

"""

############################################
######### Chapter 15(DATABASES)
#@ SQLite Browser 9.36
# Sqlite is a very popular database - it is free and fast and small
# sqlite Browser allows us to directly manipulate sqlite files
# SQLite is embedded in python and a number of other languages
##################################
#SQL (CRUD) Create Read Update Delete
#SQL : Insert
"""
* The insert statement inserts a row into a table
* "(INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu'))"
"""

"""
thon for Everybody Database Handout

https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt

Download and Install: http://sqlitebrowser.org/

* CREATE TABLE "Users" ("name" TEXT, "email" TEXT)

SQL: Insert
# (The Insert statement inserts a row into table)

INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu')
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu')
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu')

SQL: Delete
#(Deletes a row in a table based on a selection criteria)
* DELETE FROM Users WHERE email='ted@umich.edu'


SQL: UPDATE
* UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'


SQL: Retrieving Records : 
* The select statement retrieves a group of records - you can either retrieve all the records or a subsets of records with a where clause 
* SELECT * FROM Users
* SELECT * FROM Users WHERE email='csev@umich.edu'
* SELECT * FROM Users ORDER BY email
* SELECT * FROM Users ORDER BY name DESC

Multi-Table SQL:

CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    artist_id INTEGER,
    "title" TEXT)

CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, 
    "title" TEXT, "count" INTEGER)

INSERT INTO Artist (name) VALUES ('Led Zepplin')
INSERT INTO Artist (name) VALUES ('AC/DC')

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;

SELECT Album.title, Artist.name FROM Album JOIN Artist 
    ON Album.artist_id = Artist.id

SELECT Album.title, Album.artist_id, Artist.id, Artist.name 
    FROM Album JOIN Artist ON Album.artist_id = Artist.id

SELECT Track.title, Track.genre_id, Genre.id, Genre.name 
    FROM Track JOIN Genre   

SELECT Track.title, Genre.name FROM Track JOIN Genre 
    ON Track.genre_id = Genre.id

SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id


Many-Many Relationship

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) ;

INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name 

"""

# This is not too exciting (So far)
"""
* Tables pretty much look like big fast programmable spreadsheet with rows, columns, and commands  
* The power comes when we have more than one table and we can exploit the relationnships between the tables
"""

##########################################
#### Chapter 15(Databases) Code sample emaildb.py
import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute('''
            CREATE TABLE Counts (
                email TEXT,
                count INTEGER)''')
fname = input("Enter a file name: ")
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    line = line.strip()
    words = line.split()
    email = words[1]
    print(email)
    cur.execute('SELECT count from Counts WHERE email = ?',(email,)) #its actually not really retrievening/reading data its like the opening of file or set of records  Here ? markhere is placeholder 
    row = cur.fetchone() #note here if we consider all instead of one then it would give empty box
    print(row)
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count)
                VALUES(?, 1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
        
    conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()



######################################
############ Chapter 15(Databases)
## Code sample twspider.py
from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT,
            retrieved INTEGER,
            friends TEXT)''')
# >>>Ignore SSL Certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter account found')
            continue

    url = twurl.augment(TWITTER_URL,{'screen_name':acct, 'count':5})
    print('Retrieving',url)
    connection = urlopen(url, context = ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent = 4)
    cur.execute('UPDATE Twitter SET retrieved = 1 WHERE name = ?',(acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                    (count + 1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                    VALUES(?,0,1)''',(friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, 'revisited',countold)
    conn.commit()
cur.close()


######################################################
######################################################
########### Database (Database Design)
"""
* Database design is an art form of its own with particular skills and experience
* Our goal is to avoid the really bad mistakes and design clean and easily understood databases
* other may performance tune things later
* Database design starts with a picture....
"""

######################################################
######### Building a Data Model
"""
* Drawing a picture of the data objects for our application and then figuring out how to represent the objects and their relationship
* Basic Rule: Don't put the same string data in twice- use a relationship instead
* When there is one thing in the "real world" there should be one copy of that thing in the database
"""

#####################################################
########## For each "piece of info"
"""
* Is the column an object or an attribute of another onject?
* Once we define objects, we need to define the relationships between objects.
"""


###################################################
###################################################
########## Chapter 15(Databases)
# Representing relationships
"""
Database Normalization(3NF)
* There is *tons* of database theory - way too much to understand without excessive predicate calculas
* Do not replicate data - reference data - point at data
* Use integers for keys and for references
* Add a special "key" column to each table which we will make reference to. By convention, many programmers call this column "id"
* we use integer to refernece rows in another table

Three Kinds of keys
* Primary keys - genrally an integer auto-increment field
* Logical key - What the outside world uses for lookup
* Foreign key - generally an integer key pointing to a row in another table

"""

"""
Keys Rules
* Never use your logical keys as the primary key
* Logical keys can and do change, albeit slowly
* Relationships that are based on matching string fields are less efficient than integers
"""

################################################
#@Foreign Keys
"""
                                                                                                                    #   |Artist|    | AlbumId    |                                                           
* A foreign key is when a table has a column that contains a key which points to the primary key of another table   #   |id    |    |  id        |                                                                 
                                                                                                                    #   |name  |    |  title     |                                                    
                                                                                                                    #   |......|    |  artist_id |                                                           
* When all primary keys are integers, then all foreign keys are integers - this is good - very good                 #               |  ....      |                                               
                                                                                                                    #               |            |                                        
"""

######################################
####################### Databases
# Relationship building 
#We are gonna build track table
############################################################CodeImage1
"""              belongs - to
Album ----------------------------------| -Track-|                                                                                      
                                        | Title  |                                             
                                        | Rating |                                              
                                        | Len    |      | Track     |                              
                                        | Count  |      |  id       |                              
                    |-Album -|                          |  title    |                                 
                    |  id    |                          |  rating   |                               
Table               |  title |   \===--------------      |  len      |                                                                 
Primary key                                        \    |  count    |                                     
Logical key                                         \-  |  album_id |   foreign key                                     
Foreign                                                                                        
                                                                                        
                                                                                                                                        
"""

#######################################
############################ Databases(Join operation)
"""
Relational power
* By removing the replicated data and replacing it with references to a single copy of each bit of data
* - we build a "web" of information that the relational database can read through very quickly - even for very large amounts of data
* Often when you want some data it comes from a number of tables linked by these foreign keys
"""

## The JOIN Operation
"""
* The JOIN operation limks across several tables as part a select operation
* You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause
"""
##########################################################################CodeImage2
##########################################################################CodeImage2
"""
As in Image shown
* select Album.title, Artist.name from Album join Artist on    Album.artist_id = Artist.id
    What we want to see            the table that hold the data            how the tables are linked 
"""


##########################################################################CodeImage3
##########################################################################CodeImage3
"""
As in upper image shown
* select Album.title, album.artist_id, Artist.id, Artist.name
* -from Album join Artist on Album.artist_id = Artist.id
"""

#Note:- Joining two tables without an ON clause gives all possible combinations of rows.
##########################################################################CodeImage4
##########################################################################CodeImage4
"""
As in upper image shown
* SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre
"""

##########################################################################CodeImage5
##########################################################################CodeImage5
"""
As in upper image shown
* SELECT Track.title, Genre.name     from Track join Genre on           Track.genre_id = Genre.id
    what we want to see                  The tables that hold the data           How the tables are linked
"""

##########################################################################CodeImage6
##########################################################################CodeImage6
"""
As in upper image shown
* select Track.title, Artist.name, Album.title, Genre.name from Track join Genre join Album join Artist on
* -Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id


    what we want to see                  The tables that hold the data           How the tables are linked
"""



####################################################
################## Chapter 15(Databases)
## Code Sample (tracks.py)
import xml.etree.ElementTree as ET
import sqlite3
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "Library.xml"

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d,key):
    found = False
    for child in d:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry,'play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None :
        continue
    print(name, artist,album, count, rating, length)
    cur.execute('''INSERT OR IGNORE INTO Artist(name)
            VALUES(?)''',(artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id)
            VALUES(?,?)''',(album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?',(album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track
                (title, album_id, len,rating, count)
                VALUES(?,?,?,?,?)''',
                (name,album_id,length,rating,count))
    conn.commit()

"""
#* SELECT Track.title, Album.title, Artist.name FROM Track JOIN Album JOIN Artist ON
#* -- Track.album_id = album_id AND Album.artist_id = Artist.id
"""

#############################################
##################### Databases
#### Many-To-Many(Relationship)
############################################
############################# CodeImage6
############################################
"""
Many to Many
* Sometimes we need to model a relationship that is many to many
* We need to add a "connection" table with two foreign keys 
* There is usually no separate primary key
"""

############################################
############################# CodeImage7
############################################
"""
SELECT User.name, Member.role, Course.title FROM User JOIN Member JOIN Course ON Member.user_id = User.id AND
Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name

"""

"""
Complexity Enables Speed
* Complexity makes speed possible and allows you to get very fast results as the data size grows
* By normalizing the data and linking it with integer keys, the overall amount of data which the relational databases must scan is far lower than
* - if the data were simply flatted out
* It might seem like a tradeoff - spend some time designing your databases so it continues to be fast when your application is a success.

"""

############################################
######## Additional SQL Topic
"""
* Indexes improve access performance for things like strings fields
* Constraints on data - (cannot be NULL, etc...)
* Transactions - allow SQL operations to be grouped and done as a unit 
"""

"""
Summary:-
* Relational databases allow us to scale to very large amounts of data 
* The key is to have one copy of any data element and use relations and joins to link the data to multiple places
* This greatly reduces the amount of data which much be scanned when doing complex operations across large amounts of data .
* Database and SQL design is a bit of an art form
"""

##########################################
########### Chapter 15(Databases)
# Code Sample roster.py

import json
import sqlite3
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()
# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member(
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY(user_id, course_id)
)
''') 
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = 'roster_data_sample.json'

# [
# ["Charley", "still0", 1],
# ["Mea", "still0", 0]
str_data = open(fname).read()
json_data = json.loads(str_data)
for entry in json_data:
    name = entry[0]
    title = entry[1] 
    print(name, title)
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES(?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Course(title)
        VALUES(?)''',(title,))
    cur.execute('SELECT id FROM Course WHERE title = ?',(title,))
    course_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Member  
                (user_id, course_id) VALUES(?,?)''',
                (user_id, course_id))
    conn.commit()
    
    
# Error : ## if you put here IGNORE you will get error
""" Error is Traceback (most recent call last):
File "c:\VsCode\py4e\tempCodeRunnerFile.py", line 52, in <module>
cur.execute('''INSERT OR IGNORE INTO Member
sqlite3.InterfaceError: Error binding parameter 1 - probably unsupported type.
"""



#############################################
############## Chapter 15(Databases) Code sample twspyder.py
## twfriends.py
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute(''' CREATE TABLE IF NOT EXISTS Follows
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    acct = input('Enter a twitter account: ')
    if (acct == 'quit'): break
    if (len(acct)) < 1:
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1 ')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter account')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) Values(?, 0)''',(acct,))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving account', acct)
    ### """
    ### try:
    ###     connectionn = urllib.request.urlopen(url, context)
    ### except Exception as err:
    ###     print('Failed to retrieve',err)
    ###     break
    ### """
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    
    print('Remaining', headers['x-rate-limit-remaining'])
    
    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break
    
    # Debugging
    # print(json.dumps(js, indent= 4))
    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent = 4))
        continue
    cur.execute('UPDATE People SET retrieved = 1 WHERE name = ?', (acct,))
    
    countnew = 0 
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People(name, retrieved)
                        VALUES(?, 0)''',(friend, ) )
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:',friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows(from_id, to_id)
                    VALUES(?,?)''',(id, friend_id))
    print('New accounts = ', countnew, 'revisited=', countold)
    conn.commit()
cur.close()
            
            

        
        
    
        
            


#######################################################
##################################
##################################
## Chapter 16(Data Visualization)
# Retrieving and vizualizing
# Many Data Mining Technology
"""
https://hadoop.apache.org/
https://spark.apache.org/
https://aws.amazon.com/redshift/
http://community.pentaho.com/


...
"""

# Personal Data Mining
#* Our goal is to make better programmmers- not to make you data mining experts

#GeoData
"""
* Makes a Google Map from user entered data
* Uses the google Geodata API
* Cashes data in a databases to avoid rate limiting and allow restarting
* Visualized in a browser using the google Maps API

"""


################################################
################################################
############################ Code Sample(geodata)
### Chapter 16
"""
Using the Google Places API with a Database and
Visualizing Data on Google Map

In this project, we are using the Google geocoding API
to clean up some user-entered geographic locations of
university names and then placing the data on a Google
Map.

Note: Windows has difficulty in displaying UTF-8 characters
in the console so for each command window you open, you may need
to type the following command before running this code:

    chcp 65001

http://stackoverflow.com/questions/388490/unicode-characters-in-windows-command-line-how


You should install the SQLite browser to view and modify
the databases from:

http://sqlitebrowser.org/

The first problem to solve is that the Google geocoding
API is rate limited to a fixed number of requests per day.
So if you have a lot of data you might need to stop and
restart the lookup process several times.  So we break
the problem into two phases.

In the first phase we take our input data in the file
(where.data) and read it one line at a time, and retrieve the
geocoded response and store it in a database (geodata.sqlite).
Before we use the geocoding API, we simply check to see if
we already have the data for that particular line of input.

You can re-start the process at any time by removing the file
geodata.sqlite

Run the geoload.py program.   This program will read the input
lines in where.data and for each line check to see if it is already
in the database and if we don't have the data for the location,
call the geocoding API to retrieve the data and store it in
the database.

As of December 2016, the Google Geocoding APIs changed dramatically.
They moved some functionality that we use from the Geocoding API
into the Places API.  Also all the Google Geo-related APIs require an
API key. To complete this assignment without a Google account,
without an API key, or from a country that blocks
access to Google, you can use a subset of that data which is
available at:

http://py4e-data.dr-chuck.net/json

To use this, simply leave the api_key set to False in 
geoload.py.

This URL only has a subset of the data but it has no rate limit so
it is good for testing.

If you want to try this with the API key, follow the
instructions at:

https://developers.google.com/maps/documentation/geocoding/intro

and put the API key in the code.

Here is a sample run after there is already some data in the
database:

Mac: python3 geoload.py
Win: geoload.py

Found in database  Northeastern University

Found in database  University of Hong Kong, Illinois Institute of Technology, Bradley University

Found in database  Technion

Found in database  Viswakarma Institute, Pune, India

Found in database  UMD

Found in database  Tufts University

Resolving Monash University
Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=Monash+University
Retrieved 2063 characters {    "results" : [
{u'status': u'OK', u'results': ... }

Resolving Kokshetau Institute of Economics and Management
Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=Kokshetau+Institute+of+Economics+and+Management
Retrieved 1749 characters {    "results" : [
{u'status': u'OK', u'results': ... }

The first five locations are already in the database and so they
are skipped.  The program scans to the point where it finds un-retrieved
locations and starts retrieving them.

The geoload.py can be stopped at any time, and there is a counter
that you can use to limit the number of calls to the geocoding
API for each run.

Once you have some data loaded into geodata.sqlite, you can
visualize the data using the (geodump.py) program.  This
program reads the database and writes tile file (where.js)
with the location, latitude, and longitude in the form of
executable JavaScript code.

A run of the geodump.py program is as follows:

Mac: python3 geodump.py
Win: geodump.py

Northeastern University, 360 Huntington Avenue, Boston, MA 02115, USA 42.3396998 -71.08975
Bradley University, 1501 West Bradley Avenue, Peoria, IL 61625, USA 40.6963857 -89.6160811
...
Technion, Viazman 87, Kesalsaba, 32000, Israel 32.7775 35.0216667
Monash University Clayton Campus, Wellington Road, Clayton VIC 3800, Australia -37.9152113 145.134682
Kokshetau, Kazakhstan 53.2833333 69.3833333
...
12 records written to where.js
Open where.html to view the data in a browser

The file (where.html) consists of HTML and JavaScript to visualize
a Google Map.  It reads the most recent data in where.js to get
the data to be visualized.  Here is the format of the where.js file:

myData = [
[42.3396998,-71.08975, 'Northeastern University, 360 Huntington Avenue, Boston, MA 02115, USA'],
[40.6963857,-89.6160811, 'Bradley University, 1501 West Bradley Avenue, Peoria, IL 61625, USA'],
[32.7775,35.0216667, 'Technion, Viazman 87, Kesalsaba, 32000, Israel'],
   ...
];

This is a JavaScript list of lists.  The syntax for JavaScript
list constants is very similar to Python so the syntax should
be familiar to you.

Simply open where.html in a browser to see the locations.  You
can hover over each map pin to find the location that the
geocoding API returned for the user-entered input.  If you
cannot see any data when you open the where.html file, you might
want to check the JavaScript or developer console for your browser.
"""
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
#If you have a places API key, enter it here
# api_key = 'AIzaSy__IDByT70

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    
    
#Additional details for urllib
#http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations(address TEXT,  geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        print('Retrieved 200 locations, restart to retrieve')
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address = ?",
                (memoryview(address.encode()),))
    try:
        data = cur.fetchone()[0]
    except:
        pass
    
    parms = dict()
    parms["query"] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'character', data[:20].replace('/n',''))
    count = count + 1
    
    try:
        js = json.loads(data)
    except:
        print(data) #We print in case un
        continue
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('=== Failure To Retrieve===')
        print(data)
        break
    cur.execute('''INSERT INTO Locations(address, geodata)
                VALUES(?,?)''', (memoryview(address.encode()), memoryview(data.encode())))
        
    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit...')
        time.sleep(2)
print("Run geodump.py to read the data from the databases so you can visualized")


################################################
################################################
###################### geoload.py
import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w',"utf-8")
fhand.write('myData = [\n')
count = 0
for row in cur:
    data = str(row[1].decode())
    try:
        js = json.loads(str(data))
    except:
        continue
    if not('status' in js and js['status'] == 'OK'):
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 :
        continue
    where = js["results"][0]["formatted_address"]
    where = where.replace("'","")
    try:
        print(where, lat, lng)
        count = count + 1
        
        if count > 1:
            fhand.write(", \n")
        output = "[" + str(lat) +", " + str(lng) +", '"+where+"' ]"
        fhand.write(output)
    except:
        continue
fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")



###########################################
###########################################
####################### Chapter 16(Data Visualization)
### Page Rank
"""
* Write a simple web page crawler
* Compute a simple version of Google's Page Rank algorithm
* Visualize the resulting network


Search Engine Architecture
* Web Crawling
* Index Building
* Searching
"""

# Web Crawler
"""
A Web crawler is a computer program that broweses the world wide web in a methodical,
automated manner. Web crawlers are mainly used to create a copy of all the visted pages
for later processing by a search engine that will index the downloaded pages to provide fast searches 

Web Crawler
* Retrieve a page
* Look through the page for links
* Add the links to a list of "to be retrieved" sites
* Repeat


Web Crawling Policy
* A "selection policy" that states which pages to downloaded,
* A "re-visit policy" that states when to check for changes to the pages
* A "politeness policy" that states how to avoid overloading websites, and
* A "parallelization policy" that states how to coordinate distributed web crawlers

"""

"""
Robots.txt
* A way for a website to communicate with web crawlers
* An informal and voluntary standard
* Sometimes folks make a " Spider Trap" catch "bad" spiders
"""

"""
Search Indexing;-
                Search engine indexing collects, parses, and stores data to facilitate fast and accurate
                information retrievel. The purpose of storing an index is to 
                optimize speeed and performance in finding relevent documents for a search
                query. Without an index, the search engine would scan every document in the
                corpus, which would require considerable time and computing power.
                
"""

#################################################
#################################################
####################### Spider.py
import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Ignore SSL certificate errors
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Pages
            (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
        error INTEGER, old_rank REAL, new_rank REAL)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Links
        (from_id INTEGER, to_id INTEGER,  UNIQUE(from_id, to_id))''')

cur.execute('''CREATE TABLE IF NOT EXISTS Webs(url TEXT UNIQUE)''')

# check to see if we are already in progress...
cur.execute('SELECT id, url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1 ')
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl. Remove spider.sqlite to start a fresh  ")
else:
    starturl = input("Enter web url or enter: ")
    if (len(starturl)) < 1: starturl = 'http://www.dr-chuck.com/'
    if (starturl.endswith('/')) : starturl = starturl[:-1]
    web = starturl
    if (starturl.endswith('.htm')) or (starturl.endswith('.html')) :
        pos = starturl.rfind('/')
        web = starturl[:pos]
    if (len(web)>1):
        cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES( ? )', (web, ))
        cur.execute('INSERT OR IGNORE INTO Pages(url,html, new_rank) VALUES(? , NULL, 1.0)', (starturl,))
        conn.commit()
        
# Get the current webs
cur.execute('''SELECT url FROM Webs''')
webs = list()
for row in cur:
    webs.append(str(row[0]))

print(webs)

many = 0
while True:
    if (many < 1):
        sval = input('How many pages:')
        if (len(sval) < 1): break
        many = int(sval)
    many = many - 1
    
    cur.execute('SELECT id, url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cur.fetchone()
        # print(row)
        fromid = row[0]
        url = row[1]
        
    except:
        print('No unretrieved HTML pages found')
        many = 0
        break
    
    print(fromid, url, end = ' ')
    
    # If we are retrieving this page, there should be no links from it 
    cur.execute('DELETE from Links WHERE from_id = ?', (fromid,))
    try:
        document = urlopen(url, context=ctx)
        
        html = document.read()
        if document.getcode() !=200:
            print("Error on page:", document.getcode())
            cur.execute('UPDATE Pages SET error = ? WHERE url = ?', (document.getcode(), url))
        
        if 'text/html' != document.info().get_content_type():
            print("Ignore non text/html page")
            cur.execute('DELETE FROM Pages WHERE url = ?',(url,))
            conn.commit()
            continue

            
        print('('+str(len(html))+')', end= ' ')
        soup = BeautifulSoup(html, "html.parser")
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by year...')
        break
    except:
        print('Unable to retrieve or parse page')
        cur.execute('UPDATE Pages SET error = -1 WHERE url = ?',(url,))
        conn.commit()
        continue
    
    cur.execute('INSERT OR IGNORE INTO Pages(url,html, new_rank) VALUES(?, NULL, 1.0)',(url,))
    cur.execute('UPDATE Pages SET html = ? WHERE url = ?',(memoryview(html),  url))
    conn.commit()
    
    #Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href',None)
        if (href is None):
            continue
        # Resolve relative references like href="/contact"
        up = urlparse(href)
        if (len(up.scheme) < 1):
            href = urljoin(url, href)
        ipos = href.find('#')
        if (ipos > 1):
            href = href[:ipos]
        if (href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif')):
            continue
        if (href.endswith('/')):
            href = href[:-1]
        # print href
        if (len(href) < 1):
            continue
        # check if the URL is in any of the webs
        found = False
        for web in webs:
            if (href.startswith(web)):
                found = True
                break
        if not found:
            continue
        
        cur.execute('INSERT OR IGNORE INTO Pages(url, html, new_rank) VALUES(? , NULL, 1.0)', (href,))
        count = count + 1
        conn.commit()
        cur.execute('SELECT id FROM Pages WHERE url = ? LIMIT 1', (href,))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id ')
            continue
        # print fromid toid
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES(?, ?)', (fromid, toid))
        
    print(count)
cur.close()

###################################################
###################################################
############################ (Pagerank computation)
#### Chapter 16 
import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
cur.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids = list()
for row in cur: 
    from_ids.append(row[0])

# Find the ids that receive page rank 
to_ids = list()
links = list()
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id : continue
    if from_id not in from_ids : continue
    if to_id not in from_ids : continue
    links.append(row)
    if to_id not in to_ids : to_ids.append(to_id)

# Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    cur.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node, ))
    row = cur.fetchone()
    prev_ranks[node] = row[0]

sval = input('How many iterations:')
many = 1
if ( len(sval) > 0 ) : many = int(sval)

# Sanity check
if len(prev_ranks) < 1 : 
    print("Nothing to page rank.  Check data.")
    quit()

# Lets do Page Rank in memory so it is really fast
for i in range(many):
    # print prev_ranks.items()[:5]
    next_ranks = dict();
    total = 0.0
    for (node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[node] = 0.0
    # print total

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
        # print node, old_rank
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node : continue
        #  print '   ',from_id,to_id

            if to_id not in to_ids: continue
            give_ids.append(to_id)
        if ( len(give_ids) < 1 ) : continue
        amount = old_rank / len(give_ids)
        # print node, old_rank,amount, give_ids
    
        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount
    
    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank
    evap = (total - newtot) / len(next_ranks)

    # print newtot, evap
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap

    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank

    # Compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank-new_rank)
        totdiff = totdiff + diff

    avediff = totdiff / len(prev_ranks)
    print(i+1, avediff)

    # rotate
    prev_ranks = next_ranks

# Put the final ranks back into the database
print(list(next_ranks.items())[:5])
cur.execute('''UPDATE Pages SET old_rank=new_rank''')
for (id, new_rank) in list(next_ranks.items()) :
    cur.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
conn.commit()
cur.close()



################################
################################
############### spreset.py
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('''UPDATE Pages SET new_rank = 1.0, old_rank = 0.0 ''')
conn.commit()
cur.close()
print('All pages set to a rank of 1.0')


###################################################
###################################################
####################### Pagerank Visualization 
####### Chapter 16

#############(spdump.py)
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
        FROM Pages JOIN Links on Pages.id = Links.to_id
        WHERE html IS NOT NULL
        GROUP BY id ORDER BY inbound DESC''')
count = 0
for row in cur:
    if count < 50:
        print(row)
    count = count + 1
print(count, 'rows.')
cur.close()


##############################################
########################################
####################### spjson.py
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

print("Creating JSON output on spider.js... ")
howmany = int(input("How many nodes? "))
cur.execute(''' SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
            FROM Pages JOIN Links ON Pages.id = Links.to_id
            WHERE html IS NOT NULL AND ERROR IS NULL
            GROUP BY id ORDER BY id,inbound
            ''')
fhand = open('spider.js','w')
nodes = list()
maxrank = None
minrank = None
for row in cur:
    nodes.append(row)
    rank = row[2]
    if maxrank is None or maxrank < rank:
        maxrank = rank
    if minrank is None or minrank > rank:
        minrank = rank
    if len(nodes) > howmany:
        break

if maxrank == minrank or maxrank is None or minrank is None:
    print("Error - please run sprank.py to compute pagerank")
    quit()
    
fhand.write('spiderJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()
for row in nodes:
    if count > 0:
        fhand.write(',\n')
        # print row
    rank = row[2]
    rank = 19*((rank - minrank)/(maxrank-minrank))
    fhand.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
    fhand.write('"id":'+str(row[3])+',"url":"'+ row[4]+'"}')
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
fhand.write('],\n')

cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
fhand.write('"links:[\n')

count = 0
for row in cur:
    # print row
    if row[0] not in map or row[1] not in map:
        continue
    if count > 0:
        fhand.write(',\n')
    rank = ranks[row[0]]
    srank = 19*((rank - minrank)/(maxrank-minrank))
    fhand.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
    count = count + 1
fhand.write(']};')
fhand.close()
cur.close()

print("Open force.html in a browser to view the visualization")

##############################################
###########################################
######################################### Chapter16
################ DataVisualization (Mailing List Crawl)
""" 
Mailing Lists-Game::-
                        *crawl the archieve of a  mailing list
                        *Do some analysis/cleanup
                        *Visualise the data as word cloud and lines
                        
"""

"""
Warning: This Dataset is > 1gb
* Do not just point this application at gmane.org and let it run.
* There is no rate limit - these are cool folks
* Use this foe texting:
                    http://mbox.dr-chuck.net/sakai.devel/4/5
"""

############################################
########################## Gmane.py (Data Retrievel)
################ https://www.py4e.com/code3.zip
############ Chapter 16
#Gmane.py
import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
#Not all systems have this so conditionaly define parser
try:
    import dateutil.parser as parser
except:
    pass

def parsemaildate(md):
    # See if we have dateutill
    try:
        pdate = parser.parse(tdate)
        test_at = pdate.isoformat()
        return text_at
    except:
        pass
    #Non-dateutil version - we try our best
    pieces = md.split()
    notz = " ".join(pieces[:4]).strip()
    # Try a bunch of format variations-strptime() is *lame*
    dnotz = None
    for form in []

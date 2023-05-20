print("hello world!")
formatter = "{} {} {} {} {}"
print(formatter.format(1,2,3,4,5))
days = "Mon Tue Wed Thu Fri Sat Sun"
month = "Jan\tFeb\tmar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec"
print("Here is days",days)
print("Here is month",month)



#Notable
print(None == False)
# >>>False
print(None == True)
# >>>False
print(False==0)
# >>>True
print(True==1)
# >>>True


#NOTE:=cursor.execute("UPDATE Names SET FirstName = "Tony" WHERE ID = 1 ") in double quotes["] always use single quotes[']

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
"""
        I'm tabbed in.
I'm split      
on a line.     
I'm \ a \ cat. 

I'll do a list:
        * Cat food
        * Fishies
        * Catnip
        * Grass
"""

##@
word = input("Enter word: ")
wrd = word[1:]
for i in wrd:
    print("\t",i)
"""
>>> Enter word: Abhishek
>>>          b
>>>          h
>>>          i
>>>          s
>>>          h
>>>          e
>>>          k
"""

#@
x = [154,634,892,345,341,43]
print(len(x))
print(x[1:4])
for i in x:
    print(i)
num = int(input("Enter number: "))
if num in x:
    print(num,"is in the list")
else:
    print("Not in the list")
x.insert(2,420)    
print(x)
x.remove(892)
print(x)
x.append(993)
print(x)

#@
fav_sub = input("Enter your favorite subject: ")
for letter in fav_sub:
    print(letter,end = "-")
"""
>>> Enter your favorite subject: Math
>>> M-a-t-h-
"""

#@
mssg = input("Enter a word in uppercase: ")
# if word.isupper():
while mssg.islower():
    mssg = input("try again: ")
print("thank you")
# >>> thank you


#@
postcode = input("Enter Postcode: ")
ans = postcode[:2]
print(ans.upper())




#@
msg = "hello"
if msg.isupper():
    print("Uppercase")
else:
    print("This is not in uppercaase")
# >>>This is not in uppercaase

#@
msg = "hello"
msg.islower()
msg = "hello" 
for letter in msg:
    print(letter,end = "*")

#@
msg = "abhishek you are totally addicted stop this"
print(msg.capitalize())
print(msg.title())
"""
>>> Abhishek you are totally addicted stop this
>>> Abhishek You Are Totally Addicted Stop This
"""

#@
subjects = ["math","computerscience","physicks","chemistry","biology","botany"]
user = input("Enter the subject which one you do not like: ")
sub = subjects.index(user)
del subjects[sub]
print(subjects)
"""
>>> Enter the subject which one you do not like: math
>>> ['computerscience', 'physicks', 'chemistry', 'biology', 'botany']
"""


#@
colors = ["red", "green", "blue", "yellow", "black", "white","brown","orange","grey","sky"]
start = int(input("Enter number beetween 0 and 4: "))
end = int(input("Enter number beetween 5 and 9: "))
print(colors[start:end])



#@
num1= int(input("Enter a number: "))
total = num1
question = (input("Do you want add another number(y/n) : "))
while question == "yes":
    num = int(input("Enter a number: "))
    total = total+num
    question = (input("Do you want add another number(y/n) : "))
print("total is",total)

#@
num1= int(input("Enter a number: "))
total = num1
question = "yes"
while question == "yes":
    num2 = int(input("Enter a number: "))
    total = total+num2
    question = (input("Do you want add another number(y/n) : "))
print("total is",total)


#@
import turtle
turtle.Screen().bgcolor("blue")
turtle.begin_fill()
turtle.color("green", "yellow")
for i in range(1,5):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.Screen().bgcolor("blue")
turtle.begin_fill()
turtle.color("green", "red")
for i in range(1,5):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.Screen().bgcolor("blue")
turtle.begin_fill()
turtle.color("green", "pink")
for i in range(1,5):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.exitonclick()

##import turtle
# scr = turtle.Screen()
# scr.bgcolor("blue","yellow")
turtle.Screen().bgcolor("green")
turtle.begin_fill()
turtle.pensize(3)
turtle.color("blue","yellow")
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)
turtle.end_fill()
turtle.exitonclick()


################################
def get_data():
    num = int(input("Enter number: "))
    return num 


def answer(num):
    for i in num: #num not be integer should be list stirng tupple dic....
        print(i)
        
    # for i in num:
# TypeError: 'int' object is not iterable

################################


####################################################
####################################################

list1 = range(1, 51) 
sum1 = sum(list1) 
print(sum1) 
    
    
num = 50
a = 1
sum = num/2*(a+1)
print(sum)

num = 50 # where num is number of terms and last term 
a = 1 # a is first term 
sum = num//2*(50+1) 
print(sum)

res = 0
for i in range(1,51):
    res = res +i
print(res)

print(sum(range(1,51)))
'''
5 + sum(4)[10]  =15
4 + sum(3)[6]  =10
3 + sum(2)[3]  =6
2 + sum(1)[1]  =3
1
'''

#
def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)
add = sum(5)
print(add)


#
def get_name():
    num= int(input('Enter the number: '))
    return num

#
def count(num):
    sum = 0 
    for i in range(1, num+1):
        print(i)
        sum = i + sum
    print(sum)
def main():
    num = get_name()
    count(num)
main()
####################################################
####################################################

##
#85
name = input("Enter Name: ")
vowels = ["a","e","i","o","u"]
count = 0
for i in vowels:
    if i in name:
        count += 1        
print("their is ",count,"vowels in your name")



name = input("Enter Name: ")
count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i =="o" or i == "u":
        count = count + 1
print("their is ",count,"vowels in your name")


##
from array import*
nums = array("i",[])
for i in range(1,6):
    tryagain = False
    while tryagain == False:
        num = int(input("Enter the number beetwen 10 and 20: "))
        if num > 10 and num < 20:
            nums.append(num)
            tryagain = True
        else:
            print("Out of range: ")
print("thank you")
print(nums)
        
        
##
from array import*
nums = array("i",[])
while len(nums) < 5:
    num = int(input("Enter the number beetwen 10 and 20: "))
    if num > 10 and num < 20:
        nums.append(num)
    else:
        print("Out of range: ")
print("thank you")
for i in nums:
    print(i)


##
from array import*
nums = array("i",[56,78,45,34,56])
print(nums)
num = int(input("Enter one of the numbers from the array: "))
if nums.count(num) == 1:
    print(num,"appears in the list once")
else:
    print(print(num,"appears in the list",nums.count(num), "times"))


##
from array import*
import random
array1 = array("i",[])
array2 = array("i",[])
for i in range(1,4):
    num = int(input("Enter number: "))
    array1.append(num)
print(array1)
for i in range(1,6):
    num = random.randint(1,100)
    array2.append(num)
print(array2)
array1.extend(array2)
num1 = sorted(array1)



##
from array import*
import math
user_array = array("f",[])
while len(user_array) < 5:
    num = float(input("Enter a number: "))
    user_array.append(num)
tryagain = False
while tryagain == False:
    whole_num = int(input("Enter a number between 2 and 5: "))
    if whole_num > 2 and whole_num < 5:
        print("great choice")
        tryagain = True
    else:
        print("wrong selection")
        tryagain = False
print(user_array)
for x in user_array:
    ans = x/whole_num
    print(ans)


from array import*
import math
nums = array("f",[34.75,27.23,99.58,45.26,28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("incorrect selection")
    else:
        tryagain = False
print(nums)
for i in range(0,5):
    ans = nums[i]/num
    print(round(ans,2))


##

list = []
for i in range(1,4):
    party_mem = input("Enter the names of  people whom you want to invite: ")
    list.append(party_mem)
    print(list)
ask = input("Do you want to invite people(y/n): ")
while ask == "yes":
        ask = input("Enter the names of  people whom you want to invite: ")
        list.append(ask)
        ask = input("Do you want to invite people(y/n): ")
print(list)
        


##
list = []
name1 = input("Enter the name of the person you want invite: ")
list.append(name1)        
name2 = input("Enter the name of the person you want invite: ")
list.append(name2)        
name3 = input("Enter the name of the person you want invite: ")
list.append(name3)  
print(list)
ask = input("Do you want to invite people(y/n): ")
while ask == "yes":
        ask = input("Enter the names of  people whom you want to invite: ")
        list.append(ask)
        ask = input("Do you want to invite people(y/n): ")
print(list)




##
mssg = input("Enter a word in uppercase: ")
# if word.isupper():
while mssg.islower():
    mssg = input("try again: ")
print("thank you")

    
##
while True:
    mssg = input("Enter a word in uppercase: ")
    if mssg.upper():
        break
print("thanks")
    
################################################################ Reach Here
################################################################

##
mssg = input("Enter a word in uppercase: ")
tryagain = False
while tryagain == False:
    if mssg.isupper():
        print("thank you ")
        tryagain = True
    else:
        print("tryagain")
        mssg = input("Enter a word in uppercase: ")



##
name = input("Enter Name: ")
vowels = ["a","e","i","o","u"]
count = 0
for i in vowels:
    if i in name:
        count += 1        
print("their is ",count,"vowels in your name")



name = input("Enter Name: ")
count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i =="o" or i == "u":
        count = count + 1
print("their is ",count,"vowels in your name")




#
from array import*
nums = array("i",[45,324,654,45,264])
print(nums)

import array as arr
nums = arr.array("i",[45,324,654,])
print(nums)

import array
nums = array.array("i",[45,324,654,45,264])
print(nums)






#
from array import*
nums = array("i",[])
for i in range(1,6):
    tryagain = False
    while tryagain == False:
        num = int(input("Enter the number beetwen 10 and 20: "))
        if num > 10 and num < 20:
            nums.append(num)
            tryagain = True
        else:
            print("Out of range: ")
print("thank you")
print(nums)


#
from array import*
nums = array("i",[])
for i in range(1,6):
    while True:
        num = int(input("Select a number beetwen 10 and 20: "))
        if num > 10 and num < 20:
            nums.append(num)
            break
        else:
            print("Out of range: ")
print("Thank you")
print(nums)
        


##        
from array import*
nums = array("i",[])
while len(nums) < 5:
    num = int(input("Enter the number beetwen 10 and 20: "))
    if num > 10 and num < 20:
        nums.append(num)
    else:
        print("Out of range: ")
print("thank you")
for i in nums:
    print(i)

##
from array import*
import math
user_array = array("f",[])
while len(user_array) < 5:
    num = float(input("Enter a number: "))
    user_array.append(num)
tryagain = False
while tryagain == False:
    whole_num = int(input("Enter a number between 2 and 5: "))
    if whole_num > 2 and whole_num < 5:
        print("great choice")
        tryagain = True
    else:
        print("wrong selection")
        tryagain = False
print(user_array)
for x in user_array:
    ans = x/whole_num
    print(ans)

##
from array import*
import math
nums = array("f",[34.75,27.23,99.58,45.26,28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("incorrect selection")
    else:
        tryagain = False
print(nums)
for i in range(0,5):
    ans = nums[i]/num
    print(round(ans,2))




##
from array import*
nums = array("i",[45,324,654,45,264])
newvalue = int(input("Enter number: "))
nums.append(newvalue)
print(nums)
print(nums.reverse())
nums = sorted(nums)
print(nums)    
nums = nums.pop()
print(nums)


from array import*
nums = array("i",[45,324,654,45,264])
newArray = array("i",[])
more = int(input("How many items: "))
for i in range(0,more):
    newValue = int(input("Enter a number: "))
    newArray.append(newValue)
# print(newArray)
nums.extend(newArray)
print(nums)
getRid  = int(input("Enter item index: "))
nums.remove(getRid)
print(nums)
print(nums.count(45))





##
list = []
for i in range(1,4):
    party_mem = input("Enter the names of  people whom you want to invite: ")
    list.append(party_mem)
    print(list)
ask = input("Do you want to invite people(y/n): ")
while ask == "yes":
        ask = input("Enter the names of  people whom you want to invite: ")
        list.append(ask)
        ask = input("Do you want to invite people(y/n): ")
print(list)
        

##
list = {}
for i in range(1,5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[name] = {"Age":age,"Shoe_size":shoe_size}
print(list)    
ask = input("Enter name: ")
print(list[ask])


##
list = {}
for i in range(1,5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    list[name] = age
print(list)    
ask = input("Enter name: ")
print(list[ask])



##

simple_array = [[2,5,8],[3,7,4],[1,6,9]]
print(simple_array)
print(simple_array[1])
simple_array[2][1] = 5
print(simple_array)
print(simple_array[1][2])
simple_array[1].append(3)
print(simple_array)



##
data_set = {"A":{"x":54,"y":82,"z":91},"B":{"x":75,"y":29,"z":80}}
print(data_set["A"])
print(data_set["B"]["y"])
for i in data_set:
    print(data_set [i]["y"])
    
data_set["B"]["y"] = 53
print(data_set)






##display age and shoes in one and in second display only age
list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe so=ize: "))
    list[name] = {"Age":age,"Shoe size":shoe}
    
ask = input("Enter a name: ")
print(list[ask])
    
# for name in list:
#     print((name),list[name]["Age"])
list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe so=ize: "))
    list[name] = {"Age":age,"Shoe size":shoe}
    
for name in list:
    print((name),list[name]["Age"])



########################################################################

list = {}
for i in range(0,4):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        shoe = int(input("Enter shoe so=ize: "))
        list[name] = {"Age":age, "Shoe":shoe}
print(list)
ask = input("Enter name: ")
del list [ask]
for name in list:
    print((name),list[name]["Age"],list[name]["Shoe"])


###############################

print("\t1) Create a new file")
print("\t2) Display the file")
print("\t3) Add a new item to the file")
print("\t Make a selection 1, 2 or 3: ")
selection = int(input("Enter your selection: "))
if selection == 1:
    new_file = open("Subject.txt","w")
    school_sub = input("Enter your school subject: ")
    new_file.write(school_sub)
    new_file.close()
elif selection == 2:
    new_file = open("Subject.txt","r")
    print(new_file.read())
elif selection == 3:
    new_file = open("Subject.txt","a")
    school_sub = input("Enter new school subject: ")
    new_file.write("\n" + school_sub )  # continous run does not suppert line brekdown new_file.write(school_sub + "\n")
    new_file.close()
    new_file = open("Subject.txt","r")
    print(new_file.read()) 


######
######
import csv
file = open("stars.csv","a")
name = input("Enter name: ")
age = input("Enter star age: ")
star = input("Enter star sign: ")
newrecord = name + "," + age + "," + star
file.write(str(newrecord))

import csv
file = open("Stars.csv","r")
for row in file:
    print(row)
    
    
file = open("Stars.csv","r")
reader = csv.reader(file)
rows = list(reader)
print(row[1])

file = open("Stars.csv","r")
search = input("Enter the data you are searching for: ")
reader = csv.reader(file)
for row in file:
    if search in str(row):
        print(row)


################################################################################
################################Noted
####CHEKED IT
import csv
file = open("Books.csv","a")
records = int(input("How many record do want add to file: "))
for x in range(0,records):
    book = input("Enter a book: ")
    author = input("Enter a author name: ")
    year = input("Enter a year: ")
    newrecord =book + "," + author + "," +  year  + "," + "\n"
    file.write(str(newrecord))
author = input("Enter a author name: ")
file = open("Books.csv","r")
print(file.read())
reader = csv.reader(file)
count = 0
for row in file:
    if author in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There is no book written by this author in the list: ")
file.close()


########################################################################
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)  

###and 
import csv
file = list(csv.reader(open("Books.csv")))

file = open("Books.csv","r")
# print(file.read())
start = int(input("starting year: "))
end = int(input("Ending year: "))

for row in file:
    print(row[start:end])
    
""",23432,3232,

,ak,3243,

,bk,23432,

,ck,4354,

,mk,2343,

,nk,34444432"""



################################################################################
'''simple_array = [[2,5,8],[3,7,4],[1,6,9]]                   # 0 1 2
Creates a 2D list (as shown on the right) which uses          0 2 5 8
standard Python indexing for the rows and columns.            1 3 7 4
                                                              2 1 6 9

                                                            
'''
################################################################################

import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
start = int(input("starting year: "))
end = int(input("Ending year: "))
x = 0
for row in tmp:
    if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        print(tmp[x])
        x = x+1
        
##tmp[2] means indexing of instances in list for eg- book(0)->author name(1)-> year(2)
##Note  '>=' not supported between instances of 'int' and 'str' so it instance must be int (start and end)
'''PS C:\VSCode\Pythonhardway> python -u "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py"  
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
starting year: 1221
Ending year: 2132
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['A Brief History of Time', ' Stephon Hawking', ' 1988']
['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922']
['The Man Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985']
['Pride and Prejudice', ' Jane Austen', ' 1813']'''


################################################################################
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
#start = int(input("starting year: "))
#end = int(input("Ending year: "))
x = 0
for row in tmp:
    print(tmp[x])
    # if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        #print(tmp[x])
        #x = x+1
'''S C:\VSCode\Pythonhardway> python -u "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py"
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']'''

################################
        
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
#start = int(input("starting year: "))
#end = int(input("Ending year: "))
for row in tmp:
    print(row)
    # if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        #print(tmp[x])
        #x = x+1
'''[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['A Brief History of Time', ' Stephon Hawking', ' 1988']
['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922']
['The Man Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985']
['Pride and Prejudice', ' Jane Austen', ' 1813']
['a', 'b', '34', '']
['a', 'ak', '1221', '']
['b', 'bk', '2132', '']
['c', 'ck', '3433', '']
['a', 'ak', '2323', '']
['b', 'bk', '2332', '']
['a', 'ak', '2112', '']
['b', 'bk', '2332', '']
['c', '23432', '3232', '']
['a', 'ak', '3243', '']
['b', 'bk', '23432', '']
['c', 'ck', '4354', '']
['m', 'mk', '2343', '']
['n', 'nk', '34444432', '']'''


################################################################################
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
#start = int(input("starting year: "))
#end = int(input("Ending year: "))
for row in tmp:
    print(tmp)
    # if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        #print(tmp[x])
        #x = x+1
'''PS C:\VSCode\Pythonhardway> python -u "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py"
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]'''




################################################################################
import csv
file = open("Books.csv","r")
x = 0
for row in file:
    print("Row: " + str(x) + "-"+ row)
    x = x + 1
file.close()

#    print("Row: " + (x)  + "-"+ str(row))
# TypeError: can only concatenate str (not "int") to str
# all must be in str form
'''Row: 0-To Kill A Mockingbird, Harper Lee, 1960

Row: 1-A Brief History of Time, Stephon Hawking, 1988

Row: 2-The Great Gatsby, F.Scott Fitzgerald, 1922

Row: 3-The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985

Row: 4-Pride and Prejudice, Jane Austen, 1813

Row: 5-a,b,34,'''


################################
'''    del Booklist[getrid]
TypeError: list indices must be integers or slices, not str means getrid must be int or slices'''
"""Especially Care:-    x = 0
    for i in fruits:
        print(x,i)
        x = x+1
    del_fruit = input("Enter fruits name which you want to delete: ")
    dfruit =  fruits.index(del_fruit)"""

################################

import csv
import random
score = 0
name = input("Enter your name: ")
q1_num1 = random.randint(10,50)
q1_num2 = random.randint(10,50)
question1 = str(q1_num1) + " + " + str(q1_num2) + "=" 
ans1 = int(input(question1))
realans1 = q1_num1  + q1_num2
if ans1 == realans1:
    score = score + 1
q2_num1 = random.randint(10,50)
q2_num2 = random.randint(10,50)
question2 = str(q2_num1) + " + " + str(q2_num2) + "=" 
ans2 = int(input(question2))
realans1 = q2_num1  + q2_num2
if ans2 == realans1:
    score = score + 1
    
file = open("QuizScore.csv","a")
newrecord = name + "," + question1 + "," + str(ans1) + "," + question2 + "," + str(ans2) + "," + str(score) + "\n"
file.write(newrecord)  


########################################################################

########################################################################
'''    fruits[alt_fruit] = fruit_name
TypeError: list indices must be integers or slices, not str   
Remember:-[] # In this braket usually int exist either in the case of chaning item or delting items in the list
PS C:\VSCode\Pythonhardway> '''
###You can chnge input in indexing before altring or deleting or directly take integer input
########################################################################


################################################################################
'''def delete():
    file = list(csv.reader(open("Salaries.csv")))
    salary = []
    for row in file:
        salary.append(row)

    x = 0
    for row in salary:
        print(x,salary[x])
        x = x + 1
    delete_itm = int(input("Enter the name you want to  delete: "))
    del salary[delete_itm] ##After dwlting or altering we must to rewrite
##in this way> 
    file = open("Salaries.csv","w")
    x = 0
    for row in salary:
        nwrecord = salary[x][0] + "," + salary[x][1] + "\n"
        x = x + 1
        file.write(nwrecord)
    file.close() '''
    
################################################################################




    
################################################
  
'''    file = list(csv.reader(open("Salaries.csv")))
    salary = []
    for row in file:
        salary.append(row)
#############       Do not confuse 
    x = 0
    for row in salary:
        print(x,salary[x])
        x = x + 1

    x = 0
    for row in salary:
        print(x,row)
        x = x + 1 '''
        
#####################################################

##########
# entry_box.focus()
#########



#####################################################

from tkinter import*
import random
def dice():
    dice_num = random.randint(1,7)
    entry_box = Message(window, text = dice_num)
    entry_box.place(x = 125,y = 20,width = 100, height = 30)
    entry_box["justify"] = "center"
    entry_box["bg"] = "black"
    entry_box["fg"] = "white"

    

window = Tk()
window.geometry("720x480")
label = Label(text = "Roll a dice")
label.place(x = 10,y = 20)

button = Button(text = "roll", command = dice)
button.place(x = 150,y = 50,width = 50,height =25)
button["bg"] = "black"
button["fg"] = "white"
window.mainloop()

### OR
from tkinter import*
import random
def dice():
    dice_num = random.randint(1,7)
    entry_box["text"] = dice_num #Note


window = Tk()
window.geometry("720x480")
label = Label(text = "Roll a dice")
label.place(x = 10,y = 20)
entry_box = Message(window, text = "")
entry_box.place(x = 125,y = 20,width = 100, height = 30)
entry_box["justify"] = "center"
entry_box["bg"] = "black"
entry_box["fg"] = "white"
button = Button(text = "roll", command = dice)
button.place(x = 150,y = 50,width = 50,height =25)
button["bg"] = "black"
button["fg"] = "white"
window.mainloop()

#########################################################

#$$$$$

'''  File "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py", line 16
    del numbox(0,END)
        ^
SyntaxError: cannot delete function call
[numbox.delete(0,END)] it would be work

*   2nd point = , in add
    answer = int(answer)
ValueError: invalid literal for int() with base 10: ''        
means here in answer = mssg_box["text"] # text = 0


entry_box.delete(0, END) 
#Deletes the contents of an entry or 
list box. 
'''
#$$$$$

################################
'''def add():
        num = numbox.get()
        num = int(num)
        answer = mssg_box["text"]
        answer = int(answer)
        total = num + answer
        mssg_box["text"] = total
        numbox.delete(0,END)

def reset():
    total = 0
    mssg_box["text"] = 0
    numbox.delete(0,END)
    numbox.focus()
    



window = Tk()
window.geometry("720x480")
label = Label(text ="Add Number")
label.place(x = 10, y = 20)
numbox = Entry(text =0)
numbox.place(x = 100, y = 20, width = 150, height = 25)
numbox["bg"] = "blue"
numbox["fg"] = "yellow"
numbox["justify"] = "center"
label = Label(text ="Answer")
label.place(x = 10, y = 80)
mssg_box = Message(text =0)
mssg_box.place(x = 100, y = 75, width = 150, height = 25)
mssg_box["bg"] = "green"
mssg_box["fg"] = "yellow"
mssg_box["justify"] = "center"
add_button = Button(text="Add", command =add)
add_button.place(x = 90, y = 110, width =50,height = 25)
reset_button = Button(text="reset", command = reset)
reset_button.place(x = 175, y = 110, width =50,height = 25)
window.mainloop()

'''
################################

################################
'''    miles = textbox1.get()
    miles = int(miles) '''
    
    
#Listbox() parenthesis  empty
################################



################################################################

from tkinter import*
import csv
def add():
    num = numbox.get()
    if num.isdigit():
        listbox.insert(END,num)
        numbox.delete(0, END)
        numbox.focus()
    else:
        numbox.delete(0,END)
        numbox.focus()


def clear():
    listbox.delete(0,END)
    
def addcsv():
    file = open("namelist.csv", "w")
    tmp_list = listbox.get(0,END)
    item = 0
    for x in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item +1
    file.close()
    

window = Tk()
window.title("Digichecker")
window.geometry("720x480")
label = Label(text = "Enter a number")
label.place(x = 10,y = 20)
numbox = Entry(text = " ")
numbox.place(x = 125,y = 50)
numbox["justify"] = "center"
numbox.focus()
listbox = Listbox()
listbox.place(x = 150,y = 150)
listbox["justify"] = "center"
button1 = Button(text="Add", command = add)
button1.place(x = 150,y = 80, width = 50, height = 20)
button2 = Button(text="clear", command = clear)
button2.place(x = 200,y = 80, width = 50, height = 20)
button3 = Button(text="addcsv", command = addcsv)
button3.place(x = 300,y = 80, width = 50, height = 20)
window.mainloop()
########################################################################





########################################################################

from tkinter import*
import csv
def create():
    file = open("Details.csv","w")
    file.close()

def add():
    file = open("Details.csv","a")
    name = namebox.get()
    age = agebox.get()
    record = name + " , " + str(age) + "\n"
    file.write(record)
    namebox.delete(0,END)
    agebox.delete(0,END)
    namebox.focus()
    
def show():
    listbox.delete(0,END)
    file = list(csv.reader(open("Details.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        listbox.insert(END,data)
        x = x+1

window = Tk()
window.geometry("720x480")
window.title("File")
label1 = Label(text = "Enter the name: ")
label1.place(x = 10, y= 20)
namebox = Entry(text = "")
namebox.place(x = 150, y= 20)
namebox["justify"] = "center"
namebox.focus()
label2 = Label(text = "Enter your age: ")
label2.place(x = 10, y= 50)
agebox = Entry(text = "")
agebox.place(x = 150, y= 50)
agebox["justify"] = "center"
agebox.focus()
button = Button(text = "Create", command = create)
button.place(x = 200, y = 250)
button2 = Button(text = "Add", command = add)
button2.place(x = 250, y = 250)
button3 = Button(text = "show", command = show)
button3.place(x = 300, y = 250)
listbox = Listbox()
listbox.place(x = 250, y = 350)
window.mainloop()

############################################################################

############################################################################

from tkinter import*
def show():
    name = namebox.get()
    mssg = ("Hello" + " " + name)
    mssgbox["text"] = mssg    
    namebox.delete(0,END)
    
window = Tk()
window.title("Names")
window.wm_iconbitmap("icon.ico")
window.geometry("720x480")
window.configure(backgroun = "light green")
logo = PhotoImage(file = "log.gif")
logobox = Label(image = logo) 
logobox.place(x = 30, y = 10 ,width = 200 ,height = 150)
label = Label(text = "Enter your name")
label.place(x = 10, y = 200,width = 150, height = 25)
label["bg"] = "black"
label["fg"] = "white"
namebox = Entry(text = "")
namebox.place(x = 150, y = 200,width = 150, height = 25)
namebox["justify"] = "center"
namebox.focus()
button = Button(text = "press me", command = show)
button.place(x = 10, y = 250,width = 150, height = 25)
button["bg"] = "yellow"
mssgbox = Message(text = "")
mssgbox.place(x = 150, y = 250, width = 150, height = 25)
label["fg"] = "black"
label["bg"] = "white"
window.mainloop()

########################################################################

########################################################################
'''
from tkinter import*
def show():
    colour = drop_down.get()
    window.configure(background = colour)
'''
###Note StringVar not stringVar or stringvar
##drop_down.set("grey") here grey is name of dropdownmenu or on the top
'''gendr = StringVar(window)
gendr.set("gender")
genderlist = OptionMenu(window,gendr,"male","female")
def add():
    mssg = namebox.get()
    new_mssg = mssg + " ," + str(gendr.get()) # don't forget to get objects from dropdownmenu
    namelist.insert(END,new_mssg)
    namebox.delete(0,END)
'''



'''
A primary key is the field (usually the first one) in each table that 
stores the unique identifier for that record. Therefore, in the Employees 
table the primary key will be the ID column and in the Department table 
the primary key will be Dept. 

 integer: the value is an integer value; 
 real: the value is a floating-point value; 
 text: the value is a text string; 
 blob: the value is stored exactly as it was input. 

'''



########################################################################

##########################################################
##########################################################
'''
import sqlite3 
This must be the first line of the program to allow Python to use the SQLite3 library. 

with sqlite3.connect(“company.db”) as db: 
    cursor=db.cursor() 
Connects to the company database. If no such database exists, it will create one.
The file will be stored in the same folder as the program. 

cursor.execute(“““CREATE TABLE IF NOT EXISTS employees( 
    id integer PRIMARY KEY, 
    name text NOT NULL, 
    dept text NOT NULL, 
    salary integer);”””) 
Creates a table called employees which has four fields (id, name, dept and salary). It 
specifies the data type for each field, defines which field is the primary key and which 
fields cannot be left blank. The triple speech marks allow the code to be split over 
several lines to make it easier to read rather than having it all displayed in one line.

cursor.execute(“““INSERT INTO employees(id,name,dept,salary) 
    VALUES(“1”,”Bob”,”Sales”,”25000”)”””) 
db.commit() 
Inserts data into the employees table. The db.commit()line saves the changes. 

newID = input(“Enter ID number: ”) 
newame = input(“Enter name: ”) 
newDept = input(“Enter department: ”) 
newSalary = input(“Enter salary: ”) 
cursor.execute(“““INSERT INTO employees(id,name,dept,salary) 
    VALUES(?,?,?,?)”””,(newID,newName,newDept,newSalary)) 
db.commit() 
Allows a user to enter new data which is then inserted into the table.


cursor.execute(“SELECT * FROM employees”) 
print(cursor.fetchall()) 
Displays all the data from the employees table. 

db.close() 
This must be the last line in the program to close the database. 

cursor.execute(“SELECT * FROM employees”) 
for x in cursor.fetchall(): 
    print(x) 
Displays all the data from the employees table and displays each record on a separate line. 

cursor.execute(“SELECT * FROM employees ORDER BY name”) 
for x in cursor.fetchall(): 
    print(x) 
Selects all the data from the employees table, sorted by name,and displays each record on a separate line.

cursor.execute(“SELECT * FROM employees WHERE salary>20000”) 
Selects all the data from the employees table where the salary is over 20,000. 

cursor.execute(“SELECT * FROM employees WHERE dept=‘Sales’”) 
Selects all the data from the employees table where the department is “Sales”.

cursor.execute(“SELECT id,name,salary FROM employees”) 
Selects the ID, name and salary fields from the employees table. 
cursor.execute(“““SELECT employees.id,employees.name,dept.manager 
    FROM employees,dept WHERE employees.dept=dept.dept 
    AND employees.salary >20000”””) 
Selects the ID and name fields from the employees table and the manager field from the department table if the salary is over 20,000. 

whichDept = input(“Enter a department: ”) 
cursor.execute(“SELECT * FROM employees WHERE dept=?”,[whichDept])
for x in cursor.fetchall(): 
    print(x) 
Allows the user to type in a department and displays the records of all the employees in that department. 

cursor.execute(“““SELECT employees.id,employees.name,dept.manager 
    FROM employees,dept WHERE employees.dept=dept.dept”””) 
Selects the ID and name fields from the employees table and the manager field from the 
department table, using the dept fields to link the data. If you do not specify how the 
tables are linked, Python will assume every employee works in every department and 
you will not get the results you are expecting. 

cursor.execute(“UPDATE employees SET name = ‘Tony’ WHERE id=1”) 
db.commit() 
Updates the data in the table (overwriting the original data) to change the name to“Tony” for employee ID 1. 

cursor.execute(“DELETE employees WHERE id=1”)

'''
##########################################################
##########################################################

################################
'''
cursor.execute("""SELECT employees.id,employees.name, employees.dept,
    from employees,###notedept WHERE employees.dept = dept.dept AND employees.salary> 20000""") 
'''
################################

##########################################################
'''
If you want SQL to IGNORE that error and continue adding other records , then do this :

Noted:- INSERT or IGNORE into tablename VALUES (value1,value2 , so on );
if you want to replace the values in the table whenever the entry already exists , then do this:

Noted:-INSERT or REPLACE into tablename VALUES (value1,value2 , so on );

'''
##########################################################
#
formatter = "{} {} {} {} {}"
print(formatter.format(1,2,3,4,5))
days = "Mon Tue Wed Thu Fri Sat Sun"
month = "Jan\tFeb\tmar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec"
print("Here is days",days)
print("Here is month",month)

#Notable
print(None == False)
# >>>False
print(False==0)
# >>>True
print(True==1)
# >>>True


#NOTE:=cursor.execute("UPDATE Names SET FirstName = "Tony" WHERE ID = 1 ") in double quotes["] always use single quotes[']

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

##
word = input("Enter word: ")
wrd = word[1:]
for i in wrd:
    print("\t",i)

#

x = [154,634,892,345,341,43]
print(len(x))
print(x[1:4])
for i in x:
    print(i)
num = int(input("Enter number: "))
if num in x:
    print(num,"is in the list")
else:
    print("Not in the list")
x.insert(2,420)    
print(x)
x.remove(892)
print(x)
x.append(993)
print(x)

#
fav_sub = input("Enter your favorite subject: ")
for letter in fav_sub:
    print(letter,end = "-")


#
mssg = input("Enter a word in uppercase: ")
# if word.isupper():
while mssg.islower():
    mssg = input("try again: ")
print("thank you")


#
postcode = input("Enter Postcode: ")
ans = postcode[:2]
print(ans.upper())




##
msg = "hello"
if msg.isupper():
    print("Uppercase")
else:
    print("This is not in uppercaase")
    
msg.islower()
msg = "hello" 
for letter in msg:
    print(letter,end = "*")

msg.capitalize()
msg.title()


#
subjects = ["math","computerscience","physicks","chemistry","biology","botany"]
user = input("Enter the subject which one you do not like: ")
sub = subjects.index(user)
del subjects[sub]
print(subjects)

#
colors = ["red", "green", "blue", "yellow", "black", "white","brown","orange","grey","sky"]
start = int(input("Enter number beetween 0 and 4: "))
end = int(input("Enter number beetween 5 and 9"))
print(colors[start:end])



num1= int(input("Enter a number: "))
total = num1
question = (input("Do you want add another number(y/n) : "))
while question == "yes":
    num = int(input("Enter a number: "))
    total = total+num
    question = (input("Do you want add another number(y/n) : "))
print("total is",total)

num1= int(input("Enter a number: "))
total = num1
question = "yes"
while question == "yes":
    num2 = int(input("Enter a number: "))
    total = total+num2
    question = (input("Do you want add another number(y/n) : "))
print("total is",total)

#
import random
num = random.randint(1, 10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        print("You win")
        correct = True
    elif guess > num:
        print("your guess is too high")
    else:
        print("your guess is too low")


#
import turtle
turtle.Screen().bgcolor("blue")
turtle.begin_fill()
turtle.color("green", "yellow")
for i in range(1,5):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.Screen().bgcolor("blue")
turtle.begin_fill()
turtle.color("green", "red")
for i in range(1,5):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.Screen().bgcolor("blue")
turtle.begin_fill()
turtle.color("green", "pink")
for i in range(1,5):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.exitonclick()

##import turtle
# scr = turtle.Screen()
# scr.bgcolor("blue","yellow")
turtle.Screen().bgcolor("green")
turtle.begin_fill()
turtle.pensize(3)
turtle.color("blue","yellow")
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)
turtle.end_fill()
turtle.exitonclick()


################################
def get_data():
    num = int(input("Enter number: "))
    return num 


def answer(num):
    for i in num: #num not be integer should be list stirng tupple dic....
        print(i)
        
    # for i in num:
# TypeError: 'int' object is not iterable

################################


####################################################
####################################################

list1 = range(1, 51) 
sum1 = sum(list1) 
print(sum1) 
    
    
num = 50
a = 1
sum = num/2*(a+1)
print(sum)

num = 50 # where num is number of terms and last term 
a = 1 # a is first term 
sum = num//2*(50+1) 
print(sum)

res = 0
for i in range(1,51):
    res = res +i
print(res)

print(sum(range(1,51)))
'''
5 + sum(4)[10]  =15
4 + sum(3)[6]  =10
3 + sum(2)[3]  =6
2 + sum(1)[1]  =3
1
'''
def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)
add = sum(5)
print(add)



def get_name():
    num= int(input('Enter the number: '))
    return num

def count(num):
    sum = 0 
    for i in range(1, num+1):
        print(i)
        sum = i + sum
    print(sum)
def main():
    num = get_name()
    count(num)
main()
####################################################
####################################################

##
#85
name = input("Enter Name: ")
vowels = ["a","e","i","o","u"]
count = 0
for i in vowels:
    if i in name:
        count += 1        
print("their is ",count,"vowels in your name")



name = input("Enter Name: ")
count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i =="o" or i == "u":
        count = count + 1
print("their is ",count,"vowels in your name")


##
from array import*
nums = array("i",[])
for i in range(1,6):
    tryagain = False
    while tryagain == False:
        num = int(input("Enter the number beetwen 10 and 20: "))
        if num > 10 and num < 20:
            nums.append(num)
            tryagain = True
        else:
            print("Out of range: ")
print("thank you")
print(nums)
        
from array import*
nums = array("i",[])
while len(nums) < 5:
    num = int(input("Enter the number beetwen 10 and 20: "))
    if num > 10 and num < 20:
        nums.append(num)
    else:
        print("Out of range: ")
print("thank ypu")
for i in nums:
    print(i)

##
from array import*
nums = array("i",[56,78,45,34,56])
print(nums)
num = int(input("Enter one of the numbers from the array: "))
if nums.count(num) == 1:
    print(num,"appears in the list once")
else:
    print(print(num,"appears in the list",nums.count(num), "times"))

from array import*
import random
array1 = array("i",[])
array2 = array("i",[])
for i in range(1,4):
    num = int(input("Enter number: "))
    array1.append(num)
print(array1)
for i in range(1,6):
    num = random.randint(1,100)
    array2.append(num)
print(array2)
array1.extend(array2)
num1 = sorted(array1)


##

from array import*
import math
user_array = array("f",[])
while len(user_array) < 5:
    num = float(input("Enter a number: "))
    user_array.append(num)
tryagain = False
while tryagain == False:
    whole_num = int(input("Enter a number between 2 and 5: "))
    if whole_num > 2 and whole_num < 5:
        print("great choice")
        tryagain = True
    else:
        print("wrong selection")
        tryagain = False
print(user_array)
for x in user_array:
    ans = x/whole_num
    print(ans)


from array import*
import math
nums = array("f",[34.75,27.23,99.58,45.26,28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("incorrect selection")
    else:
        tryagain = False
print(nums)
for i in range(0,5):
    ans = nums[i]/num
    print(round(ans,2))


##
list = []
for i in range(1,4):
    party_mem = input("Enter the names of  people whom you want to invite: ")
    list.append(party_mem)
    print(list)
ask = input("Do you want to invite people(y/n): ")
while ask == "yes":
        ask = input("Enter the names of  people whom you want to invite: ")
        list.append(ask)
        ask = input("Do you want to invite people(y/n): ")
print(list)
        
        
list = []
name1 = input("Enter the name of the person you want invite: ")
list.append(name1)        
name2 = input("Enter the name of the person you want invite: ")
list.append(name2)        
name3 = input("Enter the name of the person you want invite: ")
list.append(name3)  
print(list)
ask = input("Do you want to invite people(y/n): ")
while ask == "yes":
        ask = input("Enter the names of  people whom you want to invite: ")
        list.append(ask)
        ask = input("Do you want to invite people(y/n): ")
print(list)




#
mssg = input("Enter a word in uppercase: ")
# if word.isupper():
while mssg.islower():
    mssg = input("try again: ")
print("thank you")
    
mssg = input("Enter a word in uppercase: ")
tryagain = False
while tryagain == False:
    if mssg.isupper():
        print("thank you ")
        tryagain = True
    else:
        print("tryagain")
        mssg = input("Enter a word in uppercase: ")

#
name = input("Enter Name: ")
vowels = ["a","e","i","o","u"]
count = 0
for i in vowels:
    if i in name:
        count += 1        
print("their is ",count,"vowels in your name")



name = input("Enter Name: ")
count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i =="o" or i == "u":
        count = count + 1
print("their is ",count,"vowels in your name")




#
from array import*
nums = array("i",[45,324,654,45,264])
print(nums)

import array as arr
nums = arr.array("i",[45,324,654,])
print(nums)

import array
nums = array.array("i",[45,324,654,45,264])
print(nums)






#
from array import*
nums = array("i",[])
for i in range(1,6):
    tryagain = False
    while tryagain == False:
        num = int(input("Enter the number beetwen 10 and 20: "))
        if num > 10 and num < 20:
            nums.append(num)
            tryagain = True
        else:
            print("Out of range: ")
print("thank you")
print(nums)
        
from array import*
nums = array("i",[])
while len(nums) < 5:
    num = int(input("Enter the number beetwen 10 and 20: "))
    if num > 10 and num < 20:
        nums.append(num)
    else:
        print("Out of range: ")
print("thank ypu")
for i in nums:
    print(i)

##


from array import*
import math
user_array = array("f",[])
while len(user_array) < 5:
    num = float(input("Enter a number: "))
    user_array.append(num)
tryagain = False
while tryagain == False:
    whole_num = int(input("Enter a number between 2 and 5: "))
    if whole_num > 2 and whole_num < 5:
        print("great choice")
        tryagain = True
    else:
        print("wrong selection")
        tryagain = False
print(user_array)
for x in user_array:
    ans = x/whole_num
    print(ans)


from array import*
import math
nums = array("f",[34.75,27.23,99.58,45.26,28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("incorrect selection")
    else:
        tryagain = False
print(nums)
for i in range(0,5):
    ans = nums[i]/num
    print(round(ans,2))




##
from array import*
nums = array("i",[45,324,654,45,264])
newvalue = int(input("Enter number: "))
nums.append(newvalue)
print(nums)
print(nums.reverse())
nums = sorted(nums)
print(nums)    
nums = nums.pop()
print(nums)


from array import*
nums = array("i",[45,324,654,45,264])
newArray = array("i",[])
more = int(input("How many items: "))
for i in range(0,more):
    newValue = int(input("Enter a number: "))
    newArray.append(newValue)
# print(newArray)
nums.extend(newArray)
print(nums)
getRid  = int(input("Enter item index: "))
nums.remove(getRid)
print(nums)
print(nums.count(45))





#
list = []
for i in range(1,4):
    party_mem = input("Enter the names of  people whom you want to invite: ")
    list.append(party_mem)
    print(list)
ask = input("Do you want to invite people(y/n): ")
while ask == "yes":
        ask = input("Enter the names of  people whom you want to invite: ")
        list.append(ask)
        ask = input("Do you want to invite people(y/n): ")
print(list)
        


list = {}
for i in range(1,5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[name] = {"Age":age,"Shoe_size":shoe_size}
print(list)    
ask = input("Enter name: ")
print(list[ask])



list = {}
for i in range(1,5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    list[name] = age
print(list)    
ask = input("Enter name: ")
print(list[ask])



##

simple_array = [[2,5,8],[3,7,4],[1,6,9]]
print(simple_array)
print(simple_array[1])
simple_array[2][1] = 5
print(simple_array)
print(simple_array[1][2])
simple_array[1].append(3)
print(simple_array)



##
data_set = {"A":{"x":54,"y":82,"z":91},"B":{"x":75,"y":29,"z":80}}
print(data_set["A"])
print(data_set["B"]["y"])
for i in data_set:
    print(data_set [i]["y"])
    
data_set["B"]["y"] = 53
print(data_set)






##display age and shoes in one and in second display only age
list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe so=ize: "))
    list[name] = {"Age":age,"Shoe size":shoe}
    
ask = input("Enter a name: ")
print(list[ask])
    
# for name in list:
#     print((name),list[name]["Age"])
list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age":age,"Shoe size":shoe}
    
for name in list:
    print((name),list[name]["Age"])

    



########################################################################

list = {}
for i in range(0,4):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        shoe = int(input("Enter shoe so=ize: "))
        list[name] = {"Age":age, "Shoe":shoe}
print(list)
ask = input("Enter name: ")
del list [ask]
for name in list:
    print((name),list[name]["Age"],list[name]["Shoe"])


###############################

print("\t1) Create a new file")
print("\t2) Display the file")
print("\t3) Add a new item to the file")
print("\t Make a selection 1, 2 or 3: ")
selection = int(input("Enter your selection: "))
if selection == 1:
    new_file = open("Subject.txt","w")
    school_sub = input("Enter your school subject: ")
    new_file.write(school_sub)
    new_file.close()
elif selection == 2:
    new_file = open("Subject.txt","r")
    print(new_file.read())
elif selection == 3:
    new_file = open("Subject.txt","a")
    school_sub = input("Enter new school subject: ")
    new_file.write("\n" + school_sub )  # continous run does not suppert line brekdown new_file.write(school_sub + "\n")
    new_file.close()
    new_file = open("Subject.txt","r")
    print(new_file.read()) 

######
import csv
file = open("stars.csv","a")
name = input("Enter name: ")
age = input("Enter star age: ")
star = input("Enter star sign: ")
newrecord = name + "," + age + "," + star
file.write(str(newrecord))

import csv
file = open("Stars.csv","r")
for row in file:
    print(row)
    
    
file = open("Stars.csv","r")
reader = csv.reader(file)
rows = list(reader)
print(row[1])

file = open("Stars.csv","r")
search = input("Enter the data you are searching for: ")
reader = csv.reader(file)
for row in file:
    if search in str(row):
        print(row)


################################################################################
################################Noted
####CHEKED IT
import csv
file = open("Books.csv","a")
records = int(input("How many record do want add to file: "))
for x in range(0,records):
    book = input("Enter a book: ")
    author = input("Enter a author name: ")
    year = input("Enter a year: ")
    newrecord =book + "," + author + "," +  year  + "," + "\n"
    file.write(str(newrecord))
author = input("Enter a author name: ")
file = open("Books.csv","r")
print(file.read())
reader = csv.reader(file)
count = 0
for row in file:
    if author in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There is no book written by this author in the list: ")
file.close()


########################################################################
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)  

###and 
import csv
file = list(csv.reader(open("Books.csv")))

file = open("Books.csv","r")
# print(file.read())
start = int(input("starting year: "))
end = int(input("Ending year: "))

for row in file:
    print(row[start:end])
    
""",23432,3232,

,ak,3243,

,bk,23432,

,ck,4354,

,mk,2343,

,nk,34444432"""



################################################################################
'''simple_array = [[2,5,8],[3,7,4],[1,6,9]]                   # 0 1 2
Creates a 2D list (as shown on the right) which uses          0 2 5 8
standard Python indexing for the rows and columns.            1 3 7 4
                                                              2 1 6 9

                                                            
'''
################################################################################

import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
start = int(input("starting year: "))
end = int(input("Ending year: "))
x = 0
for row in tmp:
    if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        print(tmp[x])
        x = x+1
        
##tmp[2] means indexing of instances in list for eg- book(0)->author name(1)-> year(2)
##Note  '>=' not supported between instances of 'int' and 'str' so it instance must be int (start and end)
'''PS C:\VSCode\Pythonhardway> python -u "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py"  
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
starting year: 1221
Ending year: 2132
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['A Brief History of Time', ' Stephon Hawking', ' 1988']
['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922']
['The Man Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985']
['Pride and Prejudice', ' Jane Austen', ' 1813']'''


################################################################################
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
#start = int(input("starting year: "))
#end = int(input("Ending year: "))
x = 0
for row in tmp:
    print(tmp[x])
    # if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        #print(tmp[x])
        #x = x+1
'''S C:\VSCode\Pythonhardway> python -u "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py"
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['To Kill A Mockingbird', ' Harper Lee', ' 1960']'''

################################
        
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
#start = int(input("starting year: "))
#end = int(input("Ending year: "))
for row in tmp:
    print(row)
    # if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        #print(tmp[x])
        #x = x+1
'''[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
['To Kill A Mockingbird', ' Harper Lee', ' 1960']
['A Brief History of Time', ' Stephon Hawking', ' 1988']
['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922']
['The Man Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985']
['Pride and Prejudice', ' Jane Austen', ' 1813']
['a', 'b', '34', '']
['a', 'ak', '1221', '']
['b', 'bk', '2132', '']
['c', 'ck', '3433', '']
['a', 'ak', '2323', '']
['b', 'bk', '2332', '']
['a', 'ak', '2112', '']
['b', 'bk', '2332', '']
['c', '23432', '3232', '']
['a', 'ak', '3243', '']
['b', 'bk', '23432', '']
['c', 'ck', '4354', '']
['m', 'mk', '2343', '']
['n', 'nk', '34444432', '']'''


################################################################################
import csv
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
print(tmp)
file = open("Books.csv","r")
#start = int(input("starting year: "))
#end = int(input("Ending year: "))
for row in tmp:
    print(tmp)
    # if int(tmp[x][2]) >=start and int(tmp[x][2]) <=end:
        #print(tmp[x])
        #x = x+1
'''PS C:\VSCode\Pythonhardway> python -u "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py"
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]
[['To Kill A Mockingbird', ' Harper Lee', ' 1960'], ['A Brief History of Time', ' Stephon Hawking', ' 1988'], ['The Great Gatsby', ' F.Scott Fitzgerald', ' 1922'], ['The Man 
Who Mistook His Wife for a Hat', ' Oliver Sacks', ' 1985'], ['Pride and Prejudice', ' Jane Austen', ' 1813'], ['a', 'b', '34', ''], ['a', 'ak', '1221', ''], ['b', 'bk', '2132', ''], ['c', 'ck', '3433', ''], ['a', 'ak', '2323', ''], ['b', 'bk', '2332', ''], ['a', 'ak', '2112', ''], ['b', 'bk', '2332', ''], ['c', '23432', '3232', ''], ['a', 'ak', '3243', ''], ['b', 'bk', '23432', ''], ['c', 'ck', '4354', ''], ['m', 'mk', '2343', ''], ['n', 'nk', '34444432', '']]'''




################################################################################
import csv
file = open("Books.csv","r")
x = 0
for row in file:
    print("Row: " + str(x) + "-"+ row)
    x = x + 1
file.close()

#    print("Row: " + (x)  + "-"+ str(row))
# TypeError: can only concatenate str (not "int") to str
# all must be in str form
'''Row: 0-To Kill A Mockingbird, Harper Lee, 1960

Row: 1-A Brief History of Time, Stephon Hawking, 1988

Row: 2-The Great Gatsby, F.Scott Fitzgerald, 1922

Row: 3-The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985

Row: 4-Pride and Prejudice, Jane Austen, 1813

Row: 5-a,b,34,'''


################################
'''    del Booklist[getrid]
TypeError: list indices must be integers or slices, not str means getrid must be int or slices'''
"""Especially Care:-    x = 0
    for i in fruits:
        print(x,i)
        x = x+1
    del_fruit = input("Enter fruits name which you want to delete: ")
    dfruit =  fruits.index(del_fruit)"""

################################

import csv
import random
score = 0
name = input("Enter your name: ")
q1_num1 = random.randint(10,50)
q1_num2 = random.randint(10,50)
question1 = str(q1_num1) + " + " + str(q1_num2) + "=" 
ans1 = int(input(question1))
realans1 = q1_num1  + q1_num2
if ans1 == realans1:
    score = score + 1
q2_num1 = random.randint(10,50)
q2_num2 = random.randint(10,50)
question2 = str(q2_num1) + " + " + str(q2_num2) + "=" 
ans2 = int(input(question2))
realans1 = q2_num1  + q2_num2
if ans2 == realans1:
    score = score + 1
    
file = open("QuizScore.csv","a")
newrecord = name + "," + question1 + "," + str(ans1) + "," + question2 + "," + str(ans2) + "," + str(score) + "\n"
file.write(newrecord)  


########################################################################

########################################################################
'''    fruits[alt_fruit] = fruit_name
TypeError: list indices must be integers or slices, not str   
Remember:-[] # In this braket usually int exist either in the case of chaning item or delting items in the list
PS C:\VSCode\Pythonhardway> '''
###You can chnge input in indexing before altring or deleting or directly take integer input
########################################################################


################################################################################
'''def delete():
    file = list(csv.reader(open("Salaries.csv")))
    salary = []
    for row in file:
        salary.append(row)

    x = 0
    for row in salary:
        print(x,salary[x])
        x = x + 1
    delete_itm = int(input("Enter the name you want to  delete: "))
    del salary[delete_itm] ##After dwlting or altering we must to rewrite
##in this way> 
    file = open("Salaries.csv","w")
    x = 0
    for row in salary:
        nwrecord = salary[x][0] + "," + salary[x][1] + "\n"
        x = x + 1
        file.write(nwrecord)
    file.close() '''
    
################################################################################



################################################
  
'''    file = list(csv.reader(open("Salaries.csv")))
    salary = []
    for row in file:
        salary.append(row)
#############       Do not confuse 
    x = 0
    for row in salary:
        print(x,salary[x])
        x = x + 1

    x = 0
    for row in salary:
        print(x,row)
        x = x + 1 '''
        
#####################################################

##########
# entry_box.focus()
#########



#####################################################

from tkinter import*
import random
def dice():
    dice_num = random.randint(1,7)
    entry_box = Message(window, text = dice_num)
    entry_box.place(x = 125,y = 20,width = 100, height = 30)
    entry_box["justify"] = "center"
    entry_box["bg"] = "black"
    entry_box["fg"] = "white"

    

window = Tk()
window.geometry("720x480")
label = Label(text = "Roll a dice")
label.place(x = 10,y = 20)

button = Button(text = "roll", command = dice)
button.place(x = 150,y = 50,width = 50,height =25)
button["bg"] = "black"
button["fg"] = "white"
window.mainloop()

### OR
from tkinter import*
import random
def dice():
    dice_num = random.randint(1,7)
    entry_box["text"] = dice_num #Note


window = Tk()
window.geometry("720x480")
label = Label(text = "Roll a dice")
label.place(x = 10,y = 20)
entry_box = Message(window, text = "")
entry_box.place(x = 125,y = 20,width = 100, height = 30)
entry_box["justify"] = "center"
entry_box["bg"] = "black"
entry_box["fg"] = "white"
button = Button(text = "roll", command = dice)
button.place(x = 150,y = 50,width = 50,height =25)
button["bg"] = "black"
button["fg"] = "white"
window.mainloop()

#########################################################

#$$$$$

'''  File "c:\VSCode\Pythonhardway\tempCodeRunnerFile.py", line 16
    del numbox(0,END)
        ^
SyntaxError: cannot delete function call
[numbox.delete(0,END)] it would be work

*   2nd point = , in add
    answer = int(answer)
ValueError: invalid literal for int() with base 10: ''        
means here in answer = mssg_box["text"] # text = 0


entry_box.delete(0, END) 
#Deletes the contents of an entry or 
list box. 
'''
#$$$$$

################################
'''def add():
        num = numbox.get()
        num = int(num)
        answer = mssg_box["text"]
        answer = int(answer)
        total = num + answer
        mssg_box["text"] = total
        numbox.delete(0,END)

def reset():
    total = 0
    mssg_box["text"] = 0
    numbox.delete(0,END)
    numbox.focus()
    



window = Tk()
window.geometry("720x480")
label = Label(text ="Add Number")
label.place(x = 10, y = 20)
numbox = Entry(text =0)
numbox.place(x = 100, y = 20, width = 150, height = 25)
numbox["bg"] = "blue"
numbox["fg"] = "yellow"
numbox["justify"] = "center"
label = Label(text ="Answer")
label.place(x = 10, y = 80)
mssg_box = Message(text =0)
mssg_box.place(x = 100, y = 75, width = 150, height = 25)
mssg_box["bg"] = "green"
mssg_box["fg"] = "yellow"
mssg_box["justify"] = "center"
add_button = Button(text="Add", command =add)
add_button.place(x = 90, y = 110, width =50,height = 25)
reset_button = Button(text="reset", command = reset)
reset_button.place(x = 175, y = 110, width =50,height = 25)
window.mainloop()

'''
################################

################################
'''    miles = textbox1.get()
    miles = int(miles) '''
    
    
#Listbox() parenthesis  empty
################################



################################################################

from tkinter import*
import csv
def add():
    num = numbox.get()
    if num.isdigit():
        listbox.insert(END,num)
        numbox.delete(0, END)
        numbox.focus()
    else:
        numbox.delete(0,END)
        numbox.focus()


def clear():
    listbox.delete(0,END)
    
def addcsv():
    file = open("namelist.csv", "w")
    tmp_list = listbox.get(0,END)
    item = 0
    for x in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item +1
    file.close()
    

window = Tk()
window.title("Digichecker")
window.geometry("720x480")
label = Label(text = "Enter a number")
label.place(x = 10,y = 20)
numbox = Entry(text = " ")
numbox.place(x = 125,y = 50)
numbox["justify"] = "center"
numbox.focus()
listbox = Listbox()
listbox.place(x = 150,y = 150)
listbox["justify"] = "center"
button1 = Button(text="Add", command = add)
button1.place(x = 150,y = 80, width = 50, height = 20)
button2 = Button(text="clear", command = clear)
button2.place(x = 200,y = 80, width = 50, height = 20)
button3 = Button(text="addcsv", command = addcsv)
button3.place(x = 300,y = 80, width = 50, height = 20)
window.mainloop()
########################################################################


########################################################################

from tkinter import*
import csv
def create():
    file = open("Details.csv","w")
    file.close()

def add():
    file = open("Details.csv","a")
    name = namebox.get()
    age = agebox.get()
    record = name + " , " + str(age) + "\n"
    file.write(record)
    namebox.delete(0,END)
    agebox.delete(0,END)
    namebox.focus()
    
def show():
    listbox.delete(0,END)
    file = list(csv.reader(open("Details.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        listbox.insert(END,data)
        x = x+1

window = Tk()
window.geometry("720x480")
window.title("File")
label1 = Label(text = "Enter the name: ")
label1.place(x = 10, y= 20)
namebox = Entry(text = "")
namebox.place(x = 150, y= 20)
namebox["justify"] = "center"
namebox.focus()
label2 = Label(text = "Enter your age: ")
label2.place(x = 10, y= 50)
agebox = Entry(text = "")
agebox.place(x = 150, y= 50)
agebox["justify"] = "center"
agebox.focus()
button = Button(text = "Create", command = create)
button.place(x = 200, y = 250)
button2 = Button(text = "Add", command = add)
button2.place(x = 250, y = 250)
button3 = Button(text = "show", command = show)
button3.place(x = 300, y = 250)
listbox = Listbox()
listbox.place(x = 250, y = 350)
window.mainloop()

############################################################################

############################################################################

from tkinter import*
def show():
    name = namebox.get()
    mssg = ("Hello" + " " + name)
    mssgbox["text"] = mssg    
    namebox.delete(0,END)
    
window = Tk()
window.title("Names")
window.wm_iconbitmap("icon.ico")
window.geometry("720x480")
window.configure(backgroun = "light green")
logo = PhotoImage(file = "log.gif")
logobox = Label(image = logo) 
logobox.place(x = 30, y = 10 ,width = 200 ,height = 150)
label = Label(text = "Enter your name")
label.place(x = 10, y = 200,width = 150, height = 25)
label["bg"] = "black"
label["fg"] = "white"
namebox = Entry(text = "")
namebox.place(x = 150, y = 200,width = 150, height = 25)
namebox["justify"] = "center"
namebox.focus()
button = Button(text = "press me", command = show)
button.place(x = 10, y = 250,width = 150, height = 25)
button["bg"] = "yellow"
mssgbox = Message(text = "")
mssgbox.place(x = 150, y = 250, width = 150, height = 25)
label["fg"] = "black"
label["bg"] = "white"
window.mainloop()

########################################################################

########################################################################
'''
from tkinter import*
def show():
    colour = drop_down.get()
    window.configure(background = colour)
'''
###Note StringVar not stringVar or stringvar
##drop_down.set("grey") here grey is name of dropdownmenu or on the top
'''gendr = StringVar(window)
gendr.set("gender")
genderlist = OptionMenu(window,gendr,"male","female")
def add():
    mssg = namebox.get()
    new_mssg = mssg + " ," + str(gendr.get()) # don't forget to get objects from dropdownmenu
    namelist.insert(END,new_mssg)
    namebox.delete(0,END)

'''


'''
A primary key is the field (usually the first one) in each table that 
stores the unique identifier for that record. Therefore, in the Employees 
table the primary key will be the ID column and in the Department table 
the primary key will be Dept. 

 integer: the value is an integer value; 
 real: the value is a floating-point value; 
 text: the value is a text string; 
 blob: the value is stored exactly as it was input. 

'''



########################################################################

##########################################################
##########################################################
'''
import sqlite3 
This must be the first line of the program to allow Python to use the SQLite3 library. 

with sqlite3.connect(“company.db”) as db: 
    cursor=db.cursor() 
Connects to the company database. If no such database exists, it will create one.
The file will be stored in the same folder as the program. 

cursor.execute(“““CREATE TABLE IF NOT EXISTS employees( 
    id integer PRIMARY KEY, 
    name text NOT NULL, 
    dept text NOT NULL, 
    salary integer);”””) 
Creates a table called employees which has four fields (id, name, dept and salary). It 
specifies the data type for each field, defines which field is the primary key and which 
fields cannot be left blank. The triple speech marks allow the code to be split over 
several lines to make it easier to read rather than having it all displayed in one line.

cursor.execute(“““INSERT INTO employees(id,name,dept,salary) 
    VALUES(“1”,”Bob”,”Sales”,”25000”)”””) 
db.commit() 
Inserts data into the employees table. The db.commit()line saves the changes. 

newID = input(“Enter ID number: ”) 
newame = input(“Enter name: ”) 
newDept = input(“Enter department: ”) 
newSalary = input(“Enter salary: ”) 
cursor.execute(“““INSERT INTO employees(id,name,dept,salary) 
    VALUES(?,?,?,?)”””,(newID,newName,newDept,newSalary)) 
db.commit() 
Allows a user to enter new data which is then inserted into the table.


cursor.execute(“SELECT * FROM employees”) 
print(cursor.fetchall()) 
Displays all the data from the employees table. 

db.close() 
This must be the last line in the program to close the database. 

cursor.execute(“SELECT * FROM employees”) 
for x in cursor.fetchall(): 
    print(x) 
Displays all the data from the employees table and displays each record on a separate line. 

cursor.execute(“SELECT * FROM employees ORDER BY name”) 
for x in cursor.fetchall(): 
    print(x) 
Selects all the data from the employees table, sorted by name,and displays each record on a separate line.

cursor.execute(“SELECT * FROM employees WHERE salary>20000”) 
Selects all the data from the employees table where the salary is over 20,000. 

cursor.execute(“SELECT * FROM employees WHERE dept=‘Sales’”) 
Selects all the data from the employees table where the department is “Sales”.

cursor.execute(“SELECT id,name,salary FROM employees”) 
Selects the ID, name and salary fields from the employees table. 
cursor.execute(“““SELECT employees.id,employees.name,dept.manager 
    FROM employees,dept WHERE employees.dept=dept.dept 
    AND employees.salary >20000”””) 
Selects the ID and name fields from the employees table and the manager field from the department table if the salary is over 20,000. 

whichDept = input(“Enter a department: ”) 
cursor.execute(“SELECT * FROM employees WHERE dept=?”,[whichDept])
for x in cursor.fetchall(): 
    print(x) 
Allows the user to type in a department and displays the records of all the employees in that department. 

cursor.execute(“““SELECT employees.id,employees.name,dept.manager 
    FROM employees,dept WHERE employees.dept=dept.dept”””) 
Selects the ID and name fields from the employees table and the manager field from the 
department table, using the dept fields to link the data. If you do not specify how the 
tables are linked, Python will assume every employee works in every department and 
you will not get the results you are expecting. 

cursor.execute(“UPDATE employees SET name = ‘Tony’ WHERE id=1”) 
db.commit() 
Updates the data in the table (overwriting the original data) to change the name to“Tony” for employee ID 1. 

cursor.execute(“DELETE employees WHERE id=1”)

'''
##########################################################
##########################################################

################################
'''
cursor.execute("""SELECT employees.id,employees.name, employees.dept,
    from employees,###notedept WHERE employees.dept = dept.dept AND employees.salary> 20000""") 
'''
################################

##########################################################
'''
If you want SQL to IGNORE that error and continue adding other records , then do this :

Noted:- INSERT or IGNORE into tablename VALUES (value1,value2 , so on );
if you want to replace the values in the table whenever the entry already exists , then do this:

Noted:-INSERT or REPLACE into tablename VALUES (value1,value2 , so on );

'''
##########################################################


##########################################################
import sqlite3
with sqlite3.connect("phonebook.db") as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS names(
    id integer PRIMARY KEY,
    firstname text,
    surname text,
    phonenumber integer);""")
cursor.execute("""INSERT or IGNORE INTO names(id, firstname,surname,phonenumber)
               VALUES("1","Simon","Howels","01223349752")""")
db.commit()
cursor.execute("""INSERT or IGNORE INTO names(id,firstname,surname,phonenumber)
               VALUES("2","Karen","Philips","01954295773")""")
db.commit()
cursor.execute("""INSERT or IGNORE INTO names(id,firstname,surname,phonenumber)
               VALUES("3","Daren","Smith","01583749012")""")
db.commit()
cursor.execute("""INSERT or IGNORE INTO names(id,firstname,surname,phonenumber)
               VALUES("4","Anne","Jones","01323567322")""")
db.commit()
cursor.execute("""INSERT or IGNORE INTO names(id,firstname,surname,phonenumber)
               VALUES("5","Mark","Smith","012238555534")""")
db.commit()
db.close()
##########################################################


##########################################################
##########################################################

import sqlite3
def view():
    with sqlite3.connect("Phonebook.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM names")
        for x in cursor.fetchall():
            print(x)
        db.commit()    
        
    
def add():
    with sqlite3.connect("Phonebook.db") as db:
        cursor = db.cursor()
        newID = int(input("Enter ID: "))
        newFirstname = input("Enter FirsName: ")
        newSurname = input("Enter Surname: ")
        newPhoneNumber = int(input("Enter PhoneNumber: "))
        cursor.execute("""INSERT OR IGNORE INTO Names(ID,FirstName,Surname,PhoneNumber)
                    VALUES(?,?,?,?)""",(newID,newFirstname,newSurname,newPhoneNumber))
        db.commit()


def search():
    with sqlite3.connect("Phonebook.db") as db:
        cursor = db.cursor()
        surname = input("Enter surname: ")
        cursor.execute("SELECT * FROM Names WHERE Surname =?",[surname])
        for x in cursor.fetchall():
            print(x)
        db.commit()
        
def delete():
    with sqlite3.connect("Phonebook.db") as db:
        cursor = db.cursor()
    sel_Id = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE ID = ?",[sel_Id])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()
    
def update():
    with sqlite3.connect("Phonebook.db") as db:
        cursor = db.cursor()
    cursor.execute("UPDATE Names SET FirstName = 'Tony' WHERE ID = 1")
    for x in cursor.fetchall():
        print(x)
    db.commit()

def main():
    tryagain = False
    while tryagain == False:
        print("1)View phone book")
        print("2)Add to phonebook")
        print("3)Search for surname")
        print("4)Delete person from phone book")
        print("5)update person from phone book")
        print("6) Quit")
        selection = int(input("Enter your selection: "))
        if selection ==1:
            view()
        elif selection == 2:
            add()
        elif selection == 3:
            search()
        elif selection == 4:
            delete()
        elif selection == 5:
            update()
        elif selection == 6:
            tryagain = True
            quit()
main()

#Note1:- close the db file after complete action else return on same objects if you call to that function
#Note2:- Always use single quote ['] in double qoute["] and Vice versa don"t use same during nasting quotes
#Note3:- don't forget to stick * notationjust after from
##########################################################
##########################################################


##########################################################
##########################################################
import sqlite3
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()
cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)
print()
place = input("Enter place of birth: ")
cursor.execute("SELECT Books.Title, Books.Date_Published, Books.Author FROM Books, Authors WHERE Authors.Name = Books.Author AND Authors.PlaceofBirth=?""",[place])
for x in cursor.fetchall():
    print(x)
db.close()
##########################################################
##########################################################


##########################################################

import sqlite3
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()
cursor.execute("SELECT * FROM Books")
for x in cursor.fetchall():
    print(x)
year = int(input("Enter year: "))
cursor.execute("""SELECT Books.Title,Books.Date_Published, Books.Author
            FROM Books WHERE Books.Date_Published > ? ORDER BY Date_Published""", [year])
for x in cursor.fetchall():
    print(x)
db.close()

##########################################################



##########################################################
##########################################################

import sqlite3
file = open("Booklist.text","w")
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()
name = input("Enter a name: ")
cursor.execute("SELECT * FROM Books WHERE Author = ?",[name])
for x in cursor.fetchall():
    newrecord = str(x[0]) + "-" + str(x[1]) + "-" + str(x[2]) + "-" + str(x[3]) + "\n"
    file.write(newrecord)
file = open("Booklist.text","r")
print(file.read())
# text = txt



# it could be done byb even directly write with x but
#this dont give p
import sqlite3
file = open("Booklist.text","w")
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()
name = input("Enter a name: ")
cursor.execute("SELECT * FROM Books WHERE Author = ?",[name])
for x in cursor.fetchall():
    # newrecord = str(x[0]) + "-" + str(x[1]) + "-" + str(x[2]) + "-" + str(x[3]) + "\n"
    file.write(x)  #Always note text always write append or read in str foramt make sure it  be in str foramt if not then convert in
file = open("Booklist.text","r")
print(file.read())


###HENCE
import sqlite3
file = open("Booklist.text","w")
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()
name = input("Enter a name: ")
cursor.execute("SELECT * FROM Books WHERE Author = ?",[name])
for x in cursor.fetchall():
    # newrecord = str(x[0]) + "-" + str(x[1]) + "-" + str(x[2]) + "-" + str(x[3]) + "\n"
    file.write(str(x))  #Always note text always write append or read in str foramt make sure it  be in str foramt if not then convert in
file = open("Booklist.text","r")
print(file.read())
# text = txt

#OR print in direct list manner
import sqlite3
file = open("Booklist.text","w")
with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()
name = input("Enter a name: ")
cursor.execute("SELECT * FROM Books WHERE Author = ?",[name])
for x in cursor.fetchall():
    # newrecord = str(x[0]) + "-" + str(x[1]) + "-" + str(x[2]) + "-" + str(x[3]) + "\n"
    file.write(str(list(x)))
file = open("Booklist.text","r")
print(file.read())
# text = txt

''' Note;-  file.write(x)
TypeError: write() argument must be str, not tuple'''
##########################################################
##########################################################


################################
alphabet = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def get_data():
    word = input("Enter  your message: ")
    word = word.lower()
    num = int(input("Enter a number (1-26): "))
    if num > 26 or num == 0:
        while num >26 or num == 0:
            num = int(input("Out of range, please enter a number (1-26): "))
    data = (word,num)
    return (data)

def make_code(word,num):
    new_word = ""
    for x in word:
        y= alphabet.index(x)
        y = y + num
        if y > 26:
            y = y - 27
        char = alphabet[y]
        new_word = new_word + char
    print(new_word)
    print()
    
    
def decode(word,num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y = y - num
        if y < 0:
            y = y + 27
        char = alphabet[y]
        new_word = new_word + char
        #println(new_word)  if you print in for loop then it would comes one by one like b/bc/bcd
    print(new_word) #if you print outside for loop then it store value till condition then print together all value
    print() #You can print all value in same line by this or using end = "" method

def main():
    again = True
    while again == True:
        print("1) Make a code")  
        print("2) Decode a message")
        print("3) Quit")
        print()
        selection = int(input("Enter your selection: "))
        if selection == 1:
            (word,num) = get_data()
            make_code(word,num)
        elif selection == 2:
            (word,num) = get_data()
            decode(word,num)
        elif selection == 3:
            again = False
        else:
            print("Incorrect selection")

main()    

########################### second method
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
            "p","q","r","s","t","u","v","w","x","y","z"]
def get_data():
    word = input("Enter mssg: ")
    word = word.lower()
    num = int(input("Enter number(1-26): "))
    while num > 26 or num == 0:
        num = int(input("Enter number(1-26): "))
    return word,num
    

def make_code(word, num):
    # word_out = ""
    for x in word:
        y = alphabet.index(x)
        y = y + num
        if y > 26:
            y = y-26
        char = alphabet[y]
        print(char,end = "")
    print()
        # word_out = word_out + char
        # print(word_out,end = "")
        
def decode(word,num):
    # word_out = ""
    for x in word:
        y = alphabet.index(x)
        y = y - num
        if y > 26:
            y = y+26
        char = alphabet[y]
        print(char,end = "")
    print()
        # word_out = word_out + char
        # print(word_out,end = "")
        
def main():
    while True:
        print("1) Make a code")
        print("2) Decode a message")
        print("3) quit")
        selection = int(input("Enter selection"))
        if selection ==1:
            word,num = get_data()
            make_code(word,num)
        elif selection ==2:
            word,num = get_data()
            decode(word,num)
        elif selection == 3:
            break
        else:
            print("Wrong selection")
main()           
    
#################################

################################################################
################################################################
#####remeber this
#first method
word = ""
for i in ["a","b","c","d","e","f","g","h"]:
    print(i)
    word = word + i
print(word)
#second method
for i in ["a","b","c","d","e","f","g","h"]:
    print(i,end = "")
    
#tablebox.insert(END,(number,"x", i,"=", number*i))   print() executed in terminal 
################################################################
################################################################
#     length = len(password) 
# TypeError: object of type 'int' has no len()
#tablebox.insert(END,(number,"x", i,"=", number*i)) here tablebox is Listbox


#################################
################################################################
'''   color_list = ["red","blue","pink","yellow","orange","green"]
    c1 = random.choice([color_list])

#REMEMBER if you give list directly the it would gonna to choose color,
# bcz you have given it not list object you directly give it a [color_list] list 
    
    
    '''
import random
color_list = ["red","blue","pink","yellow","orange","green"]
print(type([color_list]))
num = random.choice([color_list])
print(num)
num = random.choice(color_list)
print(num)
'''Terminal execution
(<class 'list'>
['red', 'blue', 'pink', 'yellow', 'orange', 'green']
red
PS C:\VSCode\Pythonhardway> )'''

###############################
###############################

import random
def select_colour():
    color_list = ["red","blue","pink","yellow","orange","green"]
    c1 = random.choice(color_list)
    c2 = random.choice(color_list)
    c3 = random.choice(color_list)
    c4 = random.choice(color_list)
    return c1,c2,c3,c4

def tryagain(c1,c2,c3,c4):
    print(c1,c2,c3,c4)
    while True:
        u1 = input("Select colour from colour_list: ")
        u1 = u1.lower()
        if u1 != "red" and u1 != "green" and u1 != "blue" and u1 !="orange" and u1 != "yellow" and u1 != "pink":
            print("Incorrect selection")
        else:
            break
        
    while True:
        u2 = input("Select colour from colour_list: ")
        u2 = u2.lower()
        if u2 != "red" and u2 != "green"and u2 != "blue" and u2 !="orange" and u2 != "yellow" and u2 != "pink":
            print("Incorrect selection")
        else:
            break
        
    while True:
        u3 = input("Select colour from colour_list: ")
        u3 = u3.lower()
        if u3 != "red" and u3 != "green" and u3 != "blue" and u3 !="orange" and u3 != "yellow" and u3 != "pink":
            print("Incorrect selection")
        else:
            break
    while True:
        u4 = input("Select colour from colour_list: ")
        u4 = u4.lower()
        if u4 != "red" and u4 != "green" and u4 != "blue" and u4 !="orange" and u4 != "yellow" and u4 != "pink":
            print("Incorrect selection")
        else:
            break
    correct = 0
    wrong_place = 0
    if u1 == c1:
        correct+=1
    elif u1 == c2 or u1 == c3 or u1 == c4:
        wrong_place+=1
    
    if u2 == c2:
        correct+=1
    elif u2 == c1 or u2 == c3 or u2 == c4:
        wrong_place+=1
    
    if u3 == c3:
        correct+=1
    elif u3 == c1 or u3 == c2 or u3 == c4:
        wrong_place+=1
    
    if u4 == c4:
        correct+=1
    elif u4 == c2 or u4 == c3 or u4 == c1:
        wrong_place+=1
    print("correct color in the correct place",correct)
    print("correct color in the wrong place",wrong_place)
    return correct,wrong_place

def main():
    (c1,c2,c3,c4) = select_colour()
    score = 0
    while True:
        correct, wrong_place = tryagain(c1,c2,c3,c4)
        score = score + 1
        if correct == 4:
            break
    print("you win!")
    print("You took",score, "guesses")
main()
###########################################################
###########################################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import random
def select_colour():
    color_list = ["red","blue","pink","yellow","orange","green"]
    c1 = random.choice(color_list)
    c2 = random.choice(color_list)
    c3 = random.choice(color_list)
    c4 = random.choice(color_list)
    return c1,c2,c3,c4

def tryagain(c1,c2,c3,c4):
    print(c1,c2,c3,c4)
    tryagain = False
    while tryagain == False:
        u1 = input("Select colour from colour_list: ")
        u1 = u1.lower()
        if u1 != "red" and u1 != "green" and u1 != "blue" and u1 !="orange" and u1 != "yellow" and u1 != "pink":
            print("Incorrect selection")
        else:
            tryagain = True
        
        
        
    tryagain = False
    while tryagain == False:
        u2 = input("Select colour from colour_list: ")
        u2 = u2.lower()
        if u2 != "red" and u2 != "green"and u2 != "blue" and u2 !="orange" and u2 != "yellow" and u2 != "pink":
            print("Incorrect selection")
        else:
            break
    tryagain = False
    while tryagain == False:
        u3 = input("Select colour from colour_list: ")
        u3 = u3.lower()
        if u3 != "red" and u3 != "green" and u3 != "blue" and u3 !="orange" and u3 != "yellow" and u3 != "pink":
            print("Incorrect selection")
        else:
            tryagain = True
            
    tryagain = False
    while tryagain == False:
        u4 = input("Select colour from colour_list: ")
        u4 = u4.lower()
        if u4 != "red" and u4 != "green" and u4 != "blue" and u4 !="orange" and u4 != "yellow" and u4 != "pink":
            print("Incorrect selection")
        else:
            tryagain = True
    correct = 0
    wrong_place = 0
    if u1 == c1:
        correct+=1
    elif u1 == c2 or u1 == c3 or u1 == c4:
        wrong_place+=1
    
    if u2 == c2:
        correct+=1
    elif u2 == c1 or u2 == c3 or u2 == c4:
        wrong_place+=1
    
    if u3 == c3:
        correct+=1
    elif u3 == c1 or u3 == c2 or u3 == c4:
        wrong_place+=1
    
    if u4 == c4:
        correct+=1
    elif u4 == c2 or u4 == c3 or u4 == c1:
        wrong_place+=1
    print("correct color in the correct place",correct)
    print("correct color in the wrong place",wrong_place)
    return correct,wrong_place

def main():
    (c1,c2,c3,c4) = select_colour()
    score = 0
    while True:
        correct, wrong_place = tryagain(c1,c2,c3,c4)
        score = score + 1
        if correct == 4:
            break
    print("you win!")
    print("You took",score, "guesses")
main()





import random
def select_colour():
    color_list = ["red","blue","pink","yellow","orange","green"]
    c1 = random.choice(color_list)
    c2 = random.choice(color_list)
    c3 = random.choice(color_list)
    c4 = random.choice(color_list)
    return c1,c2,c3,c4

def tryagain(c1,c2,c3,c4):
    print(c1,c2,c3,c4)
    while True:
        u1 = input("Select colour from colour_list: ")
        u1 = u1.lower()
        if u1 != "red" and u1 != "green" and u1 != "blue" and u1 !="orange" and u1 != "yellow" and u1 != "pink":
            print("Incorrect selection")
        else:
            break
        
    while True:
        u2 = input("Select colour from colour_list: ")
        u2 = u2.lower()
        if u2 != "red" and u2 != "green"and u2 != "blue" and u2 !="orange" and u2 != "yellow" and u2 != "pink":
            print("Incorrect selection")
        else:
            break
        
    while True:
        u3 = input("Select colour from colour_list: ")
        u3 = u3.lower()
        if u3 != "red" and u3 != "green" and u3 != "blue" and u3 !="orange" and u3 != "yellow" and u3 != "pink":
            print("Incorrect selection")
        else:
            break
    while True:
        u4 = input("Select colour from colour_list: ")
        u4 = u4.lower()
        if u4 != "red" and u4 != "green" and u4 != "blue" and u4 !="orange" and u4 != "yellow" and u4 != "pink":
            print("Incorrect selection")
        else:
            break
    correct = 0
    wrong_place = 0
    if u1 == c1:
        correct+=1
    elif u1 == c2 or u1 == c3 or u1 == c4:
        wrong_place+=1
    
    if u2 == c2:
        correct+=1
    elif u2 == c1 or u2 == c3 or u2 == c4:
        wrong_place+=1
    
    if u3 == c3:
        correct+=1
    elif u3 == c1 or u3 == c2 or u3 == c4:
        wrong_place+=1
    
    if u4 == c4:
        correct+=1
    elif u4 == c2 or u4 == c3 or u4 == c1:
        wrong_place+=1
    print("correct color in the correct place",correct)
    print("correct color in the wrong place",wrong_place)
    return correct,wrong_place

def main():
    (c1,c2,c3,c4) = select_colour()
    score = 0
    while True:
        correct, wrong_place = tryagain(c1,c2,c3,c4)
        score = score + 1
        if correct == 4:
            break
    print("you win!")
    print("You took",score, "guesses")
main()




import random
def select_colour():
    color_list = ["red","blue","pink","yellow","orange","green"]
    c1 = random.choice(color_list)
    c2 = random.choice(color_list)
    c3 = random.choice(color_list)
    c4 = random.choice(color_list)
    return c1,c2,c3,c4, color_list

def tryagain(c1,c2,c3,c4, color_list):
    print(c1,c2,c3,c4)
    while True:
        u1 = input("Select colour from colour_list: ")
        u1 = u1.lower()
        if u1 not in color_list:
            print("Incorrect selection")
        else:
            break
        
    while True:
        u2 = input("Select colour from colour_list: ")
        u2 = u2.lower()
        if u2 not in color_list:
            print("Incorrect selection")
        else:
            break
        
    while True:
        u3 = input("Select colour from colour_list: ")
        u3 = u3.lower()
        if u3 not in color_list:
            print("Incorrect selection")
        else:
            break
    while True:
        u4 = input("Select colour from colour_list: ")
        u4 = u4.lower()
        if u4 not in color_list:
            print("Incorrect selection")
        else:
            break
    correct = 0
    wrong_place = 0
    if u1 == c1:
        correct+=1
    elif u1 == c2 or u1 == c3 or u1 == c4:
        wrong_place+=1
    
    if u2 == c2:
        correct+=1
    elif u2 == c1 or u2 == c3 or u2 == c4:
        wrong_place+=1
    
    if u3 == c3:
        correct+=1
    elif u3 == c1 or u3 == c2 or u3 == c4:
        wrong_place+=1
    
    if u4 == c4:
        correct+=1
    elif u4 == c2 or u4 == c3 or u4 == c1:
        wrong_place+=1
    print("correct color in the correct place",correct)
    print("correct color in the wrong place",wrong_place)
    return correct,wrong_place

def main():
    (c1,c2,c3,c4,color_list) = select_colour()
    score = 0
    while True:
        correct, wrong_place = tryagain(c1,c2,c3,c4,color_list)
        score = score + 1
        if correct == 4:
            break
    print("you win!")
    print("You took",score, "guesses")
main()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


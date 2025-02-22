#print(s) Prints the message s to the console

print("Welcome to TIO102!")
print(100)
num = 101
s ="WELCOME to VS"
print(num)
print(s)
lst =["neha","geeta","sita"]
print(lst)
x =5
y =3
print(x+y)

#len(s) Returns the length of a list or string.
print(len(s))
print(len(lst))


#range(start, stop, step) Returns a sequence of numbers
range(10) #prints from 0 to 9
for ran in range(10):
    print(ran)

print(range(10)) ## Output: range(0, 10) prints the range object representation, not the actual numbers.

print(list(range(10)))

print(*range(10))

range(1,11)
print(list(range(1,11)))

range(0,30,5)
print(list(range(0,30,5)))

print(sum([num,x])) # used to sum iterable objects (like lists, tuples)
print(sum((num,x)))
print(sum([1,2,3,4]))

print(min(num,x))
print(min(5,2,3))
print(min([2,3,4,1,5]))
print(min(['a','b','c']))

print(max(num,x))
print(max(5,2,3))
print(max([2,3,4,1,15]))
print(max(['a','b','c']))

#List Methods & Syntax

lst.append(18)
print(lst)
lst.append("pramila")
print(lst)

lst.remove(18)# remove an element by value, not by index.
print(lst)

lst.pop(2)#To remove an element by index, use .pop(index):
print(lst)

lst.sort()
print(lst)

lstn = [4,6,7,1]
print(lstn.sort())#sort() sorts the list in place and returns None

lstn = [100,4,6,7,1019]
lstn.sort()
print(lstn)

#String Methods & Syntax
print(s.lower())

snew  = "nothing is going to change my love for you"
print(snew.split())

snew  = "nothing-is-going-to-change-my-love-for-you"
print(snew.split('-'))

mestrg = ['nothing', 'is', 'going', 'to', 'change', 'my', 'love', 'for', 'you']

nmestrg = ' '.join(mestrg)
print(nmestrg)

mmestrg = '-'.join(mestrg)
print(mmestrg)

s1 ='           never say never     '
print(s1.strip())

s2 = '???????never say never?????????'
print(s2.strip('?'))

var1 = 10
var2 ="typing"
my_boolean = True

print(var1)
print(var2)
print(my_boolean)

x1 = 10
print(x1)

x1="chai"
print(x1)

#Conditionals
cond = 101
if cond > 1:
    print("greater than 1")

if cond > 105:
    print("greater than 100")

num1= 2100
num2 = 200

if num1 > num2:
    print("num1 is greater than num2")

elif num2 > num1:
     print("num2 is greater than num1")

num3 = 100
num4 = 100

if num3 > num4:
    print("num3 is greater than num4")
elif num4 > num3:
    print("num4 is greater than num3")
else:
    print("both are equal")

def function_example():
    print("function in python")

function_example()

def two_argument(a,b):
    return a+b

print(two_argument(3,7))

def strtwo_argument(a,b):
    return a+b

print(strtwo_argument("pramila"," om"))


def without_two_argument(a,b):
     a+b

print( without_two_argument(3,7)) 

name = "pramila"
print(f"Welcome to python ,{name}!!!")
print(f"lets practice now ,{name}")

print(f"sum of {num1} and {num2} is {num1+num2}")

print(5%2)
print(4%2)

#for loop
print("for loop")
listofnum = [1,2,8,10,34,89,0,4]
for elist in listofnum:
    print(elist)

liststrg = ["hema","neha","jaya","pushpa","nirma","sabun"]
for lststring in liststrg:
    print(lststring)

for i in range(10):
    print(i)

#while loop
# user_input = ''
# while user_input != "quit":
#     user_input = input("enter a command type quit to exit ")
# print("you exited the loop")

i = 1
while i < 6:
    print(i)
    i+=1

#infinite loop
# j = 1
# while j<6:
#     print(j)

# string is immutable and list are mutable
str1 = 'popo'
# str1[0] ='po'

list1 =['p','o','p','o']
list1[0] ='o'
print(list1)

#Advanced Concepts
#Built-in Functions

value = "pramila om"
for index,char in enumerate(value):
    print(index,char)

list2 =['koko','coco','soso','toto','fofo']
for index,string in enumerate(list2,start = 12):
    print(index,string)


cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
  print(count, cereal)

stringlist = ['koko','coco','soso','toto','fofo']
numberlist= [2,6,9,3,6]
# print(zip(stringlist,numberlist))
zipped = zip(stringlist,numberlist)
print(list(zipped))

stringlist1 = ['koko','coco','soso','toto','fofo']
numberlist1 = [2,6,9]
# print(zip(stringlist,numberlist))
zipped1 = zip(stringlist1,numberlist1)
print(list(zipped1))

singers = ["neha kukur","shreya ghosal","sunidhi chauhan"]
print(singers)

albums =[
    ['mai hu na','jogi','mahi'],
    ['swadesh','momo','poco']
    ]
print(albums)

numbers =[
    [1],
    [1,2],
    [1,2,3]
]
print(numbers)

waterlevels = ["shallo",["deep",["deeper"]]]
print(waterlevels)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
firstablum = matrix[0]
# print(print)
print(firstablum)

matrix[2] =[10,20,30]
print(matrix)

matrix[2][2] =22
print(matrix)

matrix[1][2] ="update"
print(matrix)

#nested loop
for i in range(1,5):
    print("outer loop increment")
    for j in range(1,4):
        print(f" i = {i} j = {j}")

matrix2 = [
    [6,4,9],
    [2,1,5],
    [3,97,24],
    [12,54,78],
]

for row in matrix2:
    for column in row:
        print(column," ")
    print()

numbers1 =[3,5,7]
for num in numbers1:
    print(f"printing for {num}")

    while num >0:
        print(num)
        num -=1
    
    print("------")

    list3 = [1,2,3,4]
    double =[]

    for list in list3:
        double.append(list*3)
    
    print(double)

list4 = [1,2,3,4]
dob = []
for value in list4:
    print(value*2)

double2 = [value*2 for value in list4] #IMP
print(double2)

double = list4*4
print(double)

words = ["I","Love","Codepath!"]
result = []

for word in words:
    if len(word) > 5:
        result.append(word)

print(result)
print(words)
result2 = [word for word in words if len(word) > 5]
print(result2)

# read about Two Pointer Technique

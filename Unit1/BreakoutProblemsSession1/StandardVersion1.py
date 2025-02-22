#Problem 1: Hundred Acre Wood

def welcome():
    print("Welcome to The Hundred Acre Wood!")
welcome()

#Problem 2: Greeting
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
greeting("pramila")

#Problem 3: Catchphrase
def print_catchphrase(character):
    if character == "Pooh":
        print( "Oh bother!")
    elif character == "Tigger":
        print( "TTFN: Ta-ta for now!")
    elif character == "Eeyore":	
        print( "Thanks for noticing me.")
    elif character == "Christopher Robin":
        print( "Silly old bear.")
    else :
        print(f"Sorry! I don't know {character}'s catchphrase!")

#character = input("enter a character ")
# print_catchphrase(character)

#Problem 4: Return Item
def get_item(items, x):
    if(len(items) > x):
        print(items[x])
    else:
        print("None")
        

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

# Problem 5: Total Honey
# def sum_honey(hunny_jars):
#     print(sum(hunny_jars))

# hunny_jars = [2,3,4,5]
# sum_honey(hunny_jars)


def sum_honey(hunny_jars):
    total = 0
    for value in hunny_jars:
        total = value + total
    
    print(total)
    

hunny_jars = [2,3,4,5]
sum_honey(hunny_jars)

#Problem 6: Double Trouble
def doubled(hunny_jars):
    list =[]
    for n in hunny_jars:
        list.append(2*n)
    
    print(list)
    
hunny_jars = [1, 2, 3]
doubled(hunny_jars)

#Problem 7: Poohsticks
print("Problem 7")
def count_less_than(race_times, threshold):
    count = 0
    for n in race_times:
        if n < threshold:
            count+=1
	
    print(count)
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)

# Problem 8: Pooh's To Do's
print("Problem 8")

def print_todo_list(task):
    print("Pooh's To Dos:")
    for n in range(len(task)):
        print(f"{n+1}. {task[n]}")
     
     
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

# Problem 9: Pairs 
#check
def can_pair(item_quantities):
    for n in item_quantities:
        if n % 2 != 0:
            return False
    return True
    
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))


item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

# Problem 10: Split Haycorns #check
def split_haycorns(quantity):
    list = []
    n=1
    for n in range(1,quantity+1):
        if quantity%n == 0:
            list.append(n)
    print(list)
	

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)

# Problem 11: T-I-Double Guh-ER
def tiggerfy(s):
	print("".join([char for char in s if char.lower() not in "tiger"]))

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)

# Problem 12: Thistle Hunt
def locate_thistles(items):
    listing = []
    for index,string in enumerate(items):
        if string == 'thistle':
            listing.append(index)
    print(listing)

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
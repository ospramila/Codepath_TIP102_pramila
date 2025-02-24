# Problem 1: Batman
def batman():
    print("I am vengeance. I am the night. I am Batman!")
	
batman()
# Problem 2: Mad Libs

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")
	

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)

# Problem 3: Trilogy
def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight") 
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")
	

year = 2008
trilogy(year)

year = 1998
trilogy(year)

# Problem 4: Last
def get_last(items):
    length = len(items)-1
    if length > 0:
        print(items[length])
    else:
        print("None")
	
items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)

# Problem 5: Concatenate #check
def concatenate(words):
    result =""
    for item in words:
        result += item   
    print(f'{result}') 
    
words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)

# Problem 6: Squared
print("Squared") 
def squared(numbers):
    result =[]
    for n in numbers:
        result.append(n*n)
    print(result)
	
numbers = [1, 2, 3]
squared(numbers)
# Problem 7: NaNaNa Batman! check
def nanana_batman(x):
    result = ""
    for _ in range(x):
        result += 'na'
    result += ' batman!'
    print(result)

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
# Problem 8: Find the Villain
def find_villain(crowd, villain):
    listResult = []
    for index,string in enumerate(crowd):
        if crowd[index] == villain:
            listResult.append(index)
    print(listResult)

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)

# Problem 9: Odd
def get_odds(nums):
    listResult1 =[]
    for num in nums:
        if(num%2 !=0):
            listResult1.append(num)
    print(listResult1)
	

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)

# Problem 10: Up and Down
def up_and_down(lst):
    countodd=0
    counteven=0
    result=0
    for num in lst:
        if num%2 ==0:
            counteven+=1
        else:
            countodd+=1
    result = countodd - counteven
    print(result)


lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)

# Problem 11: Running Sum//check
def running_sum(superhero_stats):
    sum =0
    for i in range(1,len(superhero_stats)):
        superhero_stats[i]+=superhero_stats[i-1]
    print(superhero_stats)
   

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)

# Problem 12: Shuffle
def shuffle(cards):
    midpoint = len(cards)//2
    listResult2 =[]
    for i in range(midpoint):
        listResult2.append(cards[i])
        listResult2.append(cards[midpoint+i])
    
    cards[:] = listResult2
    print(cards)
	

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
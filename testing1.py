'''player_name= "Lionel Messi"
sport= "Soccer"
achievements= 7

if achievements > 10:
    print (f"{player_name} plays {sport} and has {achievements} achievements")
else (f"{player_name} doesn't have more than 10 achievements.")'''

'''player_name= input (  "Player name is? ")
sport = input ("Tennis? ")
achievements= input ("Achievements ")

if sport == "Tennis" or achievements == 20:
     print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
     print(f"{player_name} does not meet the criteria.")'''


'''fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")'''
'''for x in ['A', 'B', 'C']:
    print(x + 'A')'''
'''L=[1,3,2]

c= sort(L) 
print(c)'''
'''for num in range(1, 6):
    if num == 3:
        continue
    print(num)'''

'''for i, x in enumerate(['A', 'B', 'C']): 
    print(i, 2 * x)
class Points(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 


p2 = Points(1, 2) 
p2.x = 2 
p2.print_point()

def add(a,b):
    return sum (a,b)
print (add(2,3))'''
'''# List of lines to write to the file
Lines = ["This is line 1", "This is line 2", "This is line 3"]
# Create a new file Example3.txt for writing
with open('Example3.txt', 'w') as file2:
    for line in Lines:
        file2.write(line + "\n")
    # file2 is automatically closed when the 'with' block exits
'''

import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)


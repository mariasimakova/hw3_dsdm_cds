from pathlib import Path

# 1)
def car_at_light(light):
    if light=='red':
        return 'stop'
    elif light=='green':
        return 'go'
    elif light=='yellow':
        return 'wait'
    else:
        raise Exception(f"Undefined instruction for color: {light}")
    
color=car_at_light('yellow')
print(color)

# 2) 
def safe_subtract(a,b):
    try:
        return b-a
    except TypeError:
        return None
    except Exception as x:
        print(f'An error ocurred: {x}')
        return None
    
y=safe_subtract(4,6)
print(y)

# 3)
# EAFP (Easier to Ask for Forgiveness than Permission)
def retrieve_age_eafp(person):
    current_year = 2024
    try:
        bday = person['birth']
        return current_year - bday
    except KeyError:
        return "Birth year not available"
    
# print(retrieve_age_eafp(person1))  
# print(retrieve_age_eafp(person2)) 

# LBYL (Look Before You Leap)
def retrieve_age_lbyl(person):
    current_year = 2024
    if 'birth' in person:
        bday = person['birth']
        return current_year - bday
    else:
        return "Birth year not available"

# Example Usage:
person1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
person2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}

print(retrieve_age_lbyl(person1)) 
print(retrieve_age_lbyl(person2))  

def read_data(file_path: str):
    try:
        with open(file_path) as file:
            _ = file.readlines()
            print(f'{file_path} file was read.')
    except FileNotFoundError:
        print(f'{file_path} file does not exist')
    
read_data("data.csv")
read_data("data1.csv")

"""
If the goal of the loop is to calculate sum of doubled elements from list, then the bug is that
elem is being added to total_double_sum. However, double should be added since elem is iterator of a list
and double is doubled iterator
"""
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double
    # total_double_sum += elem WRONG

"""
If the goal of the loop is to create string from list with underscores between each 
string of the list (and also in front of), then the mistake is that strings equals string + _ + string each iteration, 
however, we need to add iterator to strings to make it combine in a result while now just two iterators
summing up
"""
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = strings + "_" + string
    # strings = string+"_"+string WRONG

print(strings)

"""
The loop in current desing will be endless since j will be more than 0 with first iteration.
If the goal of the loop is to add 1 with each iteration while j becomes 10, then we need to replace 
10 and 0 and also to replace > with < to make it work
"""
j = 0
while j < 10:
    j += 1
    print(j)

# WRONG 
# j=10
# while j > 0:
#    j += 1

"""
Since we multiply each element of list to productory each iteration and productory is being 0
the result of whole loop will be the 0 for productory. If the goal of the loop is to multiply each element
of the list by each other in the order, we need to make productory 1
"""
productory = 1
# productory = 0 WRONG
for elem in [1, 5, 25]:
    productory *= elem
    print(productory)
    

    

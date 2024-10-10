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
    
print(retrieve_age_eafp(person1))  
print(retrieve_age_eafp(person2)) 

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

# 4) 
def read_data(file_name='data.csv'):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        return None
    

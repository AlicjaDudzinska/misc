name = input("What is your name? ")

print(name)

long_string = '''
YO
YO
YO
'''

print(long_string)

from datetime import date
birth_year = int(input("What year were you born? "))
year_now = date.today().year
age = year_now - birth_year
print(f"You are {age} years old")
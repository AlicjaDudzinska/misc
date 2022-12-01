#conditions
is_old = False
is_licenced = True

if is_old:
    print("You are old enough to drive")
elif is_licenced:
    print("You can drive now")
else:
    print("You cannot drive")

if is_old & is_licenced:
    print("You can drive now")
else:
    print("You cannot drive")

#Truthy and Falsy
username = "Alicja"
password = "123345"

if username and password:
    print("You are logged in!")
else:
    print("Check your credentials!")

#Ternary Operator
is_friend = False
can_message = "message allowed" if is_friend else "message not allowed"
print(can_message)

#Logical Operators
is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you are getting there")
elif not is_magician:
    print("You need magic powers")

#Loops
for item in "Alicja":
    print(item)

for item in (1,2,3,4,5):
    print(item)
    print(item)
    print(item)
print(item)

for item in [1,2,3]:
    for x in ['a','b','c']:
        print(item, x)

user = {
    "name": "Alicja",
    "age": 32
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

#counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for item in my_list:
    counter = counter + item

print(counter)

#range
print(range(100))

for number in range(5):
    print(number)

for number in range(0, 5, 2):
    print(number)

for x in range(0, 5, 2):
    print(list(range(10)))

#enumarate
for i,char in enumerate("Hello"):
    print(i, char)

for i, num in enumerate(list(range(100))):
    if num == 50:
        print(f'Index of 50 is: {i}')

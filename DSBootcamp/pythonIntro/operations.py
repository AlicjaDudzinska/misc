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
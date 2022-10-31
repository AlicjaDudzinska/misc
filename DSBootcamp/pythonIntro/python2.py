from turtle import back


print(type(int(str(100))))

a = str(100)
b = type(a)
print(b)

weather = "It\'s \"kind of\" sunny"
print(weather)

weather2 = "\t It\'s \"kind of\" sunny"
print(weather2)

weather3 = "It\'s \"kind of\" sunny \nI hope you have a nice day!"
print(weather3)

name = 'Alicja'
day = 100

print(f'Hi {name}. It\'s day {day}!')
print('Hi {0}. It\'s day {1}'.format(name, day))
print('Hi {1}. It\'s day {0}'.format(name, day))


selfish = "scooby doo pa pa"
print(selfish[6])
print(selfish[2:])
print(selfish[2::2])
print(selfish[-5])
print(selfish[::-1])

quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("not"))
print(quote.replace("not", "yeah"))

is_cool = True
print(type(is_cool))
print(bool(0))

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matrix[1][2])

basket =[1,2,3,4,5]

print(basket.append(100))
print(basket)

basket.insert(2, 200)
print(basket)

basket.extend([300,301])
print(basket)

newlist = basket.pop()
print(newlist)
print(basket)

newlist = basket.extend([1000])
print(newlist)
print(basket)

newlist = basket.remove(100)
print(newlist)
print(basket)

newlist = basket.clear()
print(newlist)
print(basket)

basket =[1,2,5,4,5]

print(5 in basket)
print(basket.count(5))
#print(basket.sort())
print(sorted(basket))

newlist = basket.copy()
print(newlist)

newlist.reverse()
print(newlist)

basket.reverse()
print(basket)

list = list(range(1,25))
print(list)

newsentence = " ".join(["Hi", "bro", "!"])
print(newsentence)

a,b,c,*mix,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(mix)
print(d)

mylist = [
    {"a": [1,2,3],
    "b": "hello",
    "x": False},
    {"a": [4,5,6],
    "b": "hello",
    "x": False}
]
print(mylist[0]["x"])
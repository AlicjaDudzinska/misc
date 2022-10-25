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
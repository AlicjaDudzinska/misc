from tkinter import HIDDEN


username = input("Your user name: ")
password = input("Your password: ")
passwordlenght = len(password)
hiddenpassword = passwordlenght * "*"

print(f"Hi {username}, your password, {hiddenpassword}, is {passwordlenght} letters long")
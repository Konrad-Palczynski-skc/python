from datetime import date
name = input("Enter dogs name: ")

d0 = date(2021, 2, 11)
d1 = date(2021, 3, 12)
days = d1 - d0
print("You have had", (name), "for", (days), "days")
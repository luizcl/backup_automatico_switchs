from datetime import date

name = input("What is your name? ")
print("Hello " + name)
birth_year = int(input("Enter yout birth year: "))
todays_date = date.today()
age = todays_date.year - birth_year;
print("Your age is " + str(age))
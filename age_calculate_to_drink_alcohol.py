from datetime import date
try:
    Birth_year = int(input('Enter the birth year: '))
except:
    print('Please enter valid number')
current_year = date.today().year
Age = current_year - Birth_year
if Age<18:
    print('Your are not eligible to drink alcohol', end=",")
else:
    print('Your are eligible to drink alcohol', end=",")
print("Your current age is {}".format(Age))

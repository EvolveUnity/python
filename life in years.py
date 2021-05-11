# storing input in age variable
age = input("what is your current Age? ")
#converting age variable to int 
age_as_int = int(age)
#for 90 years we are writing this program
years_remaining = 90 - age_as_int
# months x 12 = 1 year
months_remaining = years_remaining * 12
# weeks remaining weeks * 52
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
# storing data in message and printing message
message = (f"your have {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days")
print(message)
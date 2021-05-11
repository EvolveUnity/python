height = input("Enter your height in Meters:\n")
weight = input("Enter your weight in kgs:\n")
# appling bmi calculator formula bmi = weight divided by height square
bmi = int(weight)/float(height) ** 2
print(bmi)
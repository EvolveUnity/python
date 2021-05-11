height = float(input("Enter your height in Meters:\n"))
weight = float(input("Enter your weight in kgs:\n"))
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your Bmi is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your Bmi is {bmi}, You are normalweight.")
elif bmi < 30:
    print(f"Your Bmi is {bmi}, You are overweight.")
elif bmi < 35:
    print(f"Your Bmi is {bmi}, You are Obese.")
else:
    print(f"Your Bmi is {bmi}, You are Clinically obese.")
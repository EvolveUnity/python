print("Welcome to tip calculator!")
# storing the bill in bill variable with float
bill = float(input("what was the total bill? $"))
# storing the tip in tip variable with int
tip = int(input("what percentage tip would you like to give? "))
# storing the split people to a variable called people
people = int(input("How many people to split the bill? "))
# add formula with a tip divided by 100 * bill and adding the bill
bill_with_tip = tip / 100 * bill + bill
# dividing the tip for people
bill_per_people = bill_with_tip / people
# storing the final bill in a variable
final_amount = round(bill_per_people, 2)
# printing the final bill per person
print(f"Each person should pay {final_amount}")

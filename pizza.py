pizza_size = input("which size Pizza you want S,M,L? ")
add_pepper = input("do you want pepperoni ")
add_chesses = input("do you want pepperoni ")
bill = 0
if pizza_size == "S" or pizza_size == "s":
    bill += 15
elif pizza_size == "M" or pizza_size == "m":
    bill += 20
else:
    bill += 25
if add_pepper == "yes":
    if pizza_size == "S":
        bill += 2
        # This is for M and L size pizzas
    else:
        bill += 3
if add_chesses == "yes":
    bill += 1

print(f"your bill is {bill} .")

    

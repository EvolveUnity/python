height = int(input("what is your height in cm "))
bill = 0

if height >= 120:
    print("you can ride")

    age = int(input("what is your age? "))
    if age <= 12:
        bill = 5
        print("you have to pay $5")
    elif age <= 18:
        bill = 7
        print("you have to pay $7")
    else:
        bill = 12
        print("you have to pay $12")
    wants_photo = input("Do you want Photo Yes OR No ")
    if wants_photo == "yes":
        bill += 3

    print(f"You have pay ${bill}")
else:
    print("You Can't ride ")
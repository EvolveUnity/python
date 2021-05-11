print("Welcome to Treasure game You need to find treasure. Then your mission will completed.")
name = input("what is your name \n")
choice1 = input('you are Acrossed the road which way you want to go "Right" or "Left". \n').lower()
if choice1 == "left":
    choice2 = input('you came to a lake. There is a island middle of the lake. now chosse to "wait" for Boat until morning or "swim". \n').lower()
    if choice2 == "wait":
        choice3 = input('you arrived to island. There is three doors "blue", "red" & "yellow", chosse to open the correct treasure. \n' ).lower()
        if choice3 == "blue":
            print("blue room if filled with the water, Game Over")
        elif choice3 == "yellow":
            print(f"Hey {name} You won the Treasure. You lucky boy")
        elif choice3 == "red":
            print("The room is filled with fire and your dead man, Game over")
        else:
            print("You got attacked by angry trout. Gmae Over.")
    else:
        print("You got attacked by angry trout. Gmae Over.")

else:
    print("You got attacked by angry trout. Gmae Over.")
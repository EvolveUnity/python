def option1():
    print("You selected option 1")

def option2():
    print("You selected option 2")

def option3():
    print("You selected option 3")

def default():
    print("Invalid option")

# Create a dictionary that maps options to functions
options = {
    1: option1,
    2: option2,
    3: option3
}

# Example usage
choice = int(input("Enter an option (1-3): "))
options.get(choice, default)()

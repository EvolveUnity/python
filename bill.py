import random
test_seeds = int(input("give a seed \n"))
random.seed(test_seeds)
frnds_name = input("Give me everybody names by separating using by comma,\n")
names = frnds_name.split(",")
# print(len(names))
random_names = random.choice(names)
print(random_names +" " + "Has to pay the bill")
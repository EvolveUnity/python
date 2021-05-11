first_name = input("what is your name \n")
second_name = input("what is other name \n")

cname = first_name + second_name
lname = cname.lower()

t = lname.count("t")
r = lname.count("r")
u = lname.count("u")
e = lname.count("e")
true = t+r+u+e

l = lname.count("l")
o = lname.count("o")
v = lname.count("v")
e = lname.count("e")
love = l+v+o+e 
love_score = str(true) + str(love)
print(love_score)
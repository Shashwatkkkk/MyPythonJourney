print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill = bill+15
elif size == "M":
    bill =  bill+20
else:
    bill = bill+25
if add_pepperoni == "Y":
    if size == "L":
        bill = bill + 3
    elif size == "M":
        bill = bill + 3
    else:
        bill = bill + 2
else:
    bill = bill

if extra_cheese == "Y":
    bill = bill + 1
else:
    bill = bill
print(f"Your final bill is {bill}")
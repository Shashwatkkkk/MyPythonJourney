print("Welcome to the roller coster ride")
print("We hope you enjoy it")
height = int(input("Please enter your height in cm"))
if height>120:
    print("Hurrah, you are eligible to enjoy the ride")
    age = int(input("Enter your age"))
    if age <=18:
        print("You have to pay 7$")
    else:
        print("You have to pay 12$")
        photu = input("Do you want a pic?Yes or No")
        if photu == "yes":
            print("You need to pay 3$ more")
        else:
            print("Alright no problem")
else:
    print("Sorry, better luck next time")

num = int(input("Enter a number"))
new_num = num%2
if new_num == 1:
    print("It's an odd number")
else:
    print("It's an even number")
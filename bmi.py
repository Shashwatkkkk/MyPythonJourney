weight = int(input("Enter your weight"))
height = float(input("Enter your height"))
bmi = weight/(height*height)
if bmi<18.5:
    print("You are underweight")
elif bmi>18.5 and bmi<25:
    print("You are normal weight")
elif bmi>25 and bmi<30:
    print("You are slightly overweight")
elif bmi>30 and bmi<35:
    print("You are obese")
elif bmi>35 and bmi<40:
    print("You are clinically obese")
else:
    print("Bhagwan hi bchaye aapko ab")
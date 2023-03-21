age = int(input("Enter the age of the person:"))
ticket_bill = 0
if age>=12 and age<=20:
    ticket_bill = ticket_bill + 10
    print("Your ticket bill" + str(ticket_bill))
elif age>=21 and age<= 30:
    ticket_bill = ticket_bill + 20
    print("Your ticket bill" + str(ticket_bill))
elif age>=31 and age<=40:
    ticket_bill = ticket_bill + 30
    print("Your ticket bill" + str(ticket_bill))
else: 
    ticket_bill = ticket_bill + 40
    print("Your ticket bill" + str(ticket_bill))
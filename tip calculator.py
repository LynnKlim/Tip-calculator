
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_tip = float(total_bill*tip/100 + total_bill)
bill_per_person = "{:.2f}".format(bill_tip/people)
print(f"Each person should pay: ${bill_per_person}")

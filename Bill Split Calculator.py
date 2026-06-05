print("welcome to bill split calculator")
Total_bill = float(input("what was the total bill? $"))
tip=int(input("how much would you like to tip? "))
people=int(input("how many people to split the bill? "))
payment_per_person = (Total_bill + (Total_bill*tip/100))/people
print(f"each person should pay: ${payment_per_person:.2f}")
print("Welcome to the tip calculator\n")
bill = float(input("What was your total bill?\t$"))
people = int(input("How many people to split the bill?\t"))
tip_percentage = float(input("What percentage of tip would you like to give 10 12 15? \t"))

per_person = round(((bill + (bill * (tip_percentage / 100))) / people), 2)
print(f"Each person should pay ${per_person}")

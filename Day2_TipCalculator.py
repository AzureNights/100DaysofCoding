print("Welcome to your Tip Calculator!")

total_bill = float(input("What's the total bill?\n$"))
# print(type(total_bill))

percentage_tip = int(input("How much tip do you want to give? 10, 15, or 20%?\nPlease key in the numerical values only.\n"))

num_people = int(input("How many people would like to split this bill?\n"))

per_person = round((total_bill * (percentage_tip/100 + 1)) / num_people , 2)

per_person_format = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person_format}")


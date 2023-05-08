print("Welcome to the tip calculator")
bill_amount = int(input("What was the total bill?"))
tip_percentage = int(input("What percentage tip would like you to give?10, 12 or 15?"))
people = int(input("How many people to split the ball?"))
pay = (bill_amount + bill_amount*(tip_percentage/100))/people
final_pay = round(pay)
print(f"Each person should pay:${final_pay}")
print("welcome to the tip calculator ")
bill = float(input("what was the total amount of the bill ? \n"))
tip = int(input("what percentage amount was tipped ? \n"))
people = int(input("how many people are splitting the bill ? \n"))
bill_with_tip = tip/100 * bill+bill
split = bill_with_tip/people
print(f"the total amount a person must pay including a {tip}% tip is {split}")
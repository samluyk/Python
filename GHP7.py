#Sam Luyk

#The below are constants
QUARTER = int(25)
DIME = int(10)
NICKEL = int(5)
PENNY = int(1)

#introduction
print("Do you have the change for a dollar, we'll find out")

#Ask for what the user has
user_quarters = int(input("Enter how many quarters you have: "))
user_dimes = int(input("Enter how many dimes you have: "))
user_nickels = int(input("Enter how many nickels you have: "))
user_pennies = int(input("Enter how many pennies you have: "))

#Mathmatical equation for converting user inputs to cents
cents_penny = user_pennies * PENNY
cents_nickel = user_nickels * NICKEL
cents_dimes = user_dimes * DIME
cents_quarters = user_quarters * QUARTER

#Add it all together
total_cents = (((cents_penny + cents_nickel) + cents_dimes) + cents_quarters)

#Tell user about their total
if total_cents < 100:
    print("You have less than One US Dollar.")
elif total_cents == 100:
    print("You have One US Dollar.")
else:
    print("You've more than One US Dollar.")

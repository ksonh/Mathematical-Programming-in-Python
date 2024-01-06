####
## This program prompts the user for their marital status and their income, then calculates 
## the taxable income of the user based on whether their status is Single or Married.
## Designed by Kenneth Hanson.
##

maritalStatus = input("Are you married? Enter Y for yes and N for no: ")
income = float(input("Enter the taxable income for your family: "))
if income < 0:
   print("Error: Please enter a positive value for your taxable income.")
   exit()

married = maritalStatus.lower() == "y"

firstTaxBracket = 0.1
secondTaxBracket = 0.15
thirdTaxBracket = 0.25

name = input("Please enter your first name and last time: ")
if name.count("*") > 0 or name.count("-") > 0:
        print("Error: Please enter valid name with no special characters.")
        exit()

#If the person is Single, they are taxed at 10% if their income is below $8,000, 
#inclusive; if their income is over $8,000 and below $32,000, inclusive, they are taxed 
#at 15% for the amount over $8,000 with a $800 reduction; if their income if over $32,000, 
#they are taxed at 25% of the amount over $32,000 with a $4,400 reduction.
if not married:
    if income <= 8000:
        taxes = income * firstTaxBracket
    elif income <= 32000:
        taxes = (income - 8000) * secondTaxBracket + 800
    else:
        taxes = (income - 32000) * thirdTaxBracket + 4400
    print("Tax owned by " + name + ": $" + str(taxes))
#Else if they are Married, they are taxed at 10% if their income is below $16,000, inclusive; 
#if their income is over $16,000 and below $64,000, inclusive, they are taxed at 15% of the amount 
#over $16,000 with a $1,600 reduction; if their income is over $64,000, inclusive, they are taxed 
#at 25% of the amount over $64,000 with a $8,800 reduction. 
else:
    spouseName = input("Please enter your spouse’s first name and last time: ")
    if name.count("*") > 0 or name.count("-") > 0:
        print("Error: Please enter valid name with no special characters.")
        exit()
    if income <= 16000:
        taxes = income * firstTaxBracket
    elif income <= 64000:
        taxes = (income - 16000) * secondTaxBracket + 1600
    elif income > 64000:
        taxes = (income - 64000) * thirdTaxBracket + 8800
    print("Tax owned by " + name + " and " + spouseName + ": $" + str(taxes))
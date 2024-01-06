###
## The program asks the user if they would choose either 1) a million dollars right now
## or 2) one penny to double every day for the next 30 days. It then indicates whether 
## they made a good or bad decision.
## Designed by: Kenneth Hanson
##

INITIAL_BALANCE = 0.01
OPTION_1_DOLLARS = 1000000

#Initializes variables which will be used in the loop.
user_prompted = 0
day_count = 0
balance = INITIAL_BALANCE
while_complete = False

user_choice = int(input("1) Do you want a million dollars right now or 2) one penny which will double every day for 30 days? "))

#Makes sure user input is valid. If not, it prompts the user for their choice again.
while user_choice <= 0 or user_choice > 2:
    user_prompted = user_prompted + 1
    user_choice = int(input("1) Do you want a million dollars right now or 2) one penny which will double every day for 30 days? "))

#Doubles the balance 30 times.
for day_count in range (0, 30):
    balance_compounded = balance * 2
    balance = balance_compounded
    while_complete = True

#Calculates the money they would have generated if they went for option 2.
extra_money = balance - OPTION_1_DOLLARS

if user_choice == 1 and while_complete == True:
    print(f'You made the wrong choice. You missed out on ${extra_money:,}.')
elif user_choice == 2 and while_complete == True:
    print(f'The investment grew to ${balance:,} in 30 days. You received {extra_money:,} more dollars than what you would have received with option 1.')
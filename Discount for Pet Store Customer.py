##
## Program prompts the user to enter each price of a sale then a Y 
## for a pet or N for another item. A discount equal to 20 percent 
## of the cost of items in a sale other than the pets is added if the 
## customer buys one or more pets and at least five other items.
## Designed by: Kenneth Hanson
##

#Initializes the constant variable.
DISCOUNT_FRACTION = 0.20

def main() :
   prices = []
   isPets = []
   nItems = 0

   #Read all of the prices and pet statuses from the user and 
   #stores them in two lists.
   price = float(input("Enter price: "))

   while price >= 0:
        status = input("Status: ").upper()
        if price >= 0 and status == "N":
           nItems += 1
        else:
           isPets.append(status.upper())
        price = float(input("Enter price: "))
        if price >= 0 and status == "N":
           prices.append(price)

   #Computes and displays the discount amount.
   discount(prices, isPets, nItems)

## Computes the discount for a transaction.
#  @param prices the list of prices
#  @param isPet the list of True / False values indicating if it is a pet
#  @param nItems the number of items in the transaction
#  @return the amount that should be taken off as a discount
#
def discount(prices, isPet, nItems):
   amount = 0
   total = 0
   #Determines if customer is eligible for discount if they purchased a pet.
   if "Y" in isPet:
     if nItems >= 5:
        for price in prices:
            total += price
        amount = total * DISCOUNT_FRACTION
   print(f'Thank you for shopping with us. Your discount is: %0.2f' % amount)

if __name__ == '__main__':
   main()
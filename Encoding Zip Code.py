###
## This program takes a five-digit zip code and returns a bar code according 
## to the encoding scheme used by the United States Postal Service. If the sum 
## of the digits is not a multiple of 10, the sixth frame bar is set to 1. The digit 
## is computed from the bar code using the column weights 7, 4, 2, 1, 0, each of which 
## is multiplied by the 0 or 1 for that bar and added together, such as 
## 1 x 7 + 1 x 4 + 0 x 2 + 0 x 1 + 0 x 0 = 11. Then it creates a string of 0's and 1's corresponding 
## to each digit, and prints the bar code representation of each digit of the zip code. 
## Designed by: Kenneth Hanson.
##

def main():
    zip_code = input("Enter the five-digit zip code: ")
    while len(zip_code) > 5 or len(zip_code) < 5:
        zip_code = input("Enter the five-digit zip code: ")
    print(printBarcode(zip_code))

## Reads digit passed in as argument and loops through weight list to 
## to check if digit less the weight amuount is >= 0; if so add "|" to
## digit string, else add ":"
# @param digit the integer from zip_code
# @return bar_code string of bar code representation
def printDigit(d):
    digit = ""
    weightList = [7, 4, 2, 1]
    #Counts how many long bars are added.
    longCount = 0

    #Special case for 0 where d is set to 11.
    if d == 0:
        d = 11

    #Loops through weight list and builds barcode for one digit.
    for i in weightList:
        if d - i >= 0:
         digit += "|"
         longCount += 1
         d -= i
        else:
         digit += ":"

    #Accounts for fifth bar.
    if longCount % 2 == 0:
        digit += ":"
    else:
        digit += "|"

    return digit

## Calls printDigit() for every character in the passed in as the zipCode, 
## then returns the string of long bars and short bars for each digit,
## beginning with a long bar and ending with a long bar
# @param integers the sequence of integers in zipCode
# @return bar_code string of long bars and short bars for each digit
def printBarcode(zipCode):
    zipStr = str(zipCode)
    bar_code = "|"

    #Builds full barcode with each digit in zipcode.
    for i in range(5):
        bar_code += printDigit(int(zipStr[i]))

    #Calls check digit to append result.
    bar_code += checkDigit(zipCode)

    bar_code += "|"

    return bar_code

## Loops through each digit in zipCode to check if the sum of the digits
## is a multiple of 10, then calls printDigit() to print long bar or 
## short bar based on the remainder.
# @param integers the sequence of integers in zipCode
# @return long bar or short bar by calling printDigit()
def checkDigit(zipCode):
    zipStr = str(zipCode)
    sum = 0

    for char in zipStr:
        sum += int(char)

    remainder = sum % 10
    return printDigit(10 - remainder)

if __name__ == '__main__':
    main()
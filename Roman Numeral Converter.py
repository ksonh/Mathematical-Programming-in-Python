###
## This program takes roman numeral representation of a number and returns 
## the decimal equivalent.
## Designed by: Kenneth Hanson.
##

def main():
    Roman_numeral = input("Enter the roman numeral: ").upper()
    converted_string = convertRom(Roman_numeral)
    print(f'{converted_string:,}')

## Iterates through string of Roman numerals and returns 
## the decimal equivalent.
# @param Roman_numeral the string of Roman numerals
# @return decimal conversion of Roman numeral
def convertRom(roman):
    total = 0
    str = roman

    #Iterates through roman numeral until len(str) is 0.
    while len(str) > 0:
        #If len(str) ==1 or first numValue is >= numValue[1], the string is cut 
        #from left to right by 1.
        if len(str) == 1 or numValue(str[0]) >= numValue(str[1]):
            total += numValue(str[0])
            str = str[1:]
        #Else the difference of numValue(str[1]) - numValue(str[0]) is added 
        #to total and the string is cut by two characters from left to right.
        else:
            difference = numValue(str[1]) - numValue(str[0])
            total += difference
            str = str[2:]

    return total

## Iterates through list of pairs of Roman numerals and their decimal equivalents, returning
# the decimal representation if valid, else it returns 0 to stop the while loop in convertRom().
# @param letter the index character of Roman numerals string
# @return integer equivalent of character
def numValue(letter):
    symbol_list = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]
    for symbol, decimal in symbol_list:
        if letter == symbol:
            return decimal
    #A symbol following one of equal or greater value 
    #adds to the value, i.e. VIII = 5 + 1 + 1 + 1 = 8.
    #Only three identical symbols are used consecutively.
    #When numbers begin with 4 or 9, a symbol is placed before
    #one of greater value to subtract its value, i.e. XC = -10
    #+ 100 = 90 and MCMLXXXIX = 1,000 - 100 + 1,000 + 50 + 10 
    #+ 10 + 10 - 1 + 10 = 1,989. Exceptions include 4,000,
    #which is written as MMMMM. 

    #If no decimal is returned we return 0 to avoid
    #any effect on the calculations.
    return 0

if __name__ == '__main__':
    main()
##
## This program prompts for a multiple then the prints the 
## products of that multiple in a series of lists.
## Designed by: Kenneth Hanson.
##

def main():
    multiple = int(input("Enter multiple whose products you want in a series of lists: "))

    table = []
    for i in range(5):
        row = [0] * 6
        table.append(row)
    fillTable(table, multiple)
    for row in range(len(table)):
        print(table[row])
 
def fillTable(values, multiple):
    counter = 1
    #Notice we start the counter at 1 since we do not
    #want to include 0 at the start; with every
    #increment by 1, our numbers resemble the counts
    #of regular numbers--multiplied by 5. 
    for i in range(len(values)):
        for j in range(len(values[0])):
            values[i][j] = counter * multiple
            counter += 1
    return values
 
main()
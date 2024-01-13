##
## This program prompts for the number of days in the month followed by the weekday of 
## the first day, then prints a calendar with proper formatting.
## Designed by: Kenneth Hanson.
##


def main() :
    days = int(input("Number of days: "))
    while days > 31:
        days = int(input("Number of days: "))
    print()
    weekday = int(input("Weekday of first day (0 = Sunday): "))
    print()
    printCalendar(weekday, days)
 
##
# Prints a monthly calendar with a separate row for each week.
# @param firstColumn the column of the first day
# @param numberOfDays the number of days
def printCalendar(firstColumn, numberOfDays) :
    days_week = [("Su", 0), ("Mo", 1), ("Tu", 2), ("We", 3), ("Th", 4), ("Fr", 5), ("Sa", 6)]
    for day, day_index in days_week:
        day_printed = day
        if day_index < 6:
            print(" " + day_printed, end="")
        else:
            print(" " + day_printed, end="\n")
    first_day = firstColumn
    spaces_used = firstColumn
    for col in range(first_day):
        #First column consists of 3 spaces; this prints an
		#empty column up to the index of the first_day, i.e. 4
		# = Thursday.
        print(" " * 3, end="")
		#Notice we start from 1 to mark the first day, requiring
		#that we also add 1 to the numberOfDays to account for
		#the shift in the number space.
    for day_number in range(1, numberOfDays + 1):
        if spaces_used < 6:
            print('{0:>3}'.format(day_number), end="")
            spaces_used += 1
        elif spaces_used == 6:
            spaces_used = 0
            print('{0:>3}'.format(day_number), end="\n")

main()
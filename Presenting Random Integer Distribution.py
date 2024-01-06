###
## This program generates 1,000 random integers between 1 and 999,999,
## showing a histogram with the number of times that the first digit
## is 1, 2, 3, 4, 5, 6, 7, 8, or 9. The number with the most iterations 
## is shown in green; that with the lowest is shown in red.
## Designed by: Kenneth Hanson.
##

from random import randint
from matplotlib import pyplot

#Initializes counters for each digit.
number_1s = 0
number_2s = 0
number_3s = 0
number_4s = 0
number_5s = 0
number_6s = 0
number_7s = 0
number_8s = 0
number_9s = 0

for i in range(1000):
    di = randint(0, 1000000)
    #Takes randomly-generated number and assigns the first digit to val.
    val = str(di)[0]
    if val == "1":
        number_1s += 1
    if val == "2":
        number_2s += 1
    if val == "3":
        number_3s += 1
    if val == "4":
        number_4s += 1
    if val == "5":
        number_5s += 1
    if val == "6":
        number_6s += 1
    if val == "7":
        number_7s += 1
    if val == "8":
        number_8s += 1
    if val == "9":
        number_9s += 1

dataNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
data = [number_1s, number_2s, number_3s, number_4s,
        number_5s, number_6s, number_7s, number_8s, number_9s]
#Creates list for the counters then sorts the values in ascending order.
values = [number_1s, number_2s, number_3s, number_4s,
          number_5s, number_6s, number_7s, number_8s, number_9s]
values.sort()

fig, graph = pyplot.subplots()

#Iterates over the indices of the data list, then assigns the index
#to num and the corresponding counter to counterValue. 
for i in range(len(data)):
    num = dataNumbers[i]
    counterValue = data[i]
    #If the count is equal to the maximum count, the bar is colored green.
    if counterValue == values[8]:
        graph.bar(num, counterValue, color="green")
    #Else if the count is equal to the minimum count, the bar is colored red.
    elif counterValue == values[0]:
        graph.bar(num, counterValue, color="red")
    #In all other cases, the bar is colored blue.
    else:
        graph.bar(num, counterValue, color="blue")

graph.set_xlabel("Digit")
graph.set_ylabel("Number of Counts")

graph.set_title("1,000 Numbers\nFirst Digit Distribution")

pyplot.show()
###
## This program prints a table of integers from 0 to n, inclusive, 
## and their square roots.
## Designed by: Kenneth Hanson.
##

import math

n = int(input())
n_increase = 0

left_col_width = 2
right_col_width = 9

print(f"{'n':>{left_col_width}.1s} | {'Root of n':>{right_col_width}.9s}")
for n in range(0, n + 1):
    calculate_root = math.sqrt(n_increase)
    for i in range(0, 1):
    #Notice the dynamic field width formatting using >{} (to
    #align from right) and <{} (to align from left);
    #note that we define the field widths with variables.
        print(f"{n_increase:>{left_col_width}.0f} | {calculate_root:>{right_col_width}.6f}")
    n_increase += 1
    if n_increase == n:
        break
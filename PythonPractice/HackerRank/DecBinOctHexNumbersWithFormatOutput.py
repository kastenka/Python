"""
Given an integer 'n', print the following values for each integer from 'i' to 'n':
Decimal, Octal, Hexadecimal (capitalized), Binary.
The four values must be printed on a single line in the order specified above for each
from to . Each value should be space-padded to match the width of the binary value of
and the values should be separated by a single space.
"""


def print_formatted(number):
    num_list = []
    for i in range(1, number + 1):
        dec_n = str(i)
        oct_n = oct(i)[2:]
        hex_n = hex(i)[2:].upper()
        bin_n = bin(i)[2:]
        num_list.append([dec_n, oct_n, hex_n, bin_n])  # создаётся двумерный массив
    width = len(num_list[-1][3])  # ширина для rjust
    fillchar = " "
    for i in num_list:
        print(*(num.rjust(width, fillchar) for num in i))


print_formatted(17)



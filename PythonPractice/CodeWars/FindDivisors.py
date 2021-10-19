"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array
with all of the integer's divisors' (except for 1 and the number itself), from smallest to
largest. If the number is prime return the string '(integer) is prime'.
"""


# Variant 1
def divisors(integer):
    divisors_array = []
    for i in range(2, integer):
        if integer % i == 0:
            divisors_array.append(i)
        else:
            continue

    if len(divisors_array) >= 1:
        return divisors_array
    else:
        return "{} is prime".format(integer)


# Variant 2
def divisors2(integer):
    divisors_array = [i for i in range(2, integer) if integer % i == 0]
    return divisors_array or f"{integer} is prime"


while True:
    input_string = input("Enter the integer > 1: ")
    try:
        input_string = int(input_string)
    except ValueError as ex:
        print("Try again!\n")
        continue

    if input_string > 1:
        print(divisors2(input_string))  # print(divisors(input_string))
        break
    else:
        print("Try again!")
        continue

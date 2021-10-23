# TASK1: You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
    return "".join(i.lower() if i.isupper() else i.upper() for i in s)
    # or another variant: 
    # return s.swapcase()

    
# TASK2: You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    line = "-".join(line.split(" "))
    return line


# TASK3: In this challenge, the user enters a string and a substring. You have to print the number of times that
# the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


# TASK4: Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


# TASK5: You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
def solve(s):
    return " ".join(i.capitalize() for i in s.split(" "))


print("TASK1:  " + swap_case("hELLO fROM hell"))
print("TASK2:  " + split_and_join("S T R I N G"))
print("TASK3:  " + str(count_substring("LCACACL", "CAC")))
print("TASK4:  " + mutate_string("LALALA", 2, "w"))
print("TASK5:  " + mutate_string("masha kastenka"))

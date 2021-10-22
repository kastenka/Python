# You are given a string . Your task is to find out if the string contains:
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


# Variant 1
def find_out_what_is_the_string(string):
    print(any(i.isalnum() for i in string))
    print(any(i.isalpha() for i in string))
    print(any(i.isdigit() for i in string))
    print(any(i.islower() for i in string))
    print(any(i.isupper() for i in string))


# Variant 2
def find_out_what_is_the_string2(string):
    check_string = ["isalnum()", "isalpha()", "isdigit()", "islower()", "isupper()"]
    for pos, i in enumerate(check_string):
        eval(f'print(any(character.{check_string[pos]} for character in s))')


s = input("Enter the string: ")
find_out_what_is_the_string2(s)


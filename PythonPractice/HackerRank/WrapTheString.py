# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width .
import textwrap


# Variant1
def wrap(string, max_width):
    new_string = ""
    for pos, i in enumerate(string):
        if pos % max_width == 0 and pos != 0:
            new_string += "\n"
        new_string += i
    return new_string


# Variant 2 - using textwrap.wrap
def wrap2(string, max_width):
    new_string = "\n".join(textwrap.wrap(string, width=max_width))
    return new_string


print(wrap("1111122222333334444455555", 5))
print(wrap2("AAABBBCCCDDDEEE", 3))
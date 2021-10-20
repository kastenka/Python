"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string. The input string can be assumed
to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""
from collections import Counter


# Variant 1
def duplicate_count(text):
    dup_count = 0  # number of duplicates in text
    text = text.lower()
    for i in text:
        count = 0  # number of identical symbols
        for j in text:
            if i == j:  # check if symbols have duplicates
                count += 1
        if count > 1:
            text = text.replace(i, "")  # remove symbols if they have duplicates
            dup_count += 1
    return dup_count


# Variant 2
def duplicate_count2(text):
    text = text.lower()
    # using set to make the text without duplicates
    # using count to count the number of duplicates of each character
    dup_count = len([j for j in set(text) if text.count(j) > 1])  # number of duplicates in text
    return dup_count


# Variant 3
def duplicate_count3(text):
    text = Counter(text.lower())
    dup_count = len([c for c in text.values() if c > 1])
    return dup_count


input_string = 'aAbcAaBB1i11'
print(duplicate_count3(input_string))
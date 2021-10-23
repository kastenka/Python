# Split string 'S' into equal parts of length 'k'.
# Convert each part by removing any subsequent occurrences of non-distinct characters in the part.


# Variant 1
def merge_the_tools(string, k):
    list1 = []
    str1 = ""
    for i in string:
        str1 += str1.join(i)
        if len(str1) % k == 0:
            list1.append(str1)
            str1 = ""
    for i in list1:
        print("".join([j for j in list(dict.fromkeys(i))]))


merge_the_tools("AABCAAADA", 3)
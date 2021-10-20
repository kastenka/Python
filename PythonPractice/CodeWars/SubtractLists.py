"""
Your goal  is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
"""


# Variant 1
def array_diff(a, b):
    diff = (set(a) & set(b))
    array = [i for i in a if i not in diff]
    return array


# Variant 2
def array_diff2(a, b):
    array = [i for i in a if i not in b]
    return array


array1 = [1, 2, 2]
array2 = [2]
print(array_diff(array1, array2))
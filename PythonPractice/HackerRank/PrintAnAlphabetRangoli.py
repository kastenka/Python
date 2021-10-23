# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)
import string


def print_rangoli(size):
    alpha, alpha_list = string.ascii_lowercase, []
    for i in range(size):
        s = "-".join(alpha[i:size])
        alpha_list.append((s[::-1] + s[1:]).center(4*size-3, "-"))
    print("\n".join(alpha_list[::-1] + alpha_list[1:]))


print_rangoli(26)
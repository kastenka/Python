"""
Both players are given the same string.
Both players have to make substrings using the letters of the string

Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

A player gets +1 point for each occurrence of the substring in the string
"""
import itertools
import re


# Variant 1
def minion_game(string):
    player1, player2 = "Kevin", "Stuart"
    player1_count = player2_count = 0
    for i, j in itertools.combinations(range(len(string)+1), 2):
        if re.match(r"[AEIOU]", string[i:j]):
            player1_count += 1
        else:
            player2_count += 1
    if player1_count > player2_count:
        print(f"{player1} {player1_count}")
    elif player1_count < player2_count:
        print(f"{player1} {player1_count}")
    else:
        print("Draw")


# Variant 2 - it is faster
def minion_game2(string):
    player1, player2 = "Kevin", "Stuart"
    player1_count = player2_count = 0
    for i in range(len(string)):
        if string[i] in ["A", "E", "I", "O", "U"]:
            player1_count += len(string) - i
        else:
            player2_count += len(string) - i
    if player1_count > player2_count:
        print(f"{player1} {player1_count}")
    elif player1_count < player2_count:
        print(f"{player2} {player2_count}")
    else:
        print("Draw")


minion_game2("BANANA")

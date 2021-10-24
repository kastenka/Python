import re  # regular expression


# Variant №1
def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'A', 'E', 'I', 'O']  # Note: for this kata y isn't considered a vowel.
    for v in string_:
        for i in vowels:
            if v == i:
                string_ = string_.replace(v, "")
    return string_


# Variant №2
def disemvowel2(string_):
    vowels = "[aeiouAEIOU]"  # Note: for this kata y isn't considered a vowel.
    string_ = re.sub(vowels, "", string_)
    return string_


# Variant №3 using flags
def disemvowel3(string_):
    vowels = "[aeiou]"  # Note: for this kata y isn't considered a vowel.
    string_ = re.sub(vowels, "", string_, flags=re.IGNORECASE)
    return string_


# Variant №4 using flags
def disemvowel4(string_):
    vowels = "aeiou"  # Note: for this kata y isn't considered a vowel.
    string_ = "".join(i for i in string_ if i.lower not in vowels)
    return string_


myString = "This website is for losers LOL!"
res1 = disemvowel(myString)
res2 = disemvowel2(myString)
res3 = disemvowel3(myString)
res4 = disemvowel3(myString)
# Result: "Ths wbst s fr lsrs LL!"
if res1 == res2 == res3 == res4:
    print(f"You have the same result. You new string is '{res1}'")
else:
    print(f"You have different string: '{res1}', '{res2}', '{res3}', '{res4}' ")




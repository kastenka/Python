# Variant 1 - very looooooong
def reverse_words_order_and_swap_cases(sentence):
    word, array, counter = "", [], 0
    for i in sentence:
        counter += 1
        if i.isupper() and i != " ":
            word += i.lower()
        if not i.isupper() and i != " ":
            word += i.upper()
        if i == " ":
            if word != "":
                array.append(word)
                word = ""
            else:
                word = ""
        if counter == len(sentence) and i != " ":
            array.append(word)

    return " ".join(array[::-1])


# Variant 2
def reverse_words_order_and_swap_cases2(sentence):
    array, word = [], ""
    for pos, j in enumerate(sentence):  # use enumerate to check position
        if not j.isspace() or (not j.isspace() and pos != (len(sentence) - 1)):
            word += j
        if j == " " or pos == (len(sentence) - 1):
            word += " "  # add spaces between words
            array.append(word)
            word = ""
    sentence = "".join(character.lower() if character.isupper() else character.upper()
                       for element in array[::-1] for character in element)
    return sentence.rstrip()  # remove spaces at the end of a line


print(reverse_words_order_and_swap_cases2("aWESOME IS cODING"))
print(reverse_words_order_and_swap_cases2("kASTENKA mASHA IS NAME mY"))

def word_separator(sentence):

    new_sentence = ""
    new_sentence = ''.join([' ' + char if char.isupper() else char for char in sentence]).strip() + '.'
    new_sentence = new_sentence.capitalize()

    return new_sentence.strip()

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)

# Program #2, Donovan Thompson 3/21/2025

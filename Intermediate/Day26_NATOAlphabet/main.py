#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas
file_loc = "./nato_phonetic_alphabet.csv"
nato_alphabet_df = pandas.read_csv(file_loc)
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

print("Type 'q' to quit")
coding_words = True
while coding_words:
    user_word = input("Enter a word: ").upper()
    if user_word == 'Q':
        coding_words = False
    else:
        code_list = [nato_alphabet_dict[char] for char in user_word]
        printable_list = f"{code_list}"[1:-1]
        print(printable_list)
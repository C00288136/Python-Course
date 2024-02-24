student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter: row.code for (letter, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_in = input("Enter the word you want to translate ").upper()
    # here we can usualy make the output list by using the nato dict
    # and the letter as the key which then prints the word  as the output as thats what the key points at
    try:
        out_list = [NATO_dict[letter] for letter in user_in]
    except KeyError:
        # doing exception handling run same program after catch has been done to give the user another chance to input data
        print("Sorry only letters in the alphabet please")
        generate_phonetic()
    else:
        print(out_list)

generate_phonetic()

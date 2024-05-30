# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []
# open the list of names insert them in an array
with open("./Input/Names/invited_names.txt", "r") as names:
    for line in names:
        name = line.strip()
        name_list.append(name)

# open the starting letter and read the whole thing
with open("./Input/Letters/starting_letter.txt", mode="r") as start_letter:
    first_line = start_letter.read()

for name in name_list:
    replaced_letter = first_line.replace("[name]", name)

    output_file_name = f"./Output/ReadyToSend/{name}_Letter.txt"
    with open(output_file_name, "w") as output_file:
        output_file.write(replaced_letter)
# fin
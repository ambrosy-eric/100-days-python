def modify_letter(name):
    """
    Given a name and starting letter
    Insert the name into a new file for the output
    """
    starting_letter = open('./inputs/letters/starting_letter.txt', 'r')
    finished_letter = open(f'./outputs/readytosend/{name.lower()}_letter.txt', 'w')
    for line in starting_letter:
        finished_letter.write(line.replace('[name]', name))

    starting_letter.close()
    finished_letter.close()

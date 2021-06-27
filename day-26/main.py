import pandas as pd

def main():
    data = pd.read_csv('data/nato_phonetic_alphabet.csv')
    nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
    word = input("Enter the word you would like the NATO Phonetic Alphabet for: ").upper()
    result = [nato_dict[letter] for letter in word]
    print(result)


if __name__ == '__main__':
    main()
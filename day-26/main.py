import pandas as pd

def main():
    data = pd.read_csv('data/nato_phonetic_alphabet.csv')
    nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
    
    def _nato_alphabet():
        word = input("Enter the word you would like the NATO Phonetic Alphabet for: ").upper()
        try:
            result = [nato_dict[letter] for letter in word]
        except KeyError:
            print('Only letters are valid')
            _nato_alphabet()
        else:
            print(result)
    
    _nato_alphabet()


if __name__ == '__main__':
    main()
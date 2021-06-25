from utils.tools import modify_letter

def main():
    with open('./inputs/names/invited_names.txt', 'r') as file:
        names = [line.strip('\n') for line in file]
    for name in names:
        modify_letter(name)
        
if __name__ == '__main__':
    main()

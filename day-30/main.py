import tkinter
import secrets
import string
import pyperclip
import json
from random import randint, shuffle
from tkinter import messagebox

def main():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password():
        """
        Given a int for number of letters, numbers and symbols
        Generate a string with those requirements
        Return the string
        """
        password_entry.delete(0, tkinter.END)
        characters = []
        for number in range(randint(2, 4)):
            characters.append(str(secrets.randbelow(10)))
        for symbol in range(randint(2, 4)):
            characters.append(secrets.choice(string.punctuation))
        for letter in range(randint(8, 16)):
            characters.append(secrets.choice(string.ascii_letters))
        shuffle(characters)
        password = ''.join(characters)
        password_entry.insert(0, password)

    def copy_password():
        """
        Copy the values in the password entry to the clipboard
        """
        pyperclip.copy(password_entry.get())

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password():
        """
        Save password to text file
        """
        pass_dict = {
            web_entry.get(): {
                'email': user_entry.get(),
                'password': password_entry.get()
            }
        }

        if _check_entries():
            messagebox.showerror(title='Empty Entry', message='Empty Fields cannot be saved')
        else:
            try:
                with open('./data/supersecret.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('./data/supersecret.json', 'w') as file:
                    json.dump(pass_dict, file, indent=3)
            else:
                data.update(pass_dict)
                with open('./data/supersecret.json', 'w') as file:
                    json.dump(data, file, indent=3)
            finally:
                _clear_entries()

    def _clear_entries():
        """
        Clear all entries in window
        """
        web_entry.delete(0, tkinter.END)
        user_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

    def _check_entries():
        """
        Checks if any entry fields are blank
        """
        if len(web_entry.get()) == 0:
            return True
        elif len(user_entry.get()) == 0:
            return True
        elif len(password_entry.get()) == 0:
            return True
    
    def search_password():
        """
        Search for a passwrod in the website entry
        """

        try:
            with open('./data/supersecret.json') as file:
                data = json.load(file)
        except KeyError:
            messagebox.showerror(title='Entry not found', message=f'No entry found for {web_entry.get()}')
        except FileNotFoundError:
            messagebox.showerror(title='Credential File Error', message='No password file found.\nPlease save a password to create a new file.')
        else:
            messagebox.showinfo(title='Credentials', message=f"Username: {data[web_entry.get()]['email']}\nPassword: {data[web_entry.get()]['password']}")

    # ---------------------------- UI SETUP ------------------------------- #
    window = tkinter.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
    logo = tkinter.PhotoImage(file='./images/logo.png')
    canvas.create_image(100, 100, image=logo)
    canvas.grid(column=1, row=0)

    website_label = tkinter.Label(text='Website:')
    website_label.grid(column=0, row=1)

    web_entry = tkinter.Entry(width=21)
    web_entry.focus()
    web_entry.grid(column=1, row=1, sticky='EW')

    username_label = tkinter.Label(text='Email/Username:')
    username_label.grid(column=0, row=2)

    user_entry = tkinter.Entry(width=35)
    user_entry.grid(column=1, row=2, columnspan=2, sticky='EW')

    password_label = tkinter.Label(text='Password:')
    password_label.grid(column=0, row=3)

    password_entry = tkinter.Entry(width=21)
    password_entry.grid(column=1, row=3, columnspan=1, sticky='EW')

    generate_pass = tkinter.Button(text='Generate Password', command=generate_password)
    generate_pass.grid(column=2, row=3)

    save_button = tkinter.Button(width=36, text='Add', command=save_password)
    save_button.grid(column=1, row=4, columnspan=2, sticky='EW')

    copy_button = tkinter.Button(text='Copy Password', command=copy_password)
    copy_button.grid(column=0, row=4)

    search_button = tkinter.Button(text='Search', command=search_password)
    search_button.grid(column=2, row=1, sticky='EW')

    window.mainloop()

if __name__ == '__main__':
    main()

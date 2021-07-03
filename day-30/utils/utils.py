def save_password():
    """
    Save password to text file
    """
    with open('./data/supersecret.txt', 'a') as file:
        file.write(f'{web_entry.get()} | {user_entry.get()} | {password_entry.get()}\n')
    _clear_entries()

def _clear_entries():
    """
    Clear all entries in window
    """
    web_entry.delete(0, END)
    user_entry.delete(0, END)
    password_entry.delete(0, END)
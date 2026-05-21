import random
import time
import openpyxl
from openpyxl import Workbook, load_workbook


def load_excel(apps, usernames, passwords): 
    '''loads current entries from excel file into the lists for apps etc
        args:
            apps (list): the list to fill with the saved app names
            username (list): the list to fill with saved usernames  
            passwords (list): list to fill with saved passwords
        returns:
            nothing: just fills the list with data from the excel sheet 
        '''
    book = load_workbook("Password Keeper.xlsx")
    sheet = book.active
    for row in sheet.iter_rows(min_row=2, values_only=True):    
        apps.append(row[0])
        usernames.append(row[1])
        passwords.append(row[2])

def add_entry(apps, usernames, passwords):
    '''adds a new entry to the lists and saves it to the excel file 
        args:
            apps (list): list of saved app names
            usernames (list): list of saved usernames
            passwords (list): list of saved passwords 
        returns: 
            nothing: just updates/adds to the lists and the excel sheet 
    '''
    App = input("Enter the app you want to create a account for: ")
    Username = input("Enter the username you want: ")
    Password = input("Enter the password you want: ")
    apps.append(App)
    usernames.append(Username)
    passwords.append(Password)
    book = load_workbook("Password Keeper.xlsx")
    sheet = book.active
    sheet.append([App, Username, Password])
    book.save("Password Keeper.xlsx")

def print_all(apps, usernames, passwords):
    '''prints every saved entry in the lists
        args: 
            apps (lists): list of saved app names 
            usernames (list): list of saved usernames 
            passwords (list): list of saved passwords
        returns: 
            nothing: prints all entries 
    '''
    for i in range(len(apps)): 
        print(apps[i], usernames[i], passwords[i])

def lookup_app(apps, usernames, passwords):
    '''searches for a specific app the user wants - prints its entry if it is found
        args: 
            apps (list): list of saved app names
            usernames (list): list of saved usernames
            passwords (list): list of saved passwords 
        returns: 
            i (int): index of the found entry
    '''
    wanted = input("What app account do you want to look for? ").lower().strip()
    
    for i in range(len(apps)):
        if apps[i].lower().strip() == wanted:
            print(f"App:{apps[i]}, Username:{usernames[i]}, Password:{passwords[i]}")      
            return i
    
    print("App not found")

def delete_app(apps, usernames, passwords):
    '''deletes an entry that the user wants - requires the user's confirmation, also updates the excel file with the change
        args: 
            apps (list): list of saved app names
            usernames (list): list of saved usernames 
            passwords (list): list of saved passwords
        returns: 
            nothing: removes the entry from the lists and the excel sheet 
    '''
    delete = input("What app account do you want to look for?" ).lower().strip()
    for i in range(len(apps)):
        if apps[i].lower().strip() == delete:
            print(f"App:{apps[i]}, Username:{usernames[i]}, Password:{passwords[i]}")
            confirm = input("Are you sure you want to delete this entry? Y/N ").upper().strip()
            if confirm == "Y":
                apps.pop(i)
                usernames.pop(i)
                passwords.pop(i)
                save_to_excel(apps, usernames, passwords)
                print("Entry deleted")
            elif confirm == "N":
                print("Good choice")
                return
            else: 
                print("Please enter Y or N")
            return
    
    print("App not found")

def change_entry(apps, usernames, passwords):
    '''lets the user edit a current entry and saves the changes to the excel file 
    args: 
        apps (list): list of saved app names
        usernames (list): list of saved usernames 
        passwords (list): list of saved passwords 
    returns: 
        nothing: updates the entry in the lists and the excel sheet 
    '''
    wanted = input("What app account do you want to change? ").lower().strip()
    for i in range(len(apps)):
        if apps[i].lower().strip() == wanted:
            print(f"App:{apps[i]}, Username:{usernames[i]}, Password:{passwords[i]}")
            apps[i] = input("New app name (press enter to keep current): ").strip() or apps[i]
            usernames[i] = input("New username (press enter to keep current): ").strip() or usernames[i]
            passwords[i] = input("New password (press enter to keep current): ").strip() or passwords[i]
            save_to_excel(apps, usernames, passwords)
            print("Entry updated")
            return
    print("App not found")

def password_maker(number):
    '''creates a random password for user 
    args:
        number(int): length user wants for password 
    returns: 
        new_character (str): new created password with the length the user wants 
    '''
    character_list = [ 
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e",
    "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
    "K", "k", "L", "l", "M", "m", "N", "n", "O", "o",
    "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
    "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y",
    "Z", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "[", "]", "{", "}", "|",
    ";", ":", "'", ",", ".", "<", ">", "/", "?",
    "`", "~"] 

    new_character = ""

    for n in range(number): 
        new_character += random.choice(character_list)
    return new_character   

def entry_password(master):
    '''asks for the master password and gives the user 3 tries to enter it correctly 
        args: 
        master (str): the correct master password to check for 
        returns: 
        True (bool): if access granted 
        False (bool): if all attempts fail
    '''
    attempts = 3
    for i in range(attempts):
        entered = input("Enter master password: ").strip()
        if entered == master: 
            print("Access granted")
            return True
        attempts -= 1
        if attempts > 0: 
            print(f"Incorrect. You have {attempts} attempts left")
        else: 
            print("Too many failed attempts. Exiting")
    return False

def check_secure(apps, passwords):
    '''checks how secure a saved password is based on set conditions like types of character and length
    args:
        apps (list): list of saved app names 
        passwords (list): list of saved passwords
    returns: 
        nothing: prints strength rating to user 
    '''
    wanted = input("What app's password do you want to check? (enter the app) ").lower().strip()
    found = False
    for i in range(len(apps)):
        if apps[i].lower().strip() == wanted:
            found = True
            print(f"Password:{passwords[i]}")
            A = input("Is this the password you want to check? ").lower().strip()
            if A == "yes":
                strength = 0 
                has_upper = False
                has_lower = False
                is_digit = False 
                special_character = False
                for character in passwords[i]:
                    if character.isupper():
                        has_upper = True
                    elif character.islower():
                        has_lower = True
                    elif character.isdigit(): 
                        is_digit = True 
                    else: 
                        special_character = True
                if has_upper == True:
                    strength += 1 
                if has_lower == True: 
                    strength += 1 
                if is_digit == True: 
                    strength += 1 
                if special_character == True:
                    strength += 1
                if len(passwords[i]) >= 8: 
                    strength += 1 
                if strength <= 2: 
                    print("Weak Password, would recommend changing")
                elif strength <= 4: 
                    print("Medium strength password, you can make a better one or keep this one")
                elif strength >= 5: 
                    print("Strong password, would keep this")
            elif A == "no": 
                print("Ok returning you to the menu")
            else: 
                print("Please enter only Yes or No")
            return

    if found == False: 
        print("App not found")                
    
def save_to_excel(apps, usernames, passwords):
    """rewrites/updates the excel sheet based on the current lists
    args: 
        apps (list): list of saved app names 
        usernames (list): list of saved usernames
        passwords (list): list of saved passwords
    returns:
        nothing: updates password.keeper.xlsx with current data 
    """
    book = load_workbook("Password Keeper.xlsx")
    sheet = book.active 
    sheet.delete_rows(2, sheet.max_row)
    for i in range(len(apps)):
        sheet.append([apps[i], usernames[i], passwords[i]])
    book.save("Password Keeper.xlsx")

def main():
    '''runs the whole program, loads the saved data from the excel sheet, checks master password and shows menu options
        args: 
            none
        returns:
            nothing: runs the main program until the user chooses to quit 
    '''
    time.sleep(1.25)
    apps = []
    usernames = []
    passwords = []
    master = "password123"

    load_excel(apps, usernames, passwords)

    if not entry_password(master):
        return
    
    while True:
        print(''' 
        1 = add entry 
        2 = print all entries
        3 = look up a certain app 
        4 = Have a password be made for you
        5 = delete an entry 
        6 = change an entry 
        7 = Check how secure a password is 
        8 = quit ''')
        menu = input("Choose a number for the action you want: ")
        if menu == "1": 
            add_entry(apps, usernames, passwords)
        elif menu == "2": 
            print_all(apps, usernames, passwords)
        elif menu == "3": 
            lookup_app(apps, usernames, passwords)
        elif menu == "4":
            number = int(input("Please enter the number amount of characters (in number form) you want in your password "))
            print(password_maker(number))
            print("Here is your new password. You may copy it to enter as a new password in an app")
        elif menu == "5":
            delete_app(apps, usernames, passwords)
        elif menu == "6":
            change_entry(apps, usernames, passwords)
        elif menu == "7":
            check_secure(apps, passwords)
        elif menu == "8":
            print("Goodbye")
            break
        else: 
            print("Not a valid choice, try again")

main()
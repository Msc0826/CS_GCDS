
"""
Name: Mason Coleman
Description: Asks the user for their name and gives them a menu of things
             to do with it, like reversing it, counting the vowels, or
             pulling out the first and last name.
Bugs: If you don't type a middle name, option 6 just prints a blank line.
Bonus: Menu, initials, title check, scramble
Date: 9/24/26
Log: Initial Creation: 9/10/26
     9/17/26 Created main, started display first/last name functions
     9/23/26 Finished hyphen return, upper and lowercase converting
     9/24/26 Finished palindrome checker, middle name, scramble, titles
     9/27/26 Finished intials
     9/30/26 Added full documentation to all functions
"""
 
import random
 
def reverse_display(chars):
    """Reverse a name.
    Args:
        chars: a list of single characters, or a string
    Returns:
        str: the characters in reverse order
    """
    result = ""
    i = len(chars) - 1

    while i >= 0:
        result = result + chars[i]
        i = i - 1
    return result
 
 
def count_vowels(chars):
    """Count the vowels in a name.
    Args:
        chars: a list of single characters, or a string
    Returns:
        int: how many vowels were found
    """
    count = 0
 
    for i in range(len(chars)):
        if chars[i] in "AEIOUaeiou":
            count = count + 1
    return count
 
 
def consonant_frequency(chars):
    """Count the consonants in a name.
    Args:
        chars: a list of single characters, or a string
    Returns:
        int: how many consonants were found
    """
    count = 0

    for i in range(len(chars)):
        if chars[i] in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
            count = count + 1
    return count
 
 
def display_firstname(name):
    """Return the first name.
    Args:
        name (str): the full name
    Returns:
        str: the first word of the name
    """
    parts = []
 
    parts = name.split()
    return parts[0]
 
 
def display_lastname(name):
    """Return the last name.
    Args:
        name (str): the full name
    Returns:
        str: the final word of the name
    """
    parts = []
 
    parts = name.split()
    return parts[len(parts) - 1]
 
 
def display_middlename(name):
    """Return every middle name.
    Args:
        name (str): the full name
    Returns:
        str: the middle name(s), or an empty string if there are none
    """
    parts = []
    result = ""
 
    parts = name.split()
    for i in range(1, len(parts) - 1):
        result = result + parts[i] + " "
    return result
 
 
def hyphen_return(name):
    """Check whether the last name contains a hyphen.
    Args:
        name (str): the full name
    Returns:
        bool: True if the last name is hyphenated, otherwise False
    """
    last = ""
 
    last = display_lastname(name)
    for i in range(len(last)):
        if last[i] == "-":
            return True
    return False
 
 
def convert_lowercase(chars):
    """Convert a name to lowercase without using string methods.
    Args:
        chars: a list of single characters, or a string
    Returns:
        str: the lowercase version of the name
    """
    new_name = ""
 
    for i in range(len(chars)):
        if chars[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_name = new_name + chr(ord(chars[i]) + 32)
        else:
            new_name = new_name + chars[i]
    return new_name
 
 
def convert_uppercase(chars):
    """Convert a name to uppercase without using string methods.
    Args:
        chars: a list of single characters, or a string
    Returns:
        str: the uppercase version of the name
    """
    new_name = ""
 
    for i in range(len(chars)):
        if chars[i] in "abcdefghijklmnopqrstuvwxyz":
            new_name = new_name + chr(ord(chars[i]) - 32)
        else:
            new_name = new_name + chars[i]
    return new_name
 
 
def palindrome_checker(name):
    """Check whether the first name reads the same backward.
    Args:
        name (str): the full name
    Returns:
        bool: True if the first name is a palindrome, otherwise False
    """
    first = ""
    lower = ""
 
    first = display_firstname(name)
    lower = convert_lowercase(first)
    if lower == reverse_display(lower):
        return True
    else:
        return False
 
 
def mix_up(chars):
    """Scramble the letters of a name into a random order.
    Args:
        chars: a list of single characters
    Returns:
        str: the same characters in a random order
    """
    mixed = []
    result = ""
    mixed = list(chars)
    random.shuffle(mixed)
    for i in range(len(mixed)):
        result = result + mixed[i]
    return result
 
 
def make_initials(name):
    """Build the initials of a name.
    Args:
        name (str): the full name
    Returns:
        str: the initials, such as M.R.C.
    """
    parts = []
    result = ""
 
    parts = name.split()
    for i in range(len(parts)):
        result = result + parts[i][0] + "."
    return result
 
 
def has_title(name):
    """Check whether a name contains a title or distinction.
    Args:
        name (str): the full name
    Returns:
        bool: True if a title is found, otherwise False
    """
    parts = []
 
    parts = name.split()
    for i in range(len(parts)):
        if parts[i] in ("Dr.", "Dr", "Sir", "Esq.", "Esq", "Ph.D.", "Ph.D",
                        "Ph.d", "PhD", "Mr.", "Mr", "Mrs.", "Mrs", "Ms.", "Ms"):
            return True
    return False
 
 
def main():
    """Run the program.
    Asks the user for a full name, then repeatedly displays a menu and
    calls the matching function until the user chooses to quit.
    Args:
        None
    Returns:
        None
    """
    name = ""
    chars = []
    name = input("Enter your full name (including middle): ")
    chars = list(name)
 

    while True:
        print('''
        1) Reverse name
        2) Count vowels in name
        3) Count the amount of consonants
        4) Display your first name
        5) Display your last name
        6) Display your middle name
        7) Check if your last name has a hyphen
        8) Convert your name to lowercase
        9) Convert your name to uppercase
        10) Check if your first name is a palindrome
        11) Scramble your name
        12) Make your initials
        13) Check if your name has a title
        14) Quit
        ''')
 
        menu = input("Choose a number for the option you want: ")
        if menu == "1":
            print("Reversed:", reverse_display(chars))
        elif menu == "2":
            print("Vowels:", count_vowels(chars))
        elif menu == "3":
            print("Consonants:", consonant_frequency(chars))
        elif menu == "4":
            print("First name:", display_firstname(name))
        elif menu == "5":
            print("Last name:", display_lastname(name))
        elif menu == "6":
            print("Middle name(s):", display_middlename(name))
        elif menu == "7":
            print("Hyphenated last name:", hyphen_return(name))
        elif menu == "8":
            print("Lowercase:", convert_lowercase(chars))
        elif menu == "9":
            print("Uppercase:", convert_uppercase(chars))
        elif menu == "10":
            print("Palindrome:", palindrome_checker(name))
        elif menu == "11":
            print("Scrambled:", mix_up(chars))
        elif menu == "12":
            print("Initials:", make_initials(name))
        elif menu == "13":
            print("Has a title:", has_title(name))
        elif menu == "14":
            print("Goodbye")
            break
        else:
            print("Not a valid choice")
 
 
main()
 

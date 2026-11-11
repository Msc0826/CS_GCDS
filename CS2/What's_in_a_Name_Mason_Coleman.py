
"""
Name: Mason Coleman
Description: Asks the user for their name and gives them a menu of things to do with it, like reversing it, counting the vowels, or pulling out the first and last name.
Bugs: Have to run without debugging in order for it to play
Bonus: Menu, initials, title check, scramble
Date: 9/24/26
Log: Initial Creation: 9/10/26
     9/17/26 Created main, started display first/last name functions
     9/23/26 Finished hyphen return, upper and lowercase converting
     9/24/26 Finished palindrome checker, middle name, scramble, titles
     9/27/26 Finished intials
     9/30/26 Added full documentation to all functions
     11/11/26 Release v1.1 Added documentation for single lines of code 
"""
 
import random
 
def reverse_display(chars):
    """
    Description: Reverse a name 
    Args:
        chars: a list of single characters, or a string
    Returns:
        str: the characters in reverse order
    """
    result = ""    
    i = len(chars) - 1   # start at the last index (0)

    while i >= 0:
        result = result + chars[i] #add the current charcter to the new name 
        i = i - 1
    return result
 
 
def count_vowels(chars):
    """
    Description: Count the vowels in a name.
    Args:
        chars: a list of single characters, or a string
    Returns:
        int: how many vowels were found
    """
    count = 0
 
    for i in range(len(chars)): #cycle through every character in the string 
        if chars[i] in "AEIOUaeiou":  #if a character is a vowel
            count = count + 1  #add to count if there is a vowel
    return count
 
 
def consonant_frequency(chars):
    """
    Description: Count the consonants in a name.
    Args:
        chars: a list of single characters, or a string
    Returns:
        int: how many consonants were found
    """
    count = 0 

    for i in range(len(chars)):   #cycle through every character in the string
        if chars[i] in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":  #if a character is a consonant 
            count = count + 1   #add one to count 
    return count
 
 
def display_firstname(name):
    """
    Description: Return the first name.
    Args:
        name (str): the full name
    Returns:
        str: the first word of the name
    """
    parts = []
 
    parts = name.split() #split the given full name into a list 
    return parts[0]   #return the first word in the list 
 
 
def display_lastname(name):
    """
    Description: Return the last name.
    Args:
        name (str): the full name
    Returns:
        str: the final word of the name
    """
    parts = [] 
 
    parts = name.split()   #split the given full name into a list 
    return parts[len(parts) - 1] #return the last word in the list 
 
 
def display_middlename(name):
    """
    Description: Return every middle name.
    Args:
        name (str): the full name
    Returns:
        str: the middle name(s), or an empty string if there are none
    """
    parts = []
    result = ""
 
    parts = name.split() 
    for i in range(1, len(parts) - 1):  #skip the first and last word of the list 
        result = result + parts[i] + " " #each middle word plus a space 
        return result   #return middle words 
 
 
def hyphen_return(name):
    """
    Description: Check whether the last name contains a hyphen.
    Args:
        name (str): the full name
    Returns:
        bool: True if the last name is hyphenated, otherwise False
    """
    last = ""
 
    last = display_lastname(name) #use last name function to get the last name 
    for i in range(len(last)): #cycle through every character in the last name 
        if last[i] == "-":  #if a character is a hyphen 
            return True #return that there is a hyphen
    return False #if not return false 
 
 
def convert_lowercase(chars):
    """
    Description: Convert a name to lowercase without using string methods.
    Args:
        chars: a list of single characters, or a string
    Returns:
        str: the lowercase version of the name
    """
    new_name = ""
 
    for i in range(len(chars)):
        if chars[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  #change only the uppercase letters 
            new_name = new_name + chr(ord(chars[i]) + 32) #ord gives the number that matches the letter, adding 32 changes it to lowercase, and chr turns it back to a letter 
        else:
            new_name = new_name + chars[i] #if not uppercase, leave alone 
    return new_name
 
 
def convert_uppercase(chars):
    """
    Description: Convert a name to uppercase without using string methods.
    Args:
        chars: a list of single characters, or a string
    Returns:
        str: the uppercase version of the name
    """
    new_name = ""
  
    for i in range(len(chars)):
        if chars[i] in "abcdefghijklmnopqrstuvwxyz": #change only lowercase letters
            new_name = new_name + chr(ord(chars[i]) - 32)  #subtracting 32 turns the letter to uppercase 
        else:
            new_name = new_name + chars[i]
    return new_name
 
 
def palindrome_checker(name):
    """
    Description: Check whether the first name reads the same backward.
    Args:
        name (str): the full name
    Returns:
        bool: True if the first name is a palindrome, otherwise False
    """
    first = ""
    lower = ""
 
    first = display_firstname(name) #gets first name 
    lower = convert_lowercase(first)   #makes the first name fully lowercase 
    if lower == reverse_display(lower):  #if the first name is the same as a the reversed name 
        return True  #return that it is a palindrome 
    else:
        return False
 
 
def mix_up(chars):
    """
    Description: Scramble the letters of a name into a random order.
    Args:
        chars: a list of single characters
    Returns:
        str: the same characters in a random order
    """
    mixed = []
    result = ""
    mixed = list(chars) #turns all letters/characters in the string into seperate characters in a list 
    random.shuffle(mixed) #randomly reorders the list 
    for i in range(len(mixed)):
        result = result + mixed[i]  #rebuild the shuffled list into a string 
    return result
 
 
def make_initials(name):
    """
    Description: Build the initials of a name.
    Args:
        name (str): the full name
    Returns:
        str: the initials, such as M.S.C.
    """
    parts = []
    result = ""
 
    parts = name.split() 
    for i in range(len(parts)): 
        result = result + parts[i][0] + "." #takes the first letter of each word in the list and adds a period 
    return result
 
 
def has_title(name):
    """
    Description: Check whether a name contains a title or distinction.
    Args:
        name (str): the full name
    Returns:
        bool: True if a title is found, otherwise False
    """
    parts = []
 
    parts = name.split()
    for i in range(len(parts)):
        if parts[i] in ("Dr.", "Dr", "Sir", "Esq.", "Esq", "Ph.D.", "Ph.D",    #checks if each word in the list has a title 
                        "Ph.d", "PhD", "Mr.", "Mr", "Mrs.", "Mrs", "Ms.", "Ms"): 
            return True
    return False
 
 
def main():
    """
    Description: Run the program.
    Asks the user for a full name, then repeatedly displays a menu and
    calls the matching function until the user chooses to quit.
    Args:
        None
    Returns:
        None
    """
    name = ""
    chars = []  #empty list where list of single characters will be added 
    name = input("Enter your full name (including middle): ")
    chars = list(name) #breaks the name into single characters and adds it to a list 
 

    while True:  #while program is running 
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

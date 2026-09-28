"""
Name: Mason Coleman
Description: Name function project (will update)
Bugs: None Known
Date: 9/17/26
Log: Initial Creation: 9/10/26
9/24/26 Finished palinadrome checker, 

"""

def reverse_display(chars):
  result = ""
  i = len(chars) -1
  while i >= 0:
        result = result + chars[i]
        i = i - 1
  return result

def count_vowels(name):
    count = 0 
    for i in range(len(name)):
        if name[i] in ("AEIOUaeiou"):
            count = count + 1
    return count

def consonant_frequency(name):
    count = 0 
    for i in range(len(name)):
            if name[i] in ("BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"):
                count = count + 1
    return count

def display_firstname(name):
    parts = []
    parts = name.split()
    return (parts[0])
        
def display_lastname(name):
    parts = []
    parts = name.split()
    return parts[len(parts) - 1]

def display_middlename(name):
    parts = []
    result = ""

    parts = name.split()
    for i in range(1, len(parts) - 1):
        result = result + parts[i] + " "
    return result

def hypen_return(name):
    for i in range(len(name)):
        if name[i] in ("-"):
            return True 
    return False

def convert_lowercase(chars):
    new_name = ""
    for i in range(len(chars)):
        if chars[i] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            new_name = new_name + chr(ord(chars[i]) + 32 )
        else:
            new_name = new_name + chars[i]
    return(new_name)
            


def convert_uppercase(chars):
    new_name = ""
    for i in range(len(chars)):
        if chars[i] in ("abcdefghijklmnopqrstuvwxyz"):
            new_name = new_name + chr(ord(chars[i]) - 32 )
        else:
            new_name = new_name + chars[i]
    return(new_name)
    

def palindrome_checker(name):
    first = ""
    lower = ""

    first = display_firstname(name)
    lower = convert_lowercase(first)
    if lower == reverse_display(lower):
        return True
    else:
        return False

def initial_creator():
    parts = []
    result = ""
    


def main():
    name = ""
    chars = []
    name = input("Enter your full name (including middle): ")
    chars = list(name)
    while True:
        print('''
        1) Reverse name
        2) Count vowels in name
        3) Count the amount of consonant
        4) Display your first name
        5) Display your last name
        6) Display your middle name
        7) Check if your name has a hypen
        8) Convert your name to lowercase
        9) Convert your name to uppercase
        10) Check if your first name is a palindrome
        11) Quit
        ''')

        menu = input("Choose a number for the option you want: ")
        if menu == "1":
            print(reverse_display(chars))
        elif menu == "2": 
            print(count_vowels(name))
        elif menu == "3": 
           print (consonant_frequency(name))
        elif menu == "4":
            print(display_firstname(name))
        elif menu == "5":
            print(display_lastname(name))
        elif menu == "6":
            print(display_middlename(name))
        elif menu == "7":
            print(hypen_return(name))
        elif menu == "8":
            print(convert_lowercase(chars))
        elif menu == "9":
            print(convert_uppercase(chars))
        elif menu == "10":
            print(palindrome_checker(name))
        elif menu == "11":
            print("Goodbye")
            break
        else: 
            print("Not a valid choice")

main()

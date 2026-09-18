"""
Name: Mason Coleman
Description: Name function project (will update)
Bugs: None Known
Date: 9/17/26
Log: Initial Creation: 9/10/26
9/17/26 created main, finished display first/last name and consonant frequency functions

"""




def reverse_display(chars):
  result = ""
  i = 0
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
            if name[i] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
                count = count + 1
    return count

def display_firstname(name):
    parts = []
    parts = name.split()
    return (parts[0])
        
def display_lastname(name):
    parts = []
    parts = name.split()
    return (parts[2])

def display_middlename(name):
    parts = []
    parts = name.split()
    return (parts[1])

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
        7) Quit
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
            print("Goodbye")
            break
        else: 
            print("Not a valid choice")

main()
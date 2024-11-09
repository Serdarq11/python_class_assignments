""""
Implementing a simple English/Turkish dictionary. Please copy and paste this code to your Python file to start with:

englishList = ["car"]
spanishList = ["coche"]

while ...:
    print('''
        1) Add item to the dictionary
        2) Translate (English to Spanish) 
        3) Quit
    ''')

    #Get user input
When adding an item, the program should ask the user to enter the English word and the corresponding Spanish word. 
The English word should be added to the englishList and the Spanish word should be added to spanishList.

When translating, the program should ask the user to enter the English word, and then it should print the 
Spanish translation. We assume that the user enters an existing word in the dictionary.

The program should continue to run until the user chooses the 3rd option: Quit. 

"""

englishList = ["car"]
turkishList = ["araba"]

while True:
    print('''
        1) Add item to the dictionary
        2) Translate (English to Turkish)
        3) Quit
    ''')

    choice = input("Choose an option: ")

    if choice == '1':
        english_word = input("Enter the English word: ")
        turkish_word = input("Enter the Turkish word: ")
        englishList.append(english_word)
        turkishList.append(turkish_word)
        print(f"Added '{english_word}' as '{turkish_word}' to the dictionary.")

    elif choice == '2':
        english_word = input("Enter the English word to translate: ")
        if english_word in englishList:
            index = englishList.index(english_word)
            print(f"The Turkish translation for '{english_word}' is '{turkishList[index]}'.")
        else:
            print("The word is not in the dictionary.")

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

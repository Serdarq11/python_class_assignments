

# Define the lists for English and Turkish words
englishList = ["car"]
turkishList = ["araba"]


def add_item():
    while True:
        english_word = input("Enter an English word: ")
        if english_word in englishList:
            print("The word already exists. Please try again.")
        else:
            turkish_word = input("Enter the Turkish translation: ")
            englishList.append(english_word)
            turkishList.append(turkish_word)
            print("The word added successfully.")
            break

def translate_english_to_turkish():
    while True:
        english_word = input("Enter an English word to translate: ")
        if english_word in englishList:
            index = englishList.index(english_word)
            turkish_word = turkishList[index]
            print(f"Turkish translation is: {turkish_word}")
            break
        else:
            print("The word is not found. Please try again with another word.")

def translate_turkish_to_english():
    while True:
        turkish_word = input("Enter a Turkish word to translate: ")
        if turkish_word in turkishList:
            index = turkishList.index(turkish_word)
            english_word = englishList[index]
            print(f"English translation is: {english_word}")
            break
        else:
            print("The word is not found. Please try again with another word.")

def print_dictionary():
    print("English to Turkish Dictionary:")
    for eng, tur in zip(englishList, turkishList):
        print(f"{eng} -> {tur}")

def delete_item():
    word = input("Enter the English word you want to delete: ")
    if word in englishList:
        index = englishList.index(word)
        del englishList[index]
        del turkishList[index]
        print(f"Word '{word}' has been deleted.")
    else:
        print("The word is not found.")

while True:
    print('''
        1) Add item to the dictionary
        2) Translate from English to Turkish
        3) Translate from Turkish to English
        4) Print the dictionary
        5) Delete an item
        6) Quit
    ''')

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        translate_english_to_turkish()
    elif choice == "3":
        translate_turkish_to_english()
    elif choice == "4":
        print_dictionary()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



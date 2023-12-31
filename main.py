''' Hiral Shukla '''


def encoder(original):
    new_original = ""
    for i in range(0, len(original)):
        new_original += str((int(original[i]) + 3) % 10)
    return new_original



def menu_print():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

''' Rosalinda Phipps '''
def decoder(password):
    new_password = ""
    for i in range(0, len(original)):
        new_password += str((int(original[i]) + 7) % 10)
    return new_password




if __name__ == "__main__":
    condition = True

    while condition == True:
        menu_print()

        menu_selection = input("Please enter an option: ")

        if menu_selection == "1":
            password = input("Please enter your password: ")
            print("Your password has been encoded and stored!")

        if menu_selection == "2":
            original = password
            password = encoder(original)
            decoded_password = decoder(password)
            print(f"The encoded password is {password}, and the original password is {decoded_password}.")

        if menu_selection == "3":
            break







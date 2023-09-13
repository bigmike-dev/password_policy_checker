from forbidden_passwords import forbidden_passwords


def password_checker():
    """Creating a password checker for adherence"""

    print("\nBelow is a password checker to verify if your password adheres to the company's policy.\n"
          "(Hint: do not use common passwords or anything easily identifiable.")

    while True:

        users_password = input("\nPlease enter desired password: ")

        # Checks if user's password is in commonly used password list
        if users_password in forbidden_passwords:
            print("Unable to use a common password. Please try again.")

        # Fun little easter egg
        elif users_password == "12345":
            print("\n12345? That's the kind of thing an idiot would have on his luggage! - Dark Helmet, Spaceballs")

        # Checks the user's password for adherence to company policy
        elif(
            len(users_password) >= 15 and
            any(char.isupper() for char in users_password) and
            any(char.islower() for char in users_password) and
            any(char.isdigit() for char in users_password) and
            any(char in "!@#$%&*()" for char in users_password)
        ):
            print(f"\nUser's password is: Acceptable.")
            return True

        # Rejects the user's unacceptable password
        else:
            print("\nUser's password is: Unacceptable. Please try again. ")


if __name__ == "__main__":
    password_checker()

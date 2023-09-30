from Password import PasswordGenerator
import time
from colorama import Fore, Style, init


init(autoreset=True)


def main():
    print(Fore.YELLOW + "Welcome to the Password Generator!" + Style.RESET_ALL)
    time.sleep(0.5)

    while True:
        try:
            print(Fore.BLUE + "\nEnter your password preferences:" + Style.RESET_ALL)
            password_length = int(input("Enter the length of password: "))
            time.sleep(0.2)
            if input("Include uppercase letters? (yes/no): ").lower() != 'yes':
                include_uppercase = False
            else:
                include_uppercase = True
            time.sleep(0.2)
            if input("Include lowercase letters? (yes/no): ").lower() != 'yes':
                include_lowercase = False
            else:
                include_lowercase = True
            time.sleep(0.2)
            if input("Include numbers? (yes/no): ").lower() != 'yes':
                include_numbers = False
            else:
                include_numbers = True
            time.sleep(0.2)
            if input("Include special characters? (yes/no): ").lower() != 'yes':
                include_special = False
            else:
                include_special = True
            time.sleep(0.2)

            password_gen = PasswordGenerator(
                length=password_length,
                uppercase=include_uppercase,
                lowercase=include_lowercase,
                numbers=include_numbers,
                special_characters=include_special
            )

            print("Do you want to add specific characters to be repeated more than once.")
            is_repeat = input("Enter yes/no: ").lower()
            if is_repeat == 'yes':
                repeat_chars = input("Specify characters to repeat and their counts (e.g., $:2 &:3): ")
                repeat_dict = {}
                items = repeat_chars.split()
                for item in items:
                    char, count = item.split(':')
                    char = char.strip()
                    count = int(count)
                    repeat_dict[char] = count
                password_gen.repeated_characters(repeat_dict)

            time.sleep(0.2)

            password = password_gen.generate()
            print(Fore.GREEN + f"Generated Password: {password}" + Style.RESET_ALL)

        except ValueError as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

        another = input("\nGenerate another password? (yes/no): ").lower()
        if another != 'yes':
            print(Fore.CYAN + "Goodbye!" + Style.RESET_ALL)
            exit(1)


if __name__ == "__main__":
    main()

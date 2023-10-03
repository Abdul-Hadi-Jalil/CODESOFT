from colorama import Fore, Style
from contact_book import ContactBook, Contact


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. View Contacts")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                name = input("Enter name: ")
                phone_no = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                contact = Contact(name, phone_no, email, address)
                contact_book.add_contact(contact)
                print(Fore.GREEN + "Contact added successfully." + Style.RESET_ALL)
            except KeyboardInterrupt:
                print(Fore.RED + "\nOperation canceled by user." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

        elif choice == '2':
            try:
                print("Enter the details of the contact to search it.")
                name = input("Enter name (leave empty for any): ")
                phone_no = input("Enter phone number (leave empty for any): ")
                email = input("Enter email (leave empty for any): ")
                address = input("Enter address (leave empty for any): ")
                results = contact_book.search_contact(name=name, phone_no=phone_no, email=email, address=address)

                if results:
                    print("Search results:")
                    for contact in results:
                        print(contact)
                else:
                    print("No matching contacts found.")

            except KeyboardInterrupt:
                print(Fore.RED + "\nOperation canceled by user." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

        elif choice == '3':
            try:
                print("Enter the details of the contact to delete it.")
                name = input("Enter name (leave empty for any): ")
                phone_no = input("Enter phone number (leave empty for any): ")
                email = input("Enter email (leave empty for any): ")
                address = input("Enter address (leave empty for any): ")

                if contact_book.delete_contact(name=name, phone_no=phone_no, email=email, address=address):
                    print(Fore.GREEN + "Contacts deleted successfully." + Style.RESET_ALL)
                else:
                    print("No matching contacts found.")
            except KeyboardInterrupt:
                print(Fore.RED + "\nOperation canceled by user." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

        elif choice == '4':
            try:
                old_name = input("Enter the name of the contact to update: ")
                old_phone_no = input("Enter the old phone number: ")
                old_email = input("Enter the old email (leave empty if none): ")
                old_address = input("Enter the old address (leave empty if none): ")

                matching_contacts = contact_book.search_contact(name=old_name, phone_no=old_phone_no,
                                                                email=old_email, address=old_address)

                if matching_contacts:
                    name = input("Enter new name: ")
                    phone_no = input("Enter new phone number: ")
                    email = input("Enter new email: ")
                    address = input("Enter new address: ")
                    new_contact = Contact(name, phone_no, email, address)

                    if contact_book.update_contact(name=old_name, phone_no=old_phone_no,
                                                   email=old_email, address=old_address, new_contact=new_contact):
                        print(Fore.GREEN + "Contact updated successfully." + Style.RESET_ALL)
                    else:
                        print("Contact not found.")
                else:
                    print("Contact not found.")
            except KeyboardInterrupt:
                print(Fore.RED + "\nOperation canceled by the user." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

        elif choice == '5':
            contact_book.view_contacts()

        elif choice == '6':
            print(Fore.LIGHTCYAN_EX + "Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    main()

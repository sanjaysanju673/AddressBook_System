'''
    @Author: V Sanjay Kumar
    @Date: 08-09-2024
    @Last Modified by: V Sanjay Kumar
    @Last Modified: 08-09-2024
    @Title : UC-6 Refactor to add multiple Address Book to the System. Each Address Book has a unique Name

'''
class Contact:
    # Represents a contact in the address book.
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city 
        self.state = state 
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        """
        Definition: Display the details
        parameter: None
        Return: Returns a formatted string of the contact's details.
        """
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zip Code: {self.zip_code}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Email: {self.email}\n")

def check_integer_input(prompt):
    """
        Definition: Prompts the user for an integer input 
        parameter: None
        Return: returns the integer value.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}

    def add_or_update_contact(self, contact):
        """
        Definition: Adds or updates a contact in the address book.
        If the contact with the given first name exists, update the contact details. Otherwise, add a new contact.
        parameter: contact (Contact) - The contact object with details.
        Return: None
        """
        if contact.first_name in self.contacts:
            print(f"Contact with first name '{contact.first_name}' already exists. Updating contact.")
        else:
            print(f"Adding new contact for '{contact.first_name}'.")

        self.contacts[contact.first_name] = contact
        print("Contact saved successfully.")


    def display_all_contacts(self):
        """
        Definition: Displays all contacts in the address book.
        parameter: None
        Return: None
        """
        if not self.contacts:
            print("No contacts in address book.")
        else:
            for contact in self.contacts.values():
                print('-'*30)
                print(contact.display_contact())
          
                
    def edit_contact(self, first_name):
        """
        Definition: Edits an existing contact in the address book.
        parameter: first_name (str) - The first name of the contact to edit.
        Return: None
        """
        if first_name in self.contacts:
            contact = self.contacts[first_name]
            print("Enter new details (leave blank to keep current value):")
            print("which details Do you want to update(first_name,last_name,address,city,state,zip_code,phone_number,email):")
            choice =input()
            match choice:
                case "first_name":
                    contact.first_name = input(f"First Name [{contact.first_name}]: ") or contact.first_name
                case "last_name":
                    contact.last_name = input(f"Last Name [{contact.last_name}]: ") or contact.last_name
                case "address":
                    contact.address = input(f"Address [{contact.address}]: ") or contact.address
                case "city":
                    contact.city = input(f"City [{contact.city}]: ") or contact.city
                case "state":
                    contact.state = input(f"State [{contact.state}]: ") or contact.state
                case "zip_code":
                    contact.zip_code = check_integer_input(f"ZIP Code [{contact.zip_code}]: ") or contact.zip_code
                case "phone number":
                    contact.phone_number = check_integer_input(f"Phone Number [{contact.phone_number}]: ") or contact.phone_number
                case "email":
                    contact.email = input(f"Email [{contact.email}]: ") or contact.email
                case default:
                    print("invalid choice")
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
            
    def delete_contact(self, first_name):
        """
        Definition: Deletes an existing contact in the address book.
        parameter: first_name (str) - The first name of the contact to delete.
        Return: None
        """
        if first_name in self.contacts:
            del self.contacts[first_name]
            print(f"Contact '{first_name}' deleted successfully.")
        else:
            print("Contact not found.")

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name in self.address_books:
            print(f"Address book with name '{name}' already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            print(f"Address book '{name}' created successfully.")

    def get_address_book(self, name):
        return self.address_books.get(name)

    def display_all_address_books(self):
        if not self.address_books:
            print("No address books available.")
        else:
            print("Available Address Books:")
            for name in self.address_books:
                print(f"- {name}")



def main_menu():
    system = AddressBookSystem()
    while True:
        print("\nAddress Book System Menu:")
        print("1. Create a new Address Book")
        print("2. Select an Address Book")
        print("3. Display all Address Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name for the new Address Book: ")
            system.add_address_book(name)

        elif choice == '2':
            name = input("Enter the name of the Address Book to select: ")
            address_book = system.get_address_book(name)
            
            if address_book:
                while True:
                    print(f"\nAddress Book: {name} - Menu:")
                    print("1. Add or Update Contact")
                    print("2. Display All Contacts")
                    print("3. Edit Contact")
                    print("4. Delete Contact")
                    print("5. Return to Main Menu")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        print("Enter contact details:")
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        address = input("Address: ")
                        city = input("City: ")
                        state = input("State: ")
                        zip_code = check_integer_input("ZIP Code: ")
                        phone_number = check_integer_input("Phone Number: ")
                        email = input("Email: ")

                        contact = Contact(
                            first_name=first_name,
                            last_name=last_name,
                            address=address,
                            city=city,
                            state=state,
                            zip_code=zip_code,
                            phone_number=phone_number,
                            email=email
                        )
                        address_book.add_or_update_contact(contact)

                    elif sub_choice == '2':
                        address_book.display_all_contacts()

                    elif sub_choice == '3':
                        first_name = input("Enter the first name of the contact to edit: ")
                        address_book.edit_contact(first_name)

                    elif sub_choice == '4':
                        first_name = input("Enter the first name of the contact to delete: ")
                        address_book.delete_contact(first_name)

                    elif sub_choice == '5':
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print(f"Address book '{name}' not found.")
        
        elif choice == '3':
            system.display_all_address_books()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
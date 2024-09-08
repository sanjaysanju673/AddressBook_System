'''
    @Author:V Sanjay kumar
    @Date: 08-09-2024
    @Last Modified by:V Sanjay Kumar
    @Last Modified: 08-09-2024
    @Title : UC-2 Ability to update a Contacts in Address Book with first and last names, address,city, state, zip, phone number and email. by using first name

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

    def add_contact(self, contact):
        """
        Definition: Adds a new contact to the address book.
        parameter: contact details
        Return: None
        """
        self.contacts[contact.first_name] = contact
        print("Contact added successfully.")

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
            contact.first_name = input(f"First Name [{contact.first_name}]: ") or contact.first_name
            contact.last_name = input(f"Last Name [{contact.last_name}]: ") or contact.last_name
            contact.address = input(f"Address [{contact.address}]: ") or contact.address
            contact.city = input(f"City [{contact.city}]: ") or contact.city
            contact.state = input(f"State [{contact.state}]: ") or contact.state
            contact.zip_code = check_integer_input(f"ZIP Code [{contact.zip_code}]: ") or contact.zip_code
            contact.phone_number = check_integer_input(f"Phone Number [{contact.phone_number}]: ") or contact.phone_number
            contact.email = input(f"Email [{contact.email}]: ") or contact.email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

def main_menu():
    address_book = AddressBook(name="MyAddressBook")
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Edit Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
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
            address_book.add_contact(contact)

        elif choice == '2':
            address_book.display_all_contacts()

        elif choice == '3':
            first_name = input("Enter the first name of the contact to edit: ")
            address_book.edit_contact(first_name)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

'''
    @Author: V Sanjay Kumar
    @Date: 08-09-2024
    @Last Modified by: V Sanjay Kumar
    @Last Modified: 08-09-2024
    @Title: UC-3 updating the contact, adding delete functionality.
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
        Definition: Displays the contact details.
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
    Definition: Prompts the user for an integer input.
    parameter: None
    Return: Returns the integer value.
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
        parameter: contact (Contact) - The contact object.
        Return: None
        """
        self.contacts[contact.first_name] = contact
        print("Contact added successfully.")

    def edit_contact(self, first_name):
        """
        Definition: Edits an existing contact's details in the address book using the first name.
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

    def delete_contact(self, first_name):
        """
        Definition: Deletes a contact from the address book using the first name.
        parameter: first_name (str) - The first name of the contact to delete.
        Return: None
        """
        if first_name in self.contacts:
            del self.contacts[first_name]
            print(f"Contact '{first_name}' deleted successfully.")
        else:
            print("Contact not found.")
def main():
    # Collecting user input
    print("Enter contact details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = check_integer_input("ZIP Code: ")
    phone_number = check_integer_input("Phone Number: ")
    email = input("Email: ")

    # Creating a Contact object with the user-provided details
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

    # Creating the AddressBook and adding the contact
    address_book = AddressBook(name="MyAddressBook")
    address_book.add_contact(contact)

    # Displaying the contact details
    print("\n--------------Contact Details:---------------")
    print(contact.display_contact())

    # Editing the contact
    first_name_to_edit = input("Enter the first name of the contact to edit: ")
    address_book.edit_contact(first_name_to_edit)

    # Displaying the updated contact details
    print("\n--------------Updated Contact Details:---------------")
    print(contact.display_contact())

    # Deleting a contact
    first_name_to_delete = input("Enter the first name of the contact to delete: ")
    address_book.delete_contact(first_name_to_delete)

    # Display all contacts after deletion
    print("\n--------------All Contacts After Deletion:---------------")
    for contact in address_book.contacts.values():
        print(contact.display_contact())

if __name__ == "__main__":
    main()
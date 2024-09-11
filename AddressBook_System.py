"""
    @Author: V Sanjay Kumar
    @Date: 08-09-2024
    @Last Modified by: V Sanjay Kumar
    @Last Modified: 08-09-2024
    @Title : UC-15 save the contacts in json file.
"""
import os
import json


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
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zip Code: {self.zip_code}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Email: {self.email}\n")

    def to_dict(self):
        """Convert contact details to a dictionary for storing in a JSON file

        parametes :None

        returns:None"""
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone_number": self.phone_number,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        """Create a contact from a dictionary"""
        return Contact(
            data["first_name"],
            data["last_name"],
            data["address"],
            data["city"],
            data["state"],
            data["zip_code"],
            data["phone_number"],
            data["email"]
        )


def check_integer_input(prompt):
    """
    Prompts the user for an integer input.

    parameters(prompt):input
    Returns the integer value or None if input is empty.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}
        self.file_name = f"{name}.json"
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file with proper error handling
        parameters:None

        returs:None"""
        
        if os.path.exists(self.file_name):
            try:
                # Check if file is empty
                if os.stat(self.file_name).st_size == 0:
                    print(f"{self.file_name} is empty. Starting with no contacts.")
                    return
                # Attempt to load JSON data
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    for contact_data in data:
                        contact = Contact.from_dict(contact_data)
                        self.contacts[contact.first_name] = contact
                print(f"Loaded contacts from {self.file_name}.")
            except json.JSONDecodeError:
                print(f"Error: {self.file_name} contains invalid JSON data. Starting with no contacts.")
        else:
            print(f"No existing address book found for '{self.name}'. Starting a new one.")


    def save_contacts(self):
        """Save contacts to a JSON file
        
        parameters :None
        
        returns:None"""
        with open(self.file_name, 'w') as file:
            data = [contact.to_dict() for contact in self.contacts.values()]
            json.dump(data, file, indent=4)
        print(f"Contacts saved to {self.file_name}.")

    def add_or_update_contact(self, contact):
        '''
        the function takes the contact object and add to the contects

        parameters:contact

        returns:None
        '''
        if contact.first_name in self.contacts:
            print(f"Contact with first name '{contact.first_name}' already exists. Updating contact.")
        else:
            print(f"Adding new contact for '{contact.first_name}'.")
        self.contacts[contact.first_name] = contact
        self.save_contacts()

    def display_all_contacts(self):
        '''the function display the contacts list

        parameters :None

        retuns:None
        '''
        if not self.contacts:
            print("No contacts in address book.")
        else:
            for contact in self.contacts.values():
                print('-' * 30)
                print(contact.display_contact())

    def edit_contact(self, first_name):
        """Edits an existing contact in the address book.
        
        parameters(str):first_name
        
        returns:None"""
        if first_name in self.contacts:
            contact = self.contacts[first_name]
            print("Enter new details (leave blank to keep current value)")
            print("Which details do you want to update (first_name, last_name, address, city, state, zip_code, phone_number, email)? or Enter a exit to if you want exit")
            
            while True:
                choice = input().lower()
                if choice == "exit":
                    break
                if choice in ["first_name", "last_name", "address", "city", "state", "zip_code", "phone_number", "email"]:
                    value = input(f"{choice.replace('_', ' ').title()} [{getattr(contact, choice)}]: ") or getattr(contact, choice)
                    setattr(contact, choice, value)
                    print(f"{choice.replace('_', ' ').title()} updated successfully.")
                else:
                    print("Invalid choice.")
            self.save_contacts()
        else:
            print("Contact not found.")

    def delete_contact(self, first_name):
        """Deletes an existing contact in the address book.

           parameters(str):first_name
        
            returns:None"""
        if first_name in self.contacts:
            del self.contacts[first_name]
            print(f"Contact '{first_name}' deleted successfully.")
            self.save_contacts()
        else:
            print("Contact not found.")

    def sort_contacts(self, sort_by="first_name"):
        """Sorts the contacts by first name, last name, city, state, or zip code.
        
        parameters(str):first_name
        
        returns:None"""
        if sort_by not in ["first_name", "last_name", "city", "state", "zip_code"]:
            print("Invalid sort criteria.")
            return
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: getattr(c, sort_by).lower() if isinstance(getattr(c, sort_by), str) else getattr(c, sort_by))
        if not sorted_contacts:
            print("No contacts in address book.")
        else:
            print(f"\nContacts sorted by {sort_by.replace('_', ' ').title()}:")
            for contact in sorted_contacts:
                print('-' * 30)
                print(contact.display_contact())


class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        """Adds or updates an address book in the system.

        parameters(str):address_book name

        return:none
        
        returns:None"""
        if name in self.address_books:
            print(f"Address book with name '{name}' already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            print(f"Address book '{name}' created successfully.")

    def get_address_book(self, name):
        """Select an address book from the system.
        
        parameters(str):address_book name

        return:none
        """
        return self.address_books.get(name)

    def display_all_address_books(self):
        if not self.address_books:
            print("No address books available.")
        else:
            print("Available Address Books:")
            for name in self.address_books:
                print(f"- {name}")

    def search_contact_by_city_or_state(self, search_term, search_type):
        """Searches for contacts by city or state across all address books.
        
        parameters(str,str):search_term,search_type

        return:none
        """
        found = False
        for book_name, address_book in self.address_books.items():
            for contact in address_book.contacts.values():
                if (search_type == 'city' and contact.city.lower() == search_term.lower()) or \
                   (search_type == 'state' and contact.state.lower() == search_term.lower()):
                    print(f"\nFound in Address Book: {book_name}")
                    print(contact.display_contact())
                    found = True
        if not found:
            print(f"No contacts found in {search_type.capitalize()} '{search_term}' across all address books.")

    def count_contacts_by_city_or_state(self, search_term, search_type):
        """Counts contacts by city or state across all address books.
        
        parameters(str,str):search_term,search_type

        return:none"""
        count = 0
        for address_book in self.address_books.values():
            for contact in address_book.contacts.values():
                if (search_type == 'city' and contact.city.lower() == search_term.lower()) or \
                   (search_type == 'state' and contact.state.lower() == search_term.lower()):
                    count += 1
        return count


def main_menu():
    system = AddressBookSystem()
    while True:
        print("\nAddress Book System Menu:")
        print("1. Create a new Address Book")
        print("2. Select an Address Book")
        print("3. Display all Address Books")
        print("4. Search Contact by City or State")
        print("5. Count Contacts by City or State")
        print("6. Exit")
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
                    print("5. Sort Contacts")
                    print("6. Return to Main Menu")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        address = input("Address: ")
                        city = input("City: ")
                        state = input("State: ")
                        zip_code = check_integer_input("Zip Code: ")
                        phone_number = input("Phone Number: ")
                        email = input("Email: ")
                        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                        address_book.add_or_update_contact(contact)

                    elif sub_choice == '2':
                        address_book.display_all_contacts()

                    elif sub_choice == '3':
                        first_name = input("Enter the First Name of the contact to edit: ")
                        address_book.edit_contact(first_name)

                    elif sub_choice == '4':
                        first_name = input("Enter the First Name of the contact to delete: ")
                        address_book.delete_contact(first_name)

                    elif sub_choice == '5':
                        sort_by = input("Sort by (first_name, last_name, city, state, zip_code): ")
                        address_book.sort_contacts(sort_by)

                    elif sub_choice == '6':
                        break

                    else:
                        print("Invalid option, please try again.")

            else:
                print("Address Book not found.")

        elif choice == '3':
            system.display_all_address_books()

        elif choice == '4':
            search_type = input("Search by (city/state): ").lower()
            search_term = input(f"Enter the {search_type} to search for: ")
            system.search_contact_by_city_or_state(search_term, search_type)

        elif choice == '5':
            search_type = input("Count by (city/state): ").lower()
            search_term = input(f"Enter the {search_type} to count contacts: ")
            count = system.count_contacts_by_city_or_state(search_term, search_type)
            print(f"Number of contacts in {search_type.capitalize()} '{search_term}': {count}")

        elif choice == '6':
            print("Exiting the Address Book System. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main_menu()

from contact import Contact
from hash_map import HashMap
from merge_sort import merge_sort

def print_menu():
    print("\n--- CONTACTS APP ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts (Unsorted)")
    print("5. Display All Contacts (Sorted)")
    print("6. Exit")

def main():
    contacts_map = HashMap()

    while True:
        print_menu()
        choice = input("\nEnter choice: ")

        # Add contact
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            address = input("Address (optional): ")

            new_contact = Contact(name, phone, email, address)
            contacts_map.put(name.lower(), new_contact)
            print("Contact added successfully!")

        # Search
        elif choice == "2":
            name = input("Enter name to search: ").lower()
            result = contacts_map.get(name)

            if result:
                print("Contact found:", result)
            else:
                print("Contact not found.")

        # Delete
        elif choice == "3":
            name = input("Enter name to delete: ").lower()
            if contacts_map.remove(name):
                print("Contact deleted.")
            else:
                print("Contact not found.")

        # Display unsorted
        elif choice == "4":
            print("\n--- ALL CONTACTS (UNSORTED) ---")
            contacts_map.display()

        # Display sorted
        elif choice == "5":
            # Collect contacts from the hashmap
            all_contacts = []
            for bucket in contacts_map.buckets:
                current = bucket
                while current:
                    all_contacts.append(current.value)
                    current = current.next

            sorted_list = merge_sort(all_contacts)

            print("\n--- ALL CONTACTS (SORTED A-Z) ---")
            for contact in sorted_list:
                print(contact)

        elif choice == "6":
            print("Exiting app.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

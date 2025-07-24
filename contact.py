import csv
import os

FILE_NAME = 'contacts.csv'

def validate_phone(phone):
    return phone.isdigit() and (7 <= len(phone) <= 15)

def validate_email(email):
    return '@' in email and '.' in email and len(email) >= 5

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not validate_phone(phone):
        print("Invalid phone number. Must be digits only (7-15 digits).")
        return

    if not validate_email(email):
        print("Invalid email address.")
        return

    with open(FILE_NAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, phone, email])
    print("Contact added successfully!")

def display_contacts(contacts):
    print(f"{'Name':20} {'Phone':15} {'Email'}")
    print("-" * 50)
    for contact in contacts:
        print(f"{contact[0]:20} {contact[1]:15} {contact[2]}")

def search_contact():
    query = input("Search by name or phone number: ").strip()
    results = []
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if query.lower() in row[0].lower() or query in row[1]:
                results.append(row)
    if results:
        display_contacts(results)
    else:
        print("No contacts found.")

def update_contact():
    query = input("Enter name or phone number to update: ").strip()
    contacts = []
    updated = False

    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        contacts = list(reader)

    for i, row in enumerate(contacts):
        if query.lower() in row[0].lower() or query in row[1]:
            print(f"Current: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
            name = input("Enter new name (leave blank to keep same): ").strip()
            phone = input("Enter new phone number (leave blank to keep same): ").strip()
            email = input("Enter new email (leave blank to keep same): ").strip()

            if phone and not validate_phone(phone):
                print("Invalid phone number. Update cancelled.")
                return
            if email and not validate_email(email):
                print("Invalid email address. Update cancelled.")
                return

            if name:
                contacts[i][0] = name
            if phone:
                contacts[i][1] = phone
            if email:
                contacts[i][2] = email

            updated = True
            break

    if updated:
        with open(FILE_NAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    query = input("Enter name or phone number to delete: ").strip()
    contacts = []
    deleted = False

    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        contacts = list(reader)

    new_contacts = []
    for row in contacts:
        if query.lower() in row[0].lower() or query in row[1]:
            print(f"Deleted: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
            deleted = True
        else:
            new_contacts.append(row)

    if deleted:
        with open(FILE_NAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(new_contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    # Create file if it doesn't exist
    if not os.path.isfile(FILE_NAME):
        open(FILE_NAME, 'w').close()

    while True:
        print("\n--- Digital Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

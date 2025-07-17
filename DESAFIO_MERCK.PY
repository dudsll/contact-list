contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
def search_contact(name):
    if name in contacts:
        print("Phone number for", name, "is", contacts[name])
    else:
        print("Contact not found.")
def main():
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid chice")

main()
phonebook = {}

def add_new_entry(name, phone_number):
    if name not in phonebook:
        phonebook[name] = phone_number
        print("Number added successfully")
    else:
        print("Username already exists, try a different one.")

def check_number(name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "User not found"

def delete_user(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name}'s entry has been deleted.")
    else:
        print(f"{name} is not in the phonebook.")

def all_entries():
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

while True:
    print("Phonebook Menu:")
    print("1. Add a new entry")
    print("2. Look up a phone number")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_new_entry(name, number)
    elif choice == "2":
        name = input("Enter name to look up: ")
        result = check_number(name)
        print(result)
    elif choice == "3":
        user_to_delete = input("Enter user to delete: ")
        delete_user(user_to_delete)
    elif choice == "4":
        all_entries()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

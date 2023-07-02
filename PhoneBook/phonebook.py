def add_contact():
    lists = []
    print("Add a contact")
    name = str(input("Name: "))
    phone_number = int(input("Phone number: "))

    lists.append(name)
    lists.append(phone_number)

    file = open("contact.txt", "a+")
    if file.tell() == 0:
        file.write("Name, Phone number\n")

    file.write(', '.join(map(str, lists)))
    file.write('\n')
    file.close()

    print(f"Contact added: {name, phone_number}")

    add_again = input("You want to add another one?[y/n]: ")

    if add_again == 'y':
        add_contact()
    else:
        menu()

    menu()


def search_text(choice):
    with open('contact.txt', 'r') as file:
        lines = file.readlines()
        found = False
        for line in lines:
            if choice in line:
                print(line)
                found = True
        if not found:
            print("Contact not found.")


def search():
    print("""1. Search after name
           \n2. Search after phone number
           \n3. Back""")

    choice = int(input("What will you choose?: "))

    if choice == 1:
        name = input("Enter name: ")
        search_text(name)
        menu()
    elif choice == 2:
        number = input("Enter number: ")
        search_text(number)
        menu()
    else:
        menu()


def edit_contact():
    print("""1. Edit Name
           \n2. Edit Phone number
           \n3. Back""")

    edit = int(input("Enter what you want to edit: "))

    file = open("contact.txt", "r")
    if edit == 1:
        print(file.readlines()[1:])
        choose_name = str(input("Enter name you want to edit: "))

        new_name = str(input("Enter new name: "))

        with open('contact.txt', 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            modified_line = line.replace(choose_name, new_name)
            modified_lines.append(modified_line)

        with open('contact.txt', 'w') as file:
            file.writelines(modified_lines)

    elif edit == 2:
        print(file.readlines()[1:])
        choose_number = input("Enter number you want to edit: ")
        new_number = input("Enter new number: ")

        with open('contact.txt', 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            modified_line = line.replace(choose_number, new_number)
            modified_lines.append(modified_line)

        with open('contact.txt', 'w') as file:
            file.writelines(modified_lines)

    else:
        menu()
    menu()


def delete():
    file = open("contact.txt", "r")
    print(file.readlines()[1:])
    delete_contact = input("Enter name / phone number of a contact you want to remove: ")
    contacts = []

    with open('contact.txt', 'r') as file:
        for line in file:
            if delete_contact not in line:
                contacts.append(line)

    with open('contact.txt', 'w') as file:
        file.writelines(contacts)

    print("Contact removed successfully.")

    menu()


def menu():
    print("""1. See all contacts
          \n2. Add a contact
          \n3. Search for a contact by name or phone
          \n4. Edit a contact
          \n5. Delete a contact
          \n6. Close""")


def contact_run():

    answer = int(input("What you want to do?: "))

    file = open("contact.txt", "r")

    if answer == 1:
        print(file.readlines()[1:])
        menu()

    elif answer == 2:
        add_contact()

    elif answer == 3:
        search()

    elif answer == 4:
        edit_contact()

    elif answer == 5:
        delete()

    elif answer == 6:
        print("OK!")
        exit()


if __name__ == "__main__":
    menu()
    contact_run()

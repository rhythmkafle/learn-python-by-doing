import json

notes = []

def menu():
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            edit_notes()
        elif choice == '4':
            delete_notes()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


def save_to_file(data):
    with open('notes_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_note():
    title = input("Title: ")
    content = input("Content: ")
    data = {"Title": title, "Content": content}
    global notes
    notes.append(data)
    save_to_file(notes)

def view_notes():
    global notes
    if not notes:
        print("Notes not found")
        return
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note['Title']}\n {note['Content']}")

def edit_notes():
    edit = input("Title: ")
    global notes
    found = False
    for index, note in enumerate(notes, start=1):
        if edit.lower() == note['Title'].lower():
            print("Note found")
            new_content = input("New Content:")
            note['Content'] = new_content 
            found = True
            break
    
    if found == False:
        print("Notes not found!")
        return

    save_to_file(notes)
    print("Content Updated Successfully!!!")

def delete_notes():
    delete = input("Title: ")
    global notes
    found = False
    for index, note in enumerate(notes, start=1):
        if delete.lower() == note['Title'].lower():
            print("Note Found")
            confirm = input("Do you really want to delete this?(y/n)")
            if confirm.lower() == 'y':
                del notes[index-1]
                print("Note has been deleted!")
                found = True
                break
            else:
                print("Aborting Process!")
                return
    
    if found == False:
        print("Note not Found")
        return

    save_to_file(notes)
    print("Notes updated successfully!!!")

if __name__ == "__main__":
    try:
        with open('notes_data.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    menu()
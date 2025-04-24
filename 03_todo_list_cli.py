def menu():
    print("To Do List")
    print("-"*20)
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit the program")

tasks = []

def view():
    if len(tasks) == 0:
        print("No tasks to show. How about adding one?")
    else:
        for i, t in enumerate(tasks, start=1):
            print(i,t)

def add():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)

def mark():
    view()
    to_be_marked = int(input("Enter the task number to be marked completed:")) - 1    
    if 0 <= to_be_marked < len(tasks):
        tasks[to_be_marked] = f"[COMPLETED] {tasks[to_be_marked]}"

def remove():
    view()
    to_be_removed = int(input("Enter the task number to be removed: ")) - 1
    if 0<=to_be_removed<len(tasks):
        print("-"*20)
        tasks.pop(to_be_removed)
        print("Task Removed")
        view()

def exit_task():
    with open("03_todo_list.txt","a") as f:
        for i, t in enumerate(tasks, start=1): 
            f.write(f"{i}. {t}\n")
    print("Thanks for using our app")
    exit(0)

while True:
    menu()
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        view()
    elif user_choice == 2:
        add()
    elif user_choice == 3:
        mark()
    elif user_choice == 4: 
        remove()
    elif user_choice == 5:
        exit_task()
    else:
        print("Invalid input, please make sure you are choosing a number from 1 to 5")
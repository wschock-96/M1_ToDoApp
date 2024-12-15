
tasks = []

def intro_menu():
    print("Welcome to your To-Do List!")
    print("Menu:")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

def add_tasks():
    add_input = input("Enter in task to add: ").title()
    if add_input not in tasks:
        tasks.append(add_input)
        print(f"\n'{add_input}' has been added to task list.")
    else:
        print("Task is already exists in list.")

def view_tasks():
    print("\nCurrent Tasks: ")
    if not tasks:
        print("\nNo tasks currently available.")
    else:
        for task in tasks:
            print(f"\t{task}")

def delete_tasks():
    del_input = input("Enter in task to remove from list: ").title()
    if del_input not in tasks:
        print(f"\n'{del_input}' does not exist in list. Please choose from list.")
    else:
        print(f"\n'{del_input}' has been removed from task list.")
        tasks.remove(del_input)

while True:
    intro_menu()
    choices = input("Please choose from following options (1 - 4): ")
    try:
        if choices == '1':
            add_tasks()
        elif choices == '2':
            view_tasks()
        elif choices == '3':
            delete_tasks()
        elif choices == '4':
            print("\nGoodbye!")
            break
    except ValueError:
        print("\nError. Please provide numerical input")
    else:
        print("\nInvalid option. Choose from options 1-4.")
    
    finally:
        print("\n* To-Do List Application *\n")
        


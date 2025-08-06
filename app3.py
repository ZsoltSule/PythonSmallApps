running = True
tasks = []

while running:
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    
    choice = int(input("Choose an option: "))

    if choice == 1:
        if not tasks:
            print("No tasks yet")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == 2:
        newTask = input("Enter new task")
        tasks.append(newTask)
        print("Task added.")

    elif choice == 3:
        if not tasks:
            print ("No tasks to remove.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            try:
                remove_index = int(input("Enter task number to remove: ")) - 1
                if 0 <= remove_index < len(tasks):
                    removed = tasks.pop(remove_index)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == 4:
        running = False



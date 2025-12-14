tasks = []

def show_tasks():
    print("\nTasks:")
    if len(tasks) == 0:
        print("No tasks")
    else:
        for i in range(len(tasks)):
            print(i+1, "-", tasks[i])
    print()

def add_task():
    t = input("New task: ")
    tasks.append(t)

def remove_task():
    show_tasks()
    if len(tasks) > 0:
        n = int(input("Which task to remove? "))
        tasks.pop(n-1)

def edit_task():
    show_tasks()
    if len(tasks) > 0:
        n = int(input("Which task to edit? "))
        new_t = input("Enter new text: ")
        tasks[n-1] = new_t

def complete_task():
    show_tasks()
    if len(tasks) > 0:
        n = int(input("Which task is completed? "))
        tasks[n-1] = tasks[n-1] + " (done)"

def menu():
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Edit task")
    print("5. Mark complete")
    print("6. Exit")

def main():
    while True:
        show_tasks()
        menu()
        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            break
        else:
            print("Invalid")

main()

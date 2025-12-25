tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
while True:
    show_menu()
    choice = int(input("Choose: "))
    
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
        
    elif choice == 2:
        print("\nYour Tasks: ")
        for i,t in enumerate(tasks,1):
            print(i,t)
            
    elif choice == 3:
        num = int(input("Enter task number: "))
        tasks.pop(num-1)
        print("Task Deleted!")
        
    elif choice == 4:
        print("Exiting To-Do List. Goodbye!")
        break
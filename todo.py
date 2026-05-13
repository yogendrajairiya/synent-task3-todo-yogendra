
task_list = []

print("Welcome to Task Manager")

while True:

    print("\nChoose an option to perform this tasks")
    print("1 - Add Task")
    print("2 - View Tasks")
    print("3 - Delete Task")
    print("4 - Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":              ####### Add Task

        new_task = input("Enter task name: ")

        if new_task != "":
            task_list.append(new_task)
            print("Task added successfully")
        else:
            print("Task cannot be empty")


    elif user_choice == "2":           ####### View Tasks

        if len(task_list) == 0:
            print("No tasks found")

        else:
            print("\nYour Tasks:")

            count = 1

            for task in task_list:
                print(str(count) + ". " + task)
                count = count + 1

    elif user_choice == "3":          ### Delete Task

        if len(task_list) == 0:
            print("Task list is empty")

        else:
            print("\nTasks:")

            count = 1

            for task in task_list:
                print(str(count) + ". " + task)
                count = count + 1

            try:
                delete_task = int(input("Enter task number to delete: "))

                if delete_task > 0 and delete_task <= len(task_list):

                    removed_task = task_list.pop(delete_task - 1)

                    print(removed_task + " deleted successfully")

                else:
                    print("Invalid task number")

            except ValueError:
                print("Please enter a valid number")

    elif user_choice == "4":              #### Exit Program

        print("Exiting program")
        break

    else:               ######  Invalid Choice
        print("Please enter valid choice")
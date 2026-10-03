class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"

    def display(self):
        print("------------------------------------------")
        print("Task ID     :", self.task_id)
        print("Title       :", self.title)
        print("Description :", self.description)
        print("Status      :", self.status)


tasks = []
task_id = 1


def create_task():
    global task_id

    title = input("Enter task title: ")
    description = input("Enter task description: ")

    new_task = Task(task_id, title, description)
    tasks.append(new_task)

    print("\nTask created successfully!")
    print("Task ID:", task_id)

    task_id += 1


def read_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== ALL TASKS ==========")

    for task in tasks:
        task.display()

    print("------------------------------------------")


def update_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    task_id_input = int(input("Enter Task ID to update: "))

    for task in tasks:
        if task.task_id == task_id_input:
            print("\n1. Update Title")
            print("2. Update Description")
            print("3. Mark as Completed")

            choice = input("Enter your choice: ")

            if choice == "1":
                task.title = input("Enter new title: ")
                print("\nTitle updated successfully!")

            elif choice == "2":
                task.description = input("Enter new description: ")
                print("\nDescription updated successfully!")

            elif choice == "3":
                task.status = "Completed"
                print("\nTask marked as completed!")

            else:
                print("\nInvalid choice.")

            return

    print("\nTask not found.")


def delete_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    task_id_input = int(input("Enter Task ID to delete: "))

    for task in tasks:
        if task.task_id == task_id_input:
            tasks.remove(task)
            print("\nTask deleted successfully!")
            return

    print("\nTask not found.")


print("==========================================")
print("             TASK MANAGER")
print("==========================================")

while True:
    print("\n========== MENU ==========")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_task()

    elif choice == "2":
        read_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using Task Manager!")
        break

    else:
        print("\nInvalid choice! Please try again.")
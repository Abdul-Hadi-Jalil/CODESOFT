import todo_app

if __name__ == "__main__":
    ui = todo_app.ToDoApp()

    while True:
        print("\n===== ToDo List Application =====")
        print("1. Create Category")
        print("2. Create Task")
        print("3. Mark Task as Completed")
        print("4. Display Categories")
        print("5. Display Tasks in Category")
        print("6. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            category_name = input("Enter category name: ")
            ui.create_category(category_name)

        elif choice == "2":
            category_name = input("Enter category name: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            ui.create_task(category_name, title, description, due_date)

        elif choice == "3":
            category_name = input("Enter category name: ")
            task_title = input("Enter task title: ")
            ui.mark_task_as_completed(category_name, task_title)

        elif choice == "4":
            ui.display_categories()

        elif choice == "5":
            category_name = input("Enter category name: ")
            ui.display_tasks_in_category(category_name)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


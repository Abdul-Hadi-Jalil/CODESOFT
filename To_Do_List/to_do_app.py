class Task:
    def __init__(self, title=str(), description=str(), due_date=str()):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue: {self.due_date}"


class Category:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def __str__(self):
        return f"Category Name: {self.name}\nNumber of tasks in {self.name}: {self.tasks}"


class ToDoApp:
    def __init__(self):
        self.categories = dict()

    def create_category(self, name):
        category = Category(name)
        self.categories[name] = category


    def create_task(self, category_name, title=str(), description=str(), due_date=str()):
        task = Task(title, description, due_date)
        self.categories[category_name].add_task(task)


    def mark_task_as_complete(self, category_name, task_title):
        if category_name in self.categories:
            for task in self.categories[category_name].tasks:
                if task.title == task_title:
                    task.complete()
                    print(f"Task '{task_title}' marked as completed.")
                    return
            print(f"Task '{task_title}' not found in '{category_name}' category.")
        else:
            print(f"Category '{category_name}' does not exist.")


    def display_categories(self):
        for category in self.categories.values():
            print(category)


    def display_tasks_in_category(self, category_name):
        if category_name in self.categories:
            for task in self.categories[category_name].tasks:
                print(task)
        else:
            print(f"Category {category_name} does not exist")

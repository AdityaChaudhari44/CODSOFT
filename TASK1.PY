import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}"

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(task['title'], task['description']) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            tasks_data = [{'title': task.title, 'description': task.description, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, file, indent=4)

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        self.save_tasks()

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def update_task(self, title, new_description):
        for task in self.tasks:
            if task.title == title:
                task.description = new_description
                self.save_tasks()
                return
        print("Task not found!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for task in self.tasks:
                print(task)
                print("-" * 30)

# Sample usage
app = TodoApp()

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Update Task Description")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        app.add_task(title, description)
    elif choice == '2':
        title = input("Enter task title to remove: ")
        app.remove_task(title)
    elif choice == '3':
        app.view_tasks()
    elif choice == '4':
        title = input("Enter task title to update: ")
        new_description = input("Enter new description: ")
        app.update_task(title, new_description)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")

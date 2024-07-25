class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = {
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task added: {description}, due by {due_date}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f"Task marked as completed: {self.tasks[task_index]['description']}")
        else:
            print("Invalid task index.")

    def display_pending_tasks(self):
        print("Pending Tasks:")
        for index, task in enumerate(self.tasks):
            if not task['completed']:
                print(f"{index + 1}. {task['description']} (Due: {task['due_date']})")

# Example usage
todo_list = ToDo()
todo_list.add_task("Buy groceries", "2024-07-25")
todo_list.add_task("Finish project report", "2024-07-27")
todo_list.add_task("Call Alice", "2024-07-24")

todo_list.display_pending_tasks()

todo_list.mark_task_completed(1)
todo_list.display_pending_tasks()

        
        
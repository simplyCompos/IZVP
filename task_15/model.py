class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def change_status(self):
        self.completed = not self.completed

    def get_status(self):
        if self.completed:
            return "Виконано"
        return "Не виконано"


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if title.strip() == "":
            return False

        self.tasks.append(Task(title.strip()))
        return True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

    def change_task_status(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].change_status()
            return True
        return False

    def get_tasks(self):
        return self.tasks

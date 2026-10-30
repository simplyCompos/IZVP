class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Підключення кнопок до функцій
        self.view.add_button.config(command=self.add_task)
        self.view.status_button.config(command=self.change_status)
        self.view.delete_button.config(command=self.delete_task)

    def add_task(self):
        title = self.view.get_task_title()

        if self.model.add_task(title):
            self.view.clear_entry()
            self.update_view()
        else:
            self.view.show_error("Назва завдання не може бути порожньою!")

    def change_status(self):
        index = self.view.get_selected_task()

        if index is None:
            self.view.show_error("Спочатку оберіть завдання!")
            return

        self.model.change_task_status(index)
        self.update_view()

    def delete_task(self):
        index = self.view.get_selected_task()

        if index is None:
            self.view.show_error("Спочатку оберіть завдання!")
            return

        self.model.delete_task(index)
        self.update_view()

    def update_view(self):
        tasks = self.model.get_tasks()
        self.view.update_task_list(tasks)

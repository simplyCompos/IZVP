import tkinter as tk
from tkinter import messagebox


class TaskView:
    def __init__(self, root):
        self.root = root
        self.root.title("Список завдань")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        # Поле введення назви завдання
        self.task_entry = tk.Entry(root, font=("Arial", 12), width=35)
        self.task_entry.pack(pady=15)

        # Кнопка додавання
        self.add_button = tk.Button(
            root,
            text="Додати завдання",
            width=20
        )
        self.add_button.pack(pady=5)

        # Список завдань
        self.task_list = tk.Listbox(
            root,
            width=55,
            height=12,
            font=("Arial", 11)
        )
        self.task_list.pack(pady=15)

        # Кнопки керування
        self.status_button = tk.Button(
            root,
            text="Змінити статус",
            width=20
        )
        self.status_button.pack(pady=5)

        self.delete_button = tk.Button(
            root,
            text="Видалити завдання",
            width=20
        )
        self.delete_button.pack(pady=5)

    def update_task_list(self, tasks):
        self.task_list.delete(0, tk.END)

        for task in tasks:
            status = task.get_status()
            self.task_list.insert(
                tk.END,
                f"{task.title} — {status}"
            )

    def get_task_title(self):
        return self.task_entry.get()

    def clear_entry(self):
        self.task_entry.delete(0, tk.END)

    def get_selected_task(self):
        selection = self.task_list.curselection()

        if selection:
            return selection[0]

        return None

    def show_error(self, message):
        messagebox.showerror("Помилка", message)

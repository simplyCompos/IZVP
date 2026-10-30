import tkinter as tk

from model import TaskModel
from view import TaskView
from controller import TaskController


def main():
    root = tk.Tk()

    model = TaskModel()
    view = TaskView(root)
    controller = TaskController(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()

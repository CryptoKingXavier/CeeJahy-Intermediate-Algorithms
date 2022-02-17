from tkinter import *
from tkinter import ttk

class ToDoFunction:
    def options(self):
        return """Functions: AddToDo, CancelToDo, RemoveToDo, ViewToDos, CompleteToDo"""

    ToDoList = []
    _ToDoList = []

    def AddToDo(self, todo: str):
        self.ToDoList.append(todo)
        for Todo in self.ToDoList:
            if self.ToDoList.count(Todo) > 1:
                self.ToDoList.remove(Todo)

    def RemoveToDo(self, _todo: int):
        if len(self.ToDoList) == 0:
            print("Empty List")
        else:
            removed_todo = self.ToDoList.pop(_todo - 1)
            self._ToDoList.append(removed_todo)
            print(self.ToDoList)
            return f"{removed_todo} was removed!"

    def ViewToDo(self):
        view_root = Tk()
        view_root.title("ToDoList: -> MyToDoList")
        # view_root.geometry("300x300")
        if len(self.ToDoList) == 0:
            print("Empty List")
        else:
            print("Truncated Duplicate Entries")
            for (key, Todo) in enumerate(self.ToDoList):
                label = Label(view_root, text=f"{key+1}. {Todo}", font="Pacifico, 10").pack(pady=1)
        view_root.mainloop()

    def CompleteToDo(self):
        complete_root = Tk()
        complete_root.title("ToDoList: -> CompletedToDoList")
        # complete_root.geometry("300x300")
        print("Completed ToDo:")
        if len(self._ToDoList) == 0:
            print("Empty List")
        else:
            for (key, Todo) in enumerate(self._ToDoList):
                label = Label(complete_root, text=f"{key+1}. {Todo}", font="Pacifico, 10").pack(pady=1)
        complete_root.mainloop()

    def cancelToDo(self, _todo: int):
        if len(self.ToDoList) == 0:
            print('?Pop?')
            pass
        else:
            import string
            if (_todo == ''  or _todo == " ") and (str(_todo) not in list(string.digits)):
                print('Invalid!')
            else:
                self.ToDoList.remove(self.ToDoList[int(_todo) - 1])

    def ToDoChoice(self):
        choice = input("Pick a function: ")
        if choice == '1':
            todo = input("ToDo -> ")
            self.AddToDo(todo)
        elif choice == '2':
            rem = int(input("Remove -> "))
            self.cancelToDo(rem)
        elif choice == '3':
            num = int(input('ToDo Num. -> '))
            self.RemoveToDo(num)
        elif choice == '4':
            self.ViewToDo()
        elif choice == '5':
            self.CompleteToDo()

    _q = input('[Y/N]: ')

myToDo = ToDoFunction()
valid = ["Yes", "YES", "yes", "y", "Y"]

while True:
    if myToDo._q not in valid:
        break
    else:
        print(myToDo.options())
        myToDo.ToDoChoice()
        print()

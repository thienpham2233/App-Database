from Model import DatabaseModel
from View import DatabaseView
import tkinter as tk

class DatabaseController:
    def __init__(self, root):
        self.view = DatabaseView(root)
        self.view.connect_button.config(command=self.connect_db)
        self.view.load_button.config(command=self.load_data)
        self.view.insert_button.config(command=self.insert_data)
        self.view.delete_button.config(command=self.delete_selected)
        self.model = None

    def connect_db(self):
        db_name = self.view.db_name.get()
        user = self.view.user.get()
        password = self.view.password.get()
        host = self.view.host.get()
        port = self.view.port.get()

        self.model = DatabaseModel(db_name, user, password, host, port)

    def load_data(self):
        if self.model:
            table_name = self.view.table_name.get()
            rows = self.model.load_data(table_name)
            self.view.display_data(rows)
        else:
            print("No database connection.")

    def insert_data(self):
        if self.model:
            table_name = self.view.table_name.get()
            column1 = self.view.column1.get()
            column2 = self.view.column2.get()
            column3 = self.view.column3.get()
            self.model.insert_data(table_name, column1, column2, column3)
            self.load_data()  # Refresh data
        else:
            print("No database connection.")

    def delete_selected(self):
        if self.model:
            selected_item = self.view.tree.selection()
            if not selected_item:
                print("No item selected.")
                return

            table_name = self.view.table_name.get()
            for item in selected_item:
                values = self.view.tree.item(item, "values")
                mssv = values[2]  # Assuming MSSV is the primary key
                self.model.delete_data(table_name, mssv)
                self.view.tree.delete(item)
        else:
            print("No database connection.")

if __name__ == "__main__":
    root = tk.Tk()
    controller = DatabaseController(root)
    root.mainloop()

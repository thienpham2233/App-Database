import tkinter as tk
from tkinter import ttk, messagebox

class DatabaseView:
    def __init__(self, root):
        self.root = root
        self.root.title("App Quản Lý Sinh Viên")
        
        # Entry fields for connection and table details
        self.db_name = tk.StringVar(value='postgres')
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='02072003')
        self.host = tk.StringVar(value='localhost')
        self.port = tk.StringVar(value='5432')
        self.table_name = tk.StringVar(value='danhsach')

        # Create the GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Add title label at the top
        title_label = tk.Label(self.root, text="App Quản Lý Sinh Viên", font=("Arial", 16), fg="blue")
        title_label.pack(pady=10)    

        # Connection section
        connection_frame = tk.Frame(self.root)
        connection_frame.pack(pady=10)

        tk.Label(connection_frame, text="DB Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(connection_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Host:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.host).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Port:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.port).grid(row=4, column=1, padx=5, pady=5)

        self.connect_button = tk.Button(connection_frame, text="Connect")
        self.connect_button.grid(row=5, columnspan=2, pady=10)

        # Query section
        query_frame = tk.Frame(self.root)
        query_frame.pack(pady=10)

        tk.Label(query_frame, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(query_frame, textvariable=self.table_name).grid(row=0, column=1, padx=5, pady=5)

        self.load_button = tk.Button(query_frame, text="Load Data")
        self.load_button.grid(row=1, columnspan=2, pady=10)

        # Treeview section
        self.tree = ttk.Treeview(self.root, columns=("HoTen", "DiaChi", "MSSV"), show="headings", height=10)
        self.tree.heading("HoTen", text="Họ tên")
        self.tree.heading("DiaChi", text="Địa chỉ")
        self.tree.heading("MSSV", text="MSSV")
        self.tree.pack(pady=10, fill="x", expand=True)

        # Add scrollbars for the treeview
        scrollbar_y = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar_y.set)
        scrollbar_y.pack(side="right", fill="y")

        # Insert section
        insert_frame = tk.Frame(self.root)
        insert_frame.pack(pady=10)

        self.column1 = tk.StringVar()
        self.column2 = tk.StringVar()
        self.column3 = tk.StringVar()

        tk.Label(insert_frame, text="Họ tên:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.column1).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(insert_frame, text="Địa chỉ:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.column2).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(insert_frame, text="MSSV:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.column3).grid(row=2, column=1, padx=5, pady=5)

        self.insert_button = tk.Button(insert_frame, text="Insert Data")
        self.insert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Delete button
        self.delete_button = tk.Button(self.root, text="Delete Selected", fg="red")
        self.delete_button.pack(pady=10)

    def display_data(self, rows):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new data
        for row in rows:
            self.tree.insert("", "end", values=row)

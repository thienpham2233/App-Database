import psycopg2
from psycopg2 import sql
from tkinter import messagebox

class DatabaseModel:
    def __init__(self, db_name, user, password, host, port):
        try:
            self.conn = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def load_data(self, table_name):
        try:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    def insert_data(self, table_name, column1, column2, column3):
        try:
            insert_query = sql.SQL(
                "INSERT INTO {} (hoten, diachi, mssv) VALUES (%s, %s, %s)"
            ).format(sql.Identifier(table_name))
            self.cur.execute(insert_query, (column1, column2, column3))
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def delete_data(self, table_name, mssv):
        try:
            delete_query = sql.SQL(
                "DELETE FROM {} WHERE mssv = %s"
            ).format(sql.Identifier(table_name))
            self.cur.execute(delete_query, (mssv,))
            self.conn.commit()
            messagebox.showinfo("Success", "Data deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")

import tkinter as tk
from tkinter import messagebox
import requests

class TeacherManagementUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Management System")

        self.label_id = tk.Label(root, text="ID:")
        self.label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1)

        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=1, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=1, column=1)

        self.label_subject = tk.Label(root, text="Subject:")
        self.label_subject.grid(row=2, column=0)
        self.entry_subject = tk.Entry(root)
        self.entry_subject.grid(row=2, column=1)

        self.button_add = tk.Button(root, text="Add Teacher", command=self.add_teacher)
        self.button_add.grid(row=3, column=0, columnspan=2)

        self.button_update = tk.Button(root, text="Update Teacher", command=self.update_teacher)
        self.button_update.grid(row=4, column=0, columnspan=2)

        self.button_delete = tk.Button(root, text="Delete Teacher", command=self.delete_teacher)
        self.button_delete.grid(row=5, column=0, columnspan=2)

        self.button_view = tk.Button(root, text="View Teachers", command=self.view_teachers)
        self.button_view.grid(row=6, column=0, columnspan=2)

    def add_teacher(self):
        name = self.entry_name.get()
        subject = self.entry_subject.get()

        # Send data to Flask backend for adding a teacher
        url = 'http://127.0.0.1:5000/add_teacher'
        data = {'name': name, 'subject': subject}

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            messagebox.showinfo("Success", f"Teacher {name} added successfully.")
            self.clear_entries()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to add teacher: {e}")

    def update_teacher(self):
        id = self.entry_id.get()
        name = self.entry_name.get()
        subject = self.entry_subject.get()

        # Send data to Flask backend for updating a teacher
        url = f'http://127.0.0.1:5000/update_teacher/{id}'
        data = {'name': name, 'subject': subject}

        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
            messagebox.showinfo("Success", f"Teacher {id} updated successfully.")
            self.clear_entries()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to update teacher: {e}")

    def delete_teacher(self):
        id = self.entry_id.get()

        # Send data to Flask backend for deleting a teacher
        url = f'http://127.0.0.1:5000/delete_teacher/{id}'

        try:
            response = requests.delete(url)
            response.raise_for_status()
            messagebox.showinfo("Success", f"Teacher {id} deleted successfully.")
            self.clear_entries()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to delete teacher: {e}")

    def view_teachers(self):
        # Fetch teachers from Flask backend
        url = 'http://127.0.0.1:5000/get_teachers'

        try:
            response = requests.get(url)
            response.raise_for_status()
            teachers = response.json()

            # Display teachers in a messagebox (you can customize this part)
            teachers_info = "\n".join([f"{teacher['id']} - {teacher['name']} - {teacher['subject']}" for teacher in teachers])
            messagebox.showinfo("Teachers", teachers_info)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch teachers: {e}")

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_subject.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TeacherManagementUI(root)
    root.mainloop()
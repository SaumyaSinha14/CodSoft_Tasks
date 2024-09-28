import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Contacts:
    def __init__(self, root):
        self.contacts = {}
        self.root = root
        self.root.title("Contacts")
        self.create_gui()

    def create_gui(self):
        tk.Label(self.root, text="Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Phone").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Email").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Address").grid(row=3, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(self.root)
        self.phone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)

        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=6, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=6, column=1, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists!")
        else:
            self.contacts[name] = Contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            view_window = tk.Toplevel(self.root)
            view_window.title("Contact List")

            row = 0
            for name, contact in self.contacts.items():
                tk.Label(view_window, text=f"Name: {contact.name}").grid(row=row, column=0, padx=10, pady=5)
                tk.Label(view_window, text=f"Phone: {contact.phone}").grid(row=row, column=1, padx=10, pady=5)
                tk.Label(view_window, text=f"Email: {contact.email}").grid(row=row, column=2, padx=10, pady=5)
                tk.Label(view_window, text=f"Address: {contact.address}").grid(row=row, column=3, padx=10, pady=5)
                row += 1

    def search_contact(self):
        search_term = self.name_entry.get()
        found = False
        for name, contact in self.contacts.items():
            if search_term.lower() in name.lower() or search_term == contact.phone:
                messagebox.showinfo("Contact Found", f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found!")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            if address:
                self.contacts[name].address = address

            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    manager = Contacts(root)
    root.mainloop()

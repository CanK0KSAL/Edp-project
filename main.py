import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime



class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSentEvent(Event):
    name = "application_sent"

class ApplicationRejectedEvent(Event):
    name = "application_rejected"

class ApplicationAcceptedEvent(Event):
    name = "application_accepted"

communication_queue = []


class University:
    def __init__(self, name):
        self.name = name

    def process_event(self, event):
        if isinstance(event, ApplicationSentEvent):
            return self.handle_application(event)

    def handle_application(self, event):
        message = f"University {self.name} received an application from {event.payload['name']} for the {event.payload['department']} department.\n"
        time.sleep(1)
        if random.choice([True, False]):
            message += self.accept_application(event)
        else:
            message += self.reject_application(event)
        return message

    def accept_application(self, event):
        acceptance_event = ApplicationAcceptedEvent(event.payload)
        return f"[ACCEPTED] {event.payload['name']}'s application to the {event.payload['department']} department has been accepted by {self.name}.\n"

    def reject_application(self, event):
        rejection_event = ApplicationRejectedEvent(event.payload)
        return f"[REJECTED] {event.payload['name']}'s application to the {event.payload['department']} department has been rejected by {self.name}.\n"



class ApplicationSystemUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wseiz University Application System")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        
        self.university = University("Wseiz University")
        self.departments = ["Computer Science", "Business Administration", "Psychology", "Management", "Engineering"]

        
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.department_var = tk.StringVar()
        self.department_var.set(self.departments[0])

        
        ttk.Label(root, text="Wseiz University Application Form", font=("Helvetica", 16), background="#f0f0f0").pack(pady=10)

        
        self.create_label_and_entry("Full Name:", self.name_var, 0)

        
        self.create_label_and_entry("Email Address:", self.email_var, 1)

        
        ttk.Label(root, text="Date of Birth:                                                                                                             Please write as YYYY-MM-DD", background="#f0f0f0").pack(anchor="w", padx=20, pady=5)
        self.dob_picker = ttk.Entry(root, textvariable=self.dob_var)
        self.dob_picker.pack(fill="x", padx=20, pady=5)
        self.dob_picker.insert(0, "YYYY-MM-DD")
        self.dob_picker.bind("<FocusIn>", self.clear_placeholder)

        
        ttk.Label(root, text="Select Department:", background="#f0f0f0").pack(anchor="w", padx=20, pady=5)
        self.department_menu = ttk.OptionMenu(root, self.department_var, *self.departments)
        self.department_menu.pack(fill="x", padx=20, pady=5)

        
        self.submit_button = ttk.Button(root, text="Submit Application", command=self.submit_application)
        self.submit_button.pack(pady=20)

        
        self.output_text = tk.Text(root, height=10, width=60, state="disabled", bg="#e6e6e6")
        self.output_text.pack(padx=20, pady=10)
    def create_label_and_entry(self, label_text, variable, row):
        ttk.Label(self.root, text=label_text, background="#f0f0f0").pack(anchor="w", padx=20, pady=5)
        entry = ttk.Entry(self.root, textvariable=variable)
        entry.pack(fill="x", padx=20, pady=5)

    def clear_placeholder(self, event):
        if self.dob_picker.get() == "YYYY-MM-DD":
            self.dob_picker.delete(0, tk.END)

    def validate_email(self, email):
        return "@" in email and "." in email

    def validate_name(self, name):
        return len(name.strip()) > 2

    def validate_dob(self, dob):
        try:
            birth_date = datetime.strptime(dob, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age >= 18
        except ValueError:
            return False

    def submit_application(self):
        name = self.name_var.get()
        email = self.email_var.get()
        dob = self.dob_var.get()
        department = self.department_var.get()

        if not name or not email or not dob:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        if not self.validate_name(name):
            messagebox.showerror("Error", "Full Name must be at least 3 characters long.")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        if not self.validate_dob(dob):
            messagebox.showerror("Error", "You must be at least 18 years old to apply.")
            return

        event = ApplicationSentEvent({"name": name, "email": email, "dob": dob, "department": department})
        communication_queue.append(event)

        self.output_text.config(state="normal")
        self.output_text.insert(tk.END, f"[APPLY] {name} applied to {department} department.\n")
        self.output_text.config(state="disabled")

        self.process_application()

    def process_application(self):
        if not communication_queue:
            return

        time.sleep(3)  # Simulate processing delay

        self.output_text.config(state="normal")
        event = communication_queue.pop(0)
        message = self.university.process_event(event)
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationSystemUI(root)
    root.mainloop()

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


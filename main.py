import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from applicationsystemui import ApplicationSystemUI

class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSentEvent(Event):
    name = "application_sent"

class ApplicationRejectedEvent(Event):
    name = "application_rejected"

class ApplicationAcceptedEvent(Event):
    name = "application_accepted"



if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationSystemUI(root)
    root.mainloop()

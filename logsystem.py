import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime






class LogSystem:
    def __init__(self, log_file="application_log.txt"):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()} - {message}\n")
import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from event import ApplicationSentEvent, ApplicationAcceptedEvent, ApplicationRejectedEvent

class University:
    def __init__(self, name, logger):
        self.name = name
        self.logger = logger

    def process_event(self, event):
        if isinstance(event, ApplicationSentEvent):
            return self.handle_application(event)

    def handle_application(self, event):
        message = f"University {self.name} received an application from {event.payload['name']} for the {event.payload['department']} department.\n"
        self.logger.log(message)
        time.sleep(1)
        if random.choice([True, False]):
            message += self.accept_application(event)
        else:
            message += self.reject_application(event)
        return message

    def accept_application(self, event):
        acceptance_event = ApplicationAcceptedEvent(event.payload)
        message = f"[ACCEPTED] {event.payload['name']}'s application to the {event.payload['department']} department has been accepted by {self.name}.\n"
        self.logger.log(message)
        return message

    def reject_application(self, event):
        rejection_event = ApplicationRejectedEvent(event.payload)
        message = f"[REJECTED] {event.payload['name']}'s application to the {event.payload['department']} department has been rejected by {self.name}.\n"
        self.logger.log(message)
        return message


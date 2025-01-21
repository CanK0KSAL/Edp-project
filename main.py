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

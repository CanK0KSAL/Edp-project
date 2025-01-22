



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

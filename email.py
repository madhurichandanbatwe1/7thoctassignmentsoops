class email:
    def __init__(self,sender,recipient,subject):
        self.sender=sender
        self.recipient=recipient
        self.subject=subject
        self.sent=False
        
    def sending_email(self):
        self.sent=True
        print(f"Email sent to {self.recipient} from {self.sender}")
    
    def display_email_details(self):
        print(f"Info of enail is {self.sender},{self.recipient},{self.subject}")
        
remembrance=email('Deshpande','Deshmukh','remembrance')
remembrance.sending_email()
remembrance.display_email_details()
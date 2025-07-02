class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    # Set Values
    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next
    
    # Get Values
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    # Check if next exists
    def has_next(self):
        return self.next != None
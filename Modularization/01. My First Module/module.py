# author : @jhhalls

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

class Greeter:
    """A simple class to greet people."""
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        """Return a greeting message."""
        return f"Hello, {self.name}!"

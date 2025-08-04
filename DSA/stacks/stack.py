class Stack:
    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

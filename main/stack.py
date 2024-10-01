class Stack:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        elem = self.elements.pop()
        return elem
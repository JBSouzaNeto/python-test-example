class Queue:
  def __init__(self):
    self.elements = []

  def enqueue(self, item):
    self.elements.append(item)

  def dequeue(self):
    if self.is_empty():
      raise Exception('Empty Queue')
    return self.elements.pop(0)

  def peek(self):
    if self.is_empty():
      raise Exception('Empty Queue')
    return self.elements[0]

  def is_empty(self):
    return self.elements == []

  def size(self):
    return len(self.elements)
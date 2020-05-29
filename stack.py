class Stack:

    def __init__(self, value: str = ''):
        self.st = value

    def is_empty(self):
        if len(self.st):
            return False
        else:
            return True

    def get_size(self):
        return len(self.st)

    def pop(self):
        if not self.is_empty():
            last = self.st[-1]
            self.st = self.st[:-1]
            return last
        return None

    def peek(self):
        if not self.is_empty():
            last = self.st[-1]
            return last
        return None

    def push(self, el: str):
        if len(el) != 1:
            print("EL should have only one character")
            return
        self.st = self.st + el




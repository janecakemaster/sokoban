
class Fifo:

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.insert(0, x)
        # return self.q

    def pop(self):
        return self.q.pop(0)

    def isEmpty(self):
        if len(self.q) == 0:
            return True

    def __len__(self):
        return len(self.q)
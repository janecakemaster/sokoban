class SetQueue:

    def __init__(self):
        self.q = []
        self.s = set()

    def push(self, x):
        self.q.insert(0, x)
        self.s.add(x)

    def pop(self):
        return self.q.pop(0)
        self.s.remove(x)

    def isEmpty(self):
        if len(self.q) == 0:
            return True

    def __len__(self):
        return len(self.q)

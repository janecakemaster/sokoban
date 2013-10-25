class MyQueue:

    '''
    Custom FIFO queue that keeps track of a queue in a list
    '''

    def __init__(self):
        self.q = []

    def push(self, x):
        ''' inserts at the beginning of the list '''
        self.q.insert(0, x)

    def pop(self):
        ''' removes the first item in the list '''
        return self.q.pop(0)

    def isEmpty(self):
        ''' checks for empty list '''
        if len(self.q) == 0:
            return True

    def __len__(self):
        ''' overriding len() '''
        return len(self.q)

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.idx = 0

    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer.pop(self.idx)
            self.buffer.insert(self.idx, item)
            self.idx += 1
            if self.idx == self.capacity:
                self.idx = 0

    def get(self):
        return self.buffer

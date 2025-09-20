class q:
    def __init__(self, size=10):
        self.q = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def enq(self, data):
        if self.rear == self.size - 1:
            return

        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.q[self.rear] = data

    def deq(self):
        if self.front == -1 or self.front > self.rear:
            return

        removed = self.q[self.front]
        self.q[self.front] = None
        self.front += 1

        if self.front > self.rear:
            self.front = self.rear = -1

        return removed

    def display(self):
        if self.front == -1 or self.front > self.rear:
            return
        for i in range(self.front, self.rear + 1):
            print(self.q[i])


if __name__ == "__main__":
    que = q()
    que.enq(10)
    que.enq(20)
    que.enq(30)
    que.display()
    que.deq()
    print("\nafter deque\n")
    que.display()

class Stack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1  # stack is empty initially

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow! Cannot push:", value)
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Pushed {value} to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"Popped {value} from stack.")
            return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack from top to bottom:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


# 🔽 Example Usage:
if __name__ == "__main__":
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Top element is:", s.peek())
    s.pop()
    s.display()

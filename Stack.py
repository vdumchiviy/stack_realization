from GeneralStack import GeneralStack


class Stack(GeneralStack):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    stack = Stack()
    print(f"The Stack is empty: {stack.isEmpty()}")

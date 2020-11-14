class GeneralStack():

    def __init__(self):
        self.stack = list()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        """This function checks if stack is empty

        Returns:
            bool: True if it's empty/False if not
        """
        return (self.size() == 0)

    def push(self, item):
        """This function pushes any item to the head of the stack

        Args:
            item (Any): Item to add
        """
        self.stack.append(item)

    def pop(self):
        """This function removes the las item of the stack

        Returns:
            Any: removed a last element of the stack
        """
        if self.size() > 0:
            return self.stack.pop()

    def peek(self):
        """This function returns the last element of the stack

        Returns:
            Any: A last element of the stack
        """
        if self.size() > 0:
            return self.stack[-1]
        return ""


if __name__ == "__main__":
    stack = GeneralStack()
    print(f"The Stack is empty: {stack.isEmpty()}")
    stack.push("1")
    stack.push(1234)
    print(f"The Stack is empty: {stack.isEmpty()}")
    print(f"The size of the stack is: {stack.size()}")
    print(f"The last removed element is {stack.pop()}")
    print(f"The last element is {stack.peek()}")
    print(f"The size of the stack is: {stack.size()}")

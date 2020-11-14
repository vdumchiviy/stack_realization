from GeneralStack import GeneralStack


class Stack(GeneralStack):
    """This class extends class GeneralStack to provide a new method has_balance()
    To initialize you can use some arguments, listed below:

    Args:
        left_rule (str, optional): "Left-handed" list - symbols for open. Defaults to "([{".
        right_rule (str, optional): "Right-handed" list - symbols for clode. Defaults to ")]}".
    """

    def __init__(self, left_rule: str = "([{", right_rule: str = ")]}"):
        super().__init__()
        self.left_rule = left_rule
        self.right_rule = right_rule

    def has_balance(self):
        """This function shows if the Stack is balanced or not

        Returns:
            [bool]: True - The Stack is balanced
                    Flase - The Stack isn't balanced
        """
        if self.size() % 2 != 0:
            return False
        if self.size() == 0:
            return True

        balanced_stack = Stack()
        for x in range(self.size()):
            symb = self.stack[x]
            res_left = self.left_rule.find(symb)
            res_right = self.right_rule.find(symb)
            if res_left != -1:
                balanced_stack.push(symb)
            elif res_right != -1:
                res_bal = self.left_rule.find(balanced_stack.peek())
                if res_bal == res_right:
                    balanced_stack.pop()
                else:
                    return False
            else:
                return False

        if balanced_stack.size() == 0:
            return True

        return False


if __name__ == "__main__":
    stack = Stack()
    print(f"The Stack is empty: {stack.isEmpty()}")
    stack.push("(")
    stack.push("[")
    stack.push(")")
    stack.push("]")
    print(f"The Stack has balance: {stack.has_balance()}")

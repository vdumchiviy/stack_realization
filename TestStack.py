import unittest
from Stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        print(f"setUp: stack size: {self.stack.size()}")

    def tearDown(self):
        print(f"tearDown: stack size: {self.stack.size()}")
        del self.stack

    def test_stack_is_empty(self):
        print("Test if stack is empty")
        expected = True
        actual = self.stack.isEmpty()
        self.assertEqual(actual, expected)

    def test_correct_length_empty_stack(self):
        print("Test correct length of empty stack")
        expected = 0
        actual = self.stack.size()
        self.assertEqual(actual, expected)

    def test_stack_push(self):
        print("Test if stack can add correct items")
        expected = 3
        self.stack.push("test")
        self.stack.push("test")
        self.stack.push("test")
        actual = self.stack.size()
        self.assertEqual(actual, expected)

    def test_stack_peek(self):
        print("Test if stack can get correct item")
        expected = "test"
        self.stack.push("one")
        self.stack.push("two")
        self.stack.push("test")
        actual = self.stack.peek()
        self.assertEqual(actual, expected)

    def test_stack_is_not_empty(self):
        print("Test if stack is NOT empty")
        expected = False
        self.stack.push("test")
        actual = self.stack.isEmpty()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

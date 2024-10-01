import unittest
from main.stack import Stack

class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(0, self.stack.size())

    def test_not_empty_stack(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        size = self.stack.size()
        self.assertEqual(3, size)

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        result = self.stack.pop()
        self.assertEqual(3, result)
        self.assertEqual(2, self.stack.size())

    def test_pop_empty_stack(self):
        #self.assertRaises(Exception, self.stack.pop)
        with self.assertRaises(Exception) as context:
            self.stack.pop()
        self.assertTrue('Empty Stack' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
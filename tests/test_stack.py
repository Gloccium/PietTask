import unittest
from interpreter_components.stack import Stack
from interpreter_components.rotation import Rotation


class TestStack(unittest.TestCase):
    def test_empty_operation(self):
        stack = Stack()
        stack.empty_operation()
        self.assertSequenceEqual(stack._stack, ())

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertSequenceEqual(stack._stack, (1, 2, 3))

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        self.assertSequenceEqual(stack._stack, (1, 2))

    def test_pop_from_empty_stack(self):
        stack = Stack()
        stack.pop()
        stack.push(1)
        stack.pop()
        self.assertSequenceEqual(stack._stack, ())

    def test_add(self):
        stack = Stack()
        stack.push(1)
        stack.add()
        stack.push(2)
        stack.push(3)
        stack.add()
        self.assertSequenceEqual(stack._stack, (1, 5))

    def test_subtract(self):
        stack = Stack()
        stack.push(3)
        stack.subtract()
        stack.push(4)
        stack.subtract()
        stack.push(-5)
        stack.subtract()
        self.assertSequenceEqual(stack._stack, (4,))

    def test_multiply(self):
        stack = Stack()
        stack.push(2)
        stack.multiply()
        stack.push(4)
        stack.multiply()
        stack.push(-5)
        stack.multiply()
        self.assertSequenceEqual(stack._stack, (-40,))

    def test_divide(self):
        stack = Stack()
        stack.push(10)
        stack.divide()
        stack.push(3)
        stack.push(4)
        stack.divide()
        stack.divide()
        stack.push(10)
        stack.divide()
        self.assertSequenceEqual(stack._stack, ())

    def test_mod(self):
        stack = Stack()
        stack.push(10)
        stack.mod()
        stack.push(13)
        stack.mod()
        stack.push(0)
        stack.push(3)
        stack.divide()
        self.assertSequenceEqual(stack._stack, (3,))

    def test_not_operation(self):
        stack = Stack()
        stack.not_operation()
        stack.push(13)
        stack.push(10)
        stack.not_operation()
        stack.push(0)
        stack.not_operation()
        self.assertSequenceEqual(stack._stack, (13, 0, 1))

    def test_greater(self):
        stack = Stack()
        stack.push(3)
        stack.greater()
        stack.push(2)
        stack.greater()
        stack.push(13)
        stack.push(14)
        stack.greater()
        self.assertSequenceEqual(stack._stack, (1, 0))

    def test_pointer(self):
        stack = Stack()
        stack.push(10)
        stack.pointer()
        self.assertEqual(Rotation.LEFT, stack.direction_pointer)
        stack.pointer()
        self.assertEqual(Rotation.LEFT, stack.direction_pointer)
        stack.push(13)
        stack.pointer()
        self.assertEqual(Rotation.UP, stack.direction_pointer)

    def test_switch(self):
        stack = Stack()
        stack.push(5)
        stack.switch()
        self.assertEqual(Rotation.RIGHT, stack.codel_chooser)
        stack.switch()
        self.assertEqual(Rotation.RIGHT, stack.codel_chooser)

    def test_duplicate(self):
        stack = Stack()
        stack.duplicate()
        stack.push(19)
        stack.push(0)
        stack.duplicate()
        self.assertSequenceEqual(stack._stack, (19, 0, 0))

    def test_roll(self):
        stack = Stack()
        stack.duplicate()
        stack.push(5)
        stack.push(5)
        stack.push(3)
        stack.push(2)
        stack.push(5)
        stack.roll()
        self.assertSequenceEqual(stack._stack, (5, 3, 5))

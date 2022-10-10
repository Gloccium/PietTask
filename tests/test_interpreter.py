import unittest
import sys
import io
from os import path
from PIL import Image
from interpreter_components.stack import Stack
from interpreter_components.interpreter import Interpreter


class TestPietInterpreter(unittest.TestCase):
    def test_hello_world(self):
        sys.stdout = io.StringIO()
        stack = Stack()
        with Image.open(
                path.join('test_images', 'HelloWorld.png')).convert('RGB')\
                as image:
            interpreter = Interpreter(stack, image)
            interpreter.start()
        self.assertEqual('Hello world!', sys.stdout.getvalue())

    def test_error_color(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            with Image.open(path.join('test_images', 'ColorError.png')).\
                    convert('RGB') as image:
                interpreter = Interpreter(stack, image)
                interpreter.start()

    def test_white_color(self):
        sys.stdout = io.StringIO()
        stack = Stack()
        with Image.open(path.join('test_images', 'Add.png')).convert('RGB')\
                as image:
            interpreter = Interpreter(stack, image)
            interpreter.start()
        self.assertEqual('4', sys.stdout.getvalue())

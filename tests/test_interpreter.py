import unittest
import sys
import io
from pathlib import Path
from PIL import Image
from interpreter_components.stack import Stack
from interpreter_components.interpreter import Interpreter


class TestPietInterpreter(unittest.TestCase):
    def test_hello_world(self):
        sys.stdout = io.StringIO()
        stack = Stack()
        path = Path(Path.cwd(), 'tests', 'test_images', 'HelloWorld.png')
        with Image.open(path).convert('RGB') as image:
            interpreter = Interpreter(stack, image)
            interpreter.start()
        self.assertEqual('Hello world!', sys.stdout.getvalue())

    def test_error_color(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            path = Path(Path.cwd(), 'tests', 'test_images', 'ColorError.png')
            with Image.open(path).convert('RGB') as image:
                interpreter = Interpreter(stack, image)
                interpreter.start()

    def test_white_color(self):
        sys.stdout = io.StringIO()
        stack = Stack()
        path = Path(Path.cwd(), 'tests', 'test_images', 'Add.png')
        with Image.open(path).convert('RGB') as image:
            interpreter = Interpreter(stack, image)
            interpreter.start()
        self.assertEqual('4', sys.stdout.getvalue())

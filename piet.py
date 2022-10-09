import argparse
from PIL import Image
from interpreter_components.stack import Stack
from interpreter_components.interpreter import Interpreter


def main():
    parser = argparse.ArgumentParser(description='Interprets a specific image')
    parser.add_argument('-f',
                        '--file',
                        required=True,
                        type=str,
                        help='complete path to .png image')
    args = parser.parse_args()
    stack = Stack()
    with Image.open(f'images_to_interpret/{args.file}').convert('RGB')\
            as image:
        interpreter = Interpreter(stack, image)
        interpreter.start()


if __name__ == '__main__':
    main()

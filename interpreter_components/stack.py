from interpreter_components.rotation import Rotation


class Stack:
    def __init__(self):
        self._stack = []
        self.direction_pointer = Rotation.RIGHT
        self.codel_chooser = Rotation.LEFT

    def empty_operation(self):
        return

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if len(self._stack) < 1:
            return
        self._stack.pop()

    def add(self):
        if len(self._stack) < 2:
            return
        x = self._stack.pop()
        y = self._stack.pop()
        self._stack.append(x + y)

    def subtract(self):
        if len(self._stack) < 2:
            return
        x = self._stack.pop()
        y = self._stack.pop()
        self._stack.append(y - x)

    def multiply(self):
        if len(self._stack) < 2:
            return
        x = self._stack.pop()
        y = self._stack.pop()
        self._stack.append(x * y)

    def divide(self):
        if len(self._stack) < 2:
            return
        x = self._stack.pop()
        y = self._stack.pop()
        if y == 0:
            return
        self._stack.append(x // y)

    def mod(self):
        if len(self._stack) < 2:
            return
        x = self._stack.pop()
        y = self._stack.pop()
        if y == 0:
            return
        self._stack.append(x % y)

    def not_operation(self):
        if len(self._stack) < 1:
            return
        value = self._stack.pop()
        if value == 0:
            self._stack.append(1)
        else:
            self._stack.append(0)

    def greater(self):
        if len(self._stack) < 2:
            return
        x = self._stack.pop()
        y = self._stack.pop()
        if y > x:
            self._stack.append(1)
        else:
            self._stack.append(0)

    def pointer(self):
        if len(self._stack) < 1:
            return
        value = self._stack.pop()
        self.direction_pointer = Rotation((self.direction_pointer.value
                                           + value) % 4)

    def switch(self):
        if len(self._stack) < 1:
            return
        value = self._stack.pop()
        self.codel_chooser = Rotation((self.codel_chooser.value
                                       + 2 * value) % 4)

    def duplicate(self):
        if len(self._stack) < 1:
            return
        self._stack.append(self._stack[-1])

    def roll(self):
        if len(self._stack) < 2:
            return
        number = self._stack.pop()
        depth = self._stack.pop()
        number %= depth
        if depth <= 0 or number == 0:
            return
        x = -abs(number) + depth * (number < 0)
        self._stack[-depth:] = self._stack[x:] + self._stack[-depth:x]

    def number_in(self):
        number = int(input('Type in an integer number: '))
        self._stack.append(number)

    def char_in(self):
        char = ord(input('Type in a character: '))
        self._stack.append(char)

    def number_out(self):
        if len(self._stack) < 1:
            return
        value = self._stack.pop()
        print(str(value), end='')

    def char_out(self):
        if len(self._stack) < 1:
            return
        value = self._stack.pop()
        print(chr(value), end='')

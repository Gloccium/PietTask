from interpreter_components.stack import Stack
from interpreter_components.rotation import Rotation
from interpreter_components.colors import *


class Interpreter:
    def __init__(self, stack: Stack, image):
        self.stack = stack
        self.width, self.height = image.size
        self.image = image.load()
        self.blocks = self.get_blocks(self.height, self.width, self.image)
        self.operations =\
             [['empty_operation()',
              'push(len(self.get_block_by_codel(self.previous_codel)))',
               'pop()'],
              ['add()', 'subtract()', 'multiply()'],
              ['divide()', 'mod()', 'not_operation()'],
              ['greater()', 'pointer()', 'switch()'],
              ['duplicate()', 'roll()', 'number_in()'],
              ['char_in()', 'number_out()', 'char_out()']]
        self.previous_codel = None
        self.current_codel = (0, 0)

    def find_block(self, block: list, node: tuple[int, int], pixels, color,
                   size):
        if not (node in block or not (pixels[node] == color)):
            block.append(node)
            x, y = node
            if x > 0:
                self.find_block(block, (x - 1, y), pixels, color, size)
            if x < size[0] - 1:
                self.find_block(block, (x + 1, y), pixels, color, size)
            if y > 0:
                self.find_block(block, (x, y - 1), pixels, color, size)
            if y < size[1] - 1:
                self.find_block(block, (x, y + 1), pixels, color, size)
            return block

    def get_blocks(self, height, width, image):
        blocks = []
        for y in range(height):
            for x in range(width):
                if not self.is_codel_in_blocks((x, y), blocks):
                    if image[x, y] == white:
                        blocks.append([(x, y)])
                    elif image[x, y] not in color_table.keys() and image[x, y]\
                            != black:
                        raise ValueError(f'Invalid color on {x, y}')
                    else:
                        blocks.append(
                            self.find_block([], (x, y), image, image[x, y],
                                            (width, height)))
        return blocks

    @staticmethod
    def is_codel_in_blocks(codel, blocks):
        for block in blocks:
            if codel in block:
                return True
        return False

    def get_block_by_codel(self, codel):
        for block in self.blocks:
            if codel in block:
                return block

    def get_edge(self, direction_pointer, codel_chooser):
        block = self.get_block_by_codel(self.current_codel)
        next_block = block[0]
        for elem in block:
            match (direction_pointer, codel_chooser):
                case (Rotation.RIGHT, Rotation.LEFT) \
                    if elem[0] > next_block[0] or elem[0] == next_block[0]\
                        and elem[1] < next_block[1]:
                    next_block = elem
                case (Rotation.RIGHT, Rotation.RIGHT) \
                    if elem[0] > next_block[0] or elem[0] == next_block[0]\
                       and elem[1] > next_block[1]:
                    next_block = elem
                case (Rotation.DOWN, Rotation.LEFT) \
                    if elem[1] > next_block[1] or elem[1] == next_block[1]\
                       and elem[0] > next_block[0]:
                    next_block = elem
                case (Rotation.DOWN, Rotation.RIGHT) \
                    if elem[1] > next_block[1] or elem[1] == next_block[1]\
                       and elem[0] < next_block[0]:
                    next_block = elem
                case (Rotation.LEFT, Rotation.LEFT) \
                    if elem[0] < next_block[0] or elem[0] == next_block[0]\
                       and elem[1] > next_block[1]:
                    next_block = elem
                case (Rotation.LEFT, Rotation.RIGHT) \
                    if elem[0] < next_block[0] or elem[0] == next_block[0]\
                       and elem[1] < next_block[1]:
                    next_block = elem
                case (Rotation.UP, Rotation.LEFT) \
                    if elem[1] < next_block[1] or elem[1] == next_block[1]\
                       and elem[0] < next_block[0]:
                    next_block = elem
                case (Rotation.UP, Rotation.RIGHT) \
                    if elem[1] < next_block[1] or elem[1] == next_block[1]\
                       and elem[0] > next_block[0]:
                    next_block = elem
        return next_block

    def is_valid_step(self, codel):
        x, y = codel
        return 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1

    def run(self):
        i = 0
        change_codel_chooser = True
        white_codel_path = []
        while i < 8:
            self.previous_codel = self.current_codel
            ex, ey = self.get_edge(self.stack.direction_pointer,
                                   self.stack.codel_chooser)
            match self.stack.direction_pointer:
                case Rotation.UP:
                    temp = (ex, ey - 1)
                case Rotation.LEFT:
                    temp = (ex - 1, ey)
                case Rotation.DOWN:
                    temp = (ex, ey + 1)
                case Rotation.RIGHT:
                    temp = (ex + 1, ey)
            if self.is_valid_step(temp) \
                    and self.image[temp[0], temp[1]] != black:
                self.current_codel = temp
                previous_color = self.image[self.previous_codel]
                current_color = self.image[self.current_codel]
                if current_color != white and previous_color != white:
                    white_codel_path = []
                    hue_difference = color_table[current_color]['hue'] - \
                                     color_table[previous_color]['hue']
                    bright_difference = color_table[current_color][
                                            'brightness'] - \
                                        color_table[previous_color][
                                            'brightness']
                    exec(
                        f'self.'
                        f'stack.'
                        f'{self.operations[hue_difference][bright_difference]}'
                    )
                else:
                    if current_color in white_codel_path:
                        raise ValueError('Infinite white cycle')
                    else:
                        white_codel_path.append(self.current_codel)
                i = 0
            else:
                i += 1
                if change_codel_chooser:
                    self.stack.codel_chooser = \
                        Rotation((self.stack.codel_chooser.value + 2) % 4)
                    change_codel_chooser = False
                else:
                    self.stack.direction_pointer = \
                        Rotation((self.stack.direction_pointer.value + 1) % 4)
                    change_codel_chooser = True

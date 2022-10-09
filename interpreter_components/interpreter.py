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
             [["empty_operation()",
              "push(len(self.get_block_by_codel(self.previous_codel)))",
               "pop()"],
              ["add()", "subtract()", "multiply()"],
              ["divide()", "mod()", "not_operation()"],
              ["greater()", "pointer()", "switch()"],
              ["duplicate()", "roll()", "number_in()"],
              ["char_in()", "number_out()", "char_out()"]]
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
                        raise ValueError(f"Invalid color on {x, y}")
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

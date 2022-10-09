from interpreter_components.rotation import Rotation


class Stack:
    def __init__(self):
        self._stack = []
        self.direction_pointer = Rotation.RIGHT
        self.codel_chooser = Rotation.LEFT

    

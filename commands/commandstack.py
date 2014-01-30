from . import commands_list

__all__ = ['CommandStack']

class CommandStack:
    """
    CommandStack is a simple FIFO Stack implementation used to load commands,
    and handle command callbacks.
    """
    def __init__(self, console):
        self.console = console
        self.in_stack = []
        self.out_stack = []

        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        try:
            return self.out_stack.pop()
        except IndexError:
            pass

    def is_empty(self):
        if self.out_stack:
            return False
        else:
            return True
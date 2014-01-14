from . import commands_list

__all__ = ['CommandStack']

class CommandStack:
    """
    CommandStack is a simple FIFO Stack implementation used to load commands,
    and handle command callbacks.
    """
    def __init__(self, input):
        self.in_stack = []
        self.out_stack = []
        self.args = input.split()    # input will be passed raw to the
                                     # stack - we need to split them up.

        for arg in self.args:
            self.push(arg)

        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
    
        self.curr_command = commands_list[self.out_stack[-1]].callback(self.out_stack[:1])

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        print '[*] debug: popping...'
        return self.out_stack.pop()

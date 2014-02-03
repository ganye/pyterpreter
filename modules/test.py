from base.module import Module
from option import Option

class Test(Module):
    def initialize(self):
        self.update_info({
            'name' : 'Test Module',
            'description' : 'Module used for testing purposes. If you see ' +
                            'this, report it.',
            'license' : 'BSD',
            'author' : ['ganye'],
        })
        self.set_options({
            'test' : Option(True, 'Test variable for debugging purposes.', 
                        'to-be-changed'),
        })

    def run(self):
        self.console.writeln("Everything looks okay...")
        self.console.writeln("Test: %s" % self.test.value)
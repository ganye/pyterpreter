from base.command import Command

class Run(Command):
	def callback(self, *args):
		self.console.module.setup()
		self.console.module.run()

	@staticmethod
	def help():
		return "Execute the currently loaded module."
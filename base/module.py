
class Module:
	info = {}
	options = {}
	help = {}
	def __init__(self, console):
		self.console = console
		self.initialize()

	def initialize(self):
		raise NotImplementedError()

	def setup(self):
		raise NotImplementedError()

	def run(self):
		raise NotImplementedError()

	def update_info(self, info):
		for key, value in info.items():
			self.info[key] = value

	def set_options(self, options):
		for key, value in options.items():
			self.help[key] = value[0]
			if len(value) > 1:
				setattr(self, key, value[1])
			else:
				setattr(self, key, None)

	def set(self, key, value):
		setattr(self, key, value)

	#def help(self):
	#	for key, value in self.help:

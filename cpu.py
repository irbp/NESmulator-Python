class CPU(object):
	def __init__(self):
		self.regs = []

	def instructionDecode(self, instruction: bytes):
		print(instruction)
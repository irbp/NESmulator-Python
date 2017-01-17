from . import cpu

lol = CPU()

def main():
	with open("SMB.nes", 'rb') as file:
		teste = file.readlines()
		lol.instructionDecode(teste[0:2])

if __name__ == '__main__':
	main()
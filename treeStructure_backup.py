from dcString import consoleOutput

class Tree(object):
	def __init__(self, name, parent, children, contents, access, lock):
		self.parent = parent
		self.children = children
		self.name = name
		self.contents = contents
		self.access = access
		self.lock = lock
	
	def who(self):
		return(self.name)
		
	def whoParent(self):
		return(self.parent)
		
	def whoChildren(self):
		return(self.children)
		
	def locContents(self):
		return(self.contents)
		
	def checkAccess(self):
		return(self.access)	
	
	def checkLock(self):
		return(self.lock)


	
	
def whereAmI(currentLoc):
	"Prints current location."
	pause = 0.00
	
	consoleOutput("\n\n", pause)
	consoleOutput("\nYou are in " + currentLoc.who() + ".", pause)
	
	if currentLoc.whoParent() != "":
		consoleOutput("\nParent directory:\n" + currentLoc.whoParent(), pause)
		
	if currentLoc.whoChildren() != "": 
		consoleOutput("\nSubdirectories:\n", pause)
	
	loopLimit = len(currentLoc.whoChildren())
	
	for loop in range(0, loopLimit):
		consoleOutput(currentLoc.whoChildren()[loop], pause)
		consoleOutput(" ", pause)
		
	consoleOutput("\n", pause)
	return 
	
	
def locContents(currentLoc):
	"Show directory contents of current location."
	pause = 0.00

	if currentLoc.whoChildren() != "": 
		consoleOutput("\nSubdirectories:\n", pause)
		loopLimit = len(currentLoc.whoChildren())
		for loop in range(0, loopLimit):
			consoleOutput(currentLoc.whoChildren()[loop], pause)
			consoleOutput(" ", pause)
		consoleOutput("\n")
		
	if currentLoc.locContents() != "":	
		consoleOutput("\nDirectory contains:\n", pause)
		loopLimit = len(currentLoc.locContents())
		for loop in range(0, loopLimit):
			consoleOutput(currentLoc.locContents()[loop], pause)
			consoleOutput(" ", pause)	
		consoleOutput("\n", pause)
	else:
		consoleOutput("\nDirectory empty.")
	return 
	

def displayFile(fileName):
	consoleOutput("\n")
	with open(fileName + ".txt", "r") as file:
		for line in file:
			consoleOutput(line)
	return
	
	
def promptPrint(prompt, promptLength):
	consoleOutput("\n/")
	for loop in range(0, promptLength + 1):
		consoleOutput(prompt[loop])
		consoleOutput("/")
	consoleOutput(">")
	return 
	
def promptAdd(prompt, promptLength, currentLocation):
	promptLength += 1
	prompt[promptLength] = currentLocation.name
	return(prompt, promptLength) 
	
	
def promptSubtract(promptLength):
	promptLength -= 1
	return(promptLength)

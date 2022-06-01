from dcString import consoleOutput

class Tree(object):
	def __init__(self, name, parent, children, contents, ownerAccess, groupAccess, otherAccess, lock):
		self.parent = parent
		self.children = children
		self.name = name
		self.contents = contents
		self.ownerAccess = ownerAccess
		self.groupAccess = groupAccess
		self.otherAccess = otherAccess
		self.lock = lock
		
	def who(self):
		return(self.name)
		
	def whoParent(self):
		return(self.parent)
		
	def whoChildren(self):
		return(self.children)
		
	def locContents(self):
		return(self.contents)

	def otherAccess(self):
		return(self.otherAccess)
				
	def checkLock(self):
		return(self.lock)


def evalAccess(access = 7):
	accessType = 0
	readAccess = 0
	writeAccess = 0
	executeAccess = 0
	read = 4
	write = 2
	execute = 1
	
	if access and read == True:
		accessType = accessType + read
	if access and write == True:
		accessType = accessType + write
	if access and execute == True:
		accessType = accessType + execute
	return(accessType)
	
	
def whereAmI(currentLoc):
	"Prints current location."
	pause = 0.00
	
	consoleOutput("\n\n", pause)
	consoleOutput("\nYou are in " + currentLoc.who() + ".", pause)
	
	if currentLoc.whoParent() != "":
		consoleOutput("\n\nParent directory:\n" + currentLoc.whoParent(), pause)
		
	if currentLoc.whoChildren() != "": 
		consoleOutput("\n\nSubdirectories:\n", pause)
	
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
	skipLine = 1
	consoleOutput("\n")
	with open(fileName + ".txt", "r") as file:
		for line in file:
			if skipLine != 0:
				skipLine -= 1
				if line[2] == "0":
					consoleOutput("Access denied.")
					return(-1)
			else:
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
	
	

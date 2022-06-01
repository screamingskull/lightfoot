def consoleOutput(outputString, pause=0.00):
	"Outputs a given string to the console one character at a time with a pause between each character."
	
	import time

	for loop in range(0, len(outputString)):
		print(outputString[loop], end="", flush=True)
		time.sleep(pause)
	
	return
	
	
def consoleClear():
	"Simply clears the screen by printing new lines."
	print ("\n" * 100)
	
	
def matchList(wordList, wordCount, actionList):
	"Supply word list, word count and an action list. Word list is checked against the action list. First common (matching) string is returned."
	#Check for an action word
	currentWord = 0
	currentAction = 0
	actionWord = ""
	
	while currentWord < wordCount:
		currentAction = 0
		
		while currentAction < len(actionList):

			if actionList[currentAction] == wordList[currentWord]:
				actionWord = actionList[currentAction]
				currentWord = wordCount + 1
			else:	
				currentAction += 1
				
		if actionWord == "":
			currentWord += 1
		else:
			currentWord = wordCount + 1
			
	return(actionWord)
	
	
def breakString(inString):
	"Takes a string input of words (sentence) and chops it up into a list of separate words using space char as delimiter. Returns a list of up to 10 words (minus spaces) and an integer specifying the number of words output (first word being 0)."
	
	inputBuffer = ["", "", "", "", "", "", "", "", "", ""]
	bufferMax = 10
	
	endString = len(inString)
	currPosition = 0
	bufferNo = 0
	
	#Begin input processing
	while currPosition < endString:
		if inString[currPosition] != " ":
			inputBuffer[bufferNo] = inputBuffer[bufferNo] + inString[currPosition]
			currPosition += 1
		else:
			bufferNo += 1
			currPosition += 1
		if bufferNo > bufferMax:
			bufferNo = bufferMax

	return(inputBuffer, bufferNo + 1)

#from treeStructure import Tree, whereAmI, locContents, displayFile, promptPrint, promptAdd, promptSubtract
from treeStructure import *
from dcString import *
from threading import Timer


actionList = ["exit", "quit", "cd", "pwd", "ls", "cat", "help", "clear", "mail", "netstat", "drop", "force"]
recognisedAction = ""
pause = 0.00
prompt = ["", "", "", "", "", "", "", "", "", ""]
promptLength = -1
currentUser = "other"


#Tree objects format: Tree(preferred label, parent directory, [subdirectories list], [files present list], owner access, group access, others access, lock)
recovery = Tree("recovery", "", ["var", "bin", "etc", "home", "tmp"], ["welcome", "readme", "help"], 7, 5, 5, False)
var = Tree("var", "recovery", ["www"], [""], 7, 5, 5, False)
bin = Tree("bin", "recovery", ["tools", "kernel"], [""], 7, 5, 0, False)
etc = Tree("etc", "recovery", ["mail", "net"], [""], 7, 5, 5, False)
mail = Tree("mail", "etc", [""], ["msg001", "msg002"], 7, 5, 5, False)
home = Tree("home", "recovery", ["lightfoot", "jdoe", "ssmith"], [""], 7, 5, 5, False)
tmp = Tree("tmp", "recovery", [""], ["readme_old", "dev_out", "~001tmp"], 7, 5, 5, False)
lightfoot = Tree("lightfoot", "home", [""], [""], 7, 5, 5, False)
jdoe = Tree("jdoe", "home", ["secure"], ["todo"], 7, 5, 5, False)
ssmith = Tree("ssmith", "home", [""], [""], 7, 5, 0, False)
secure = Tree("secure", "jdoe", [""], ["item1", "item2", "item3"], 7, 5, 5, False)
www = Tree("www", "var", ["html"], [""], 7, 5, 5, False)
html = Tree("html", "www", ["intranet"], [""], 7, 5, 5, False)
intranet = Tree("intranet", "html", [""], [""], 7, 5, 5, False)
tools = Tree("tools", "bin", ["hd"], [""], 7, 5, 5, False)
net = Tree("net", "etc", [""], ["live"], 7, 5, 5, False)
#connections = Tree("connections", "net", [""], [""], 7, 5, 5, False)
hd = Tree("hd", "tools", [""], [""], 7, 5, 5, False)
kernel = Tree("kernel", "bin", ["ver7"], [""], 7, 5, 5, False)
ver7 = Tree("ver7", "kernel", [""], [""], 7, 5, 5, False)
hd = Tree("hd", "tools", [""], [""], 7, 5, 5, False)
currentLocation = recovery

prompt, promptLength = promptAdd(prompt, promptLength, currentLocation)


#Set to True to skip intro.
testing = False

if testing != True:
	#Intro
	consoleClear()
	displayFile("welcome")
	consoleOutput("\n\nWelcome to Lightfoot Enterprises")
	consoleOutput("\n", 0.2)
	consoleOutput("\nEnter username: ")
	input()
	consoleOutput("\nEnter password: ")
	input()
	consoleOutput("\nVerifying, please wait")
	consoleOutput(".", 0.2)
	consoleOutput("\n\n*** Too many incorrect logon attempts for user.")
	consoleOutput("\n", 1)
	consoleOutput("\nConsole access will be disabled in ")
	consoleOutput("5.....4.....3.....2.....1.....0", 0.2)
	consoleOutput(" disabling terminal found at /dev/tty2")
	consoleOutput("\n\n", 0.5)
	consoleOutput("\n\n*** An error occurred accessing the file system.")
	consoleOutput("\n*** Dropping you to a shell.")
	consoleOutput("\n*** The system will reboot when you exit the shell.")
	consoleOutput("\n\nGive root password for maintenance:")
	input()
	consoleOutput("\nRead error!")
	consoleOutput("\n\n\n***************")
	consoleOutput("\n Welcome jdoe! ")
	consoleOutput("\n***************")
	consoleOutput("\nType 'help' for a list of available commands.")
	consoleOutput("\n", 2)
	whereAmI(currentLocation)
	# End of intro

#schedAction = Timer(10, print, ("THREAD TIMER!"))
#schedAction.start()


while (recognisedAction != "exit") and (recognisedAction != "quit"):
	objectList = currentLocation.whoChildren()
	parentList = currentLocation.whoParent()
	dirContents = currentLocation.locContents()
	mailDirContents = mail.locContents()
	recognisedObject = ""

	promptPrint(prompt, promptLength)
	
	#Get input and force lowercase.
	userString = str.lower(input())
	
	#Break userString down into words that match a supplied list.
	if userString != "":
		#Break down into separate words.
		wordList, wordCount = breakString(userString)
		
		#Look for action words.
		recognisedAction = matchList(wordList, wordCount, actionList)
		
		#Look for object words.
		recognisedObject = matchList(wordList, wordCount, objectList)
		if recognisedObject != "":
			accessObject = eval(recognisedObject)
			#accessTemp = accessObject.otherAccess
			#accessAllowed = evalAccess(accessTemp)
	
		#Look for parent words.
		recognisedParent = matchList(wordList, wordCount, [parentList])
		
		#Look for file list.
		recognisedFile = matchList(wordList, wordCount, dirContents)
		
		#Look for mail files.
		recognisedMail = matchList(wordList, wordCount, mailDirContents)
		
		
		#Take action based on action words found.
		if (recognisedAction == "cd") and (recognisedObject != ""):
			if accessObject.otherAccess > 0:
				currentLocation = accessObject
				prompt, promptLength = promptAdd(prompt, promptLength, currentLocation)
			else:
				consoleOutput("\nAccess denied.\n")
				
		elif (recognisedAction == "cd") and (recognisedParent != ""):
			currentLocation = eval(recognisedParent)
			promptLength = promptSubtract(promptLength)
			
		elif recognisedAction == "pwd":
			whereAmI(currentLocation)
		elif recognisedAction == "ls":
			locContents(currentLocation)
		elif (recognisedAction == "cat") and (recognisedFile != ""):
			displayFile(recognisedFile)
		elif recognisedAction == "help":
			displayFile("help")
		elif (recognisedAction == "mail") and (recognisedMail == ""):
			locContents(mail)
		elif (recognisedAction == "mail") and (recognisedMail != ""):
			displayFile(recognisedMail)
		elif (recognisedAction == "clear"):
			consoleClear()
		elif (recognisedAction == "force"):
			consoleOutput("\nNot enough privileges.")
			consoleOutput("\nSystem Administrator has been alerted.\n")                        
		elif (recognisedAction == "netstat"):
			displayFile("netstats")
			consoleOutput("\nCheck /etc/net/live for active connections.\n")
		elif (recognisedAction == "drop"):
			consoleOutput("Listing live connections...\n")
			displayFile("live")
			consoleOutput("\nAttempting to drop connection for user")
			consoleOutput(".....", 2)
			consoleOutput("\n*** Error! Unable to drop user.")
			consoleOutput("\n", 2)
			consoleOutput("\n*** WARNING: ")
			consoleOutput("\nSystem Administrator has been alerted.")
			consoleOutput("\n\nYou have new mail.\n")
		else:	
			consoleOutput("\nSyntax error\n")
	
consoleOutput("\n\n*** Signal 15 caught. \n\nBroadcast: Log off NOW! System going down for a reboot immediately...\n\n*** Switching to runlevel 5.")
consoleOutput("\n\n*** Restarting")
consoleOutput("...", 1.5)
consoleClear()

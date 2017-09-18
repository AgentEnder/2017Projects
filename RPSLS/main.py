################################
##rockPaperScissorsLizardSpock##
########Craigory Coppola########
################################

from random import randint
import tkinter as tk

class Application(tk.Frame): #class inherits from frame
	def __init__(self, master=None): #constructor
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		
		#For each widget, it must be created and then placed.
	def createWidgets(self):
		self.outputLabel = tk.Label(self, text = "Make your choice!")
		self.outputLabel.grid(row = 0, columnspan = 5)
		self.aiLabel = tk.Label(self, text = "The AI's choice will show up here")
		self.aiLabel.grid(row = 1, columnspan = 5)
		self.rockButton = tk.Button(self, text = "(1)Rock", command = lambda: self.playRPS(1))
		self.rockButton.grid(row=2,column=0)
		self.paperButton = tk.Button(self, text = "(2)Paper", command = lambda: self.playRPS(2))
		self.paperButton.grid(row=2,column=1)
		self.scissorsButton = tk.Button(self, text = "(3)Scissors", command = lambda: self.playRPS(3))
		self.scissorsButton.grid(row=2,column=2)
		self.scissorsButton = tk.Button(self, text = "(4)Spock", command = lambda: self.playRPS(4))
		self.scissorsButton.grid(row=2,column=3)
		self.scissorsButton = tk.Button(self, text = "(5)Lizard", command = lambda: self.playRPS(5))
		self.scissorsButton.grid(row=2,column=4)
		self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
		self.quitButton.grid(row = 3, columnspan = 5)
	
	def playRPS(self, choice):
		#AI chooses randomly
		aiChoice = randint(1,5)
		#Boolean value for whether or not you win
		win = 0
		if( not(aiChoice == choice)): #If it would not be a tie
			if((aiChoice+choice)%2 == 1): #If it is odd
				if(aiChoice - choice > 0): # is AI choice higher
					win = 0
				else: #Or not
					win = 1
			else: #If not odd
				if(aiChoice - choice > 0): #Is AI choice higher
					win = 1
				else: #or not
					win = 0
			if(win): #You won
				self.outputLabel['text'] = "You won!"
				self.aiLabel['text'] = str(choice) + " beats " + str(aiChoice)
			else: #You lost
				self.outputLabel['text'] = "You Lost!"
				self.aiLabel['text'] = str(aiChoice) + " beats " + str(choice)
		else: #You tied
			self.outputLabel['text'] = "You tied!"
			self.aiLabel['text'] = "You both choose:" + str(choice)
		
app = Application()
app.master.title("Rock, paper, scissors, lizard, spock!")

app.mainloop()
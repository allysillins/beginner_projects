# beginner project from: https://github.com/jorgegonzalez/beginner-projects#magic-8-ball

from tkinter import *
import random

class Magic8Ball:
	def __init__(self, master):
		self.master = master
		master.title("Magic 8 Ball")

		self.label = Label(master, background="yellow",
			 text="Enter your question: ", font=("Roboto",20))
		self.label.grid(row=0,column=0, columnspan=1)

		self.entry = Entry(master, font=("Roboto",20))
		self.entry.grid(row=0,column=1, columnspan=1, sticky=E+W)

		self.ask_button = Button(master, text = "Ask",
			font=("Roboto",14), command = self.respondToAsk)
		self.ask_button.grid(row=2,column=0, sticky=E+W)

		self.clear_button = Button(master, text = "Clear",
			font=("Roboto",14), command = self.clearBox)
		self.clear_button.grid(row=2,column=1, sticky=E+W)

		self.again_button = Button(master, text = "Again",
			font=("Roboto",14), command = self.playAgain)
		self.again_button.grid(row=3,column=0, sticky=E+W)

		self.quit_button = Button(master, text = "Quit",
			font=("Roboto",14), command = master.quit)
		self.quit_button.grid(row=3,column=1, sticky=E+W)

	def respondToAsk(self):
		answers = [
			"Try again later",
			"No",
			"I do not know",
			"Why do you want to know",
			"Yes",
			"Go away",
			"Time will only tell",
		]
		answerLabel = Label(self.master,font=("Roboto",16),
				 text = random.choice(answers))
		answerLabel.grid(row=1,column=0,columnspan=2)

	def playAgain(self):
		self.entry.delete(0,"end")

	def clearBox(self):
		self.entry.delete(0,"end")

root = Tk()
my_magic_8_ball = Magic8Ball(root)
root.mainloop()


"""
Program: GUItemplate.py (page 251)
Author: George 6/2/2022
Template code for all GUI-based applications
GUI based app to simulate the Mega Millions lotter number picks. Five random between 1 and 70 and a "Megal Ball" between 1 and 25
"""
from breezypythongui import EasyFrame
from PIL import ImageTk, Image
from tkinter.font import Font
import random
# other imports

class MegaMill(EasyFrame):

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Mega Mill App", background = "blue")
		font = Font(family = "Verdana", size = 32, weight = "bold",)
		self.addLabel(text = "Mega Millions", row = 0, column = 0, columnspan = 5, foreground = "lemonchiffon", font = font, sticky = "NSEW", background = "limegreen")
		self.addLabel(text = "Winning numbers", row = 1, column = 0, background = "limegreen", foreground = "white")
		self.field1 = self.addIntegerField(value = 0, row = 2, column = 0, state = "readonly")
		self.field2 = self.addIntegerField(value = 0, row = 2, column = 1, state = "readonly")
		self.field3 = self.addIntegerField(value = 0, row = 2, column = 2, state = "readonly")
		self.field4 = self.addIntegerField(value = 0, row = 2, column = 3, state = "readonly")
		self.field5 = self.addIntegerField(value = 0, row = 2, column = 4, state = "readonly")
		self.addLabel(text = "Mega Ball", row = 3, column = 0, background = "limegreen", foreground = "yellow")
		self.megaField = self.addIntegerField(value = 0, row = 4, column = 0, sticky = "NSEW", state = "readonly")
		self.megaField["bg"] = "lemonchiffon"

		self.addButton(text = "Draw Numbers", row = 5, column = 0, columnspan = 5, command = self.compute)

	def compute(self):
		num1 = random.randint(1,70)
		num2 = random.randint(1,70)
		num3 = random.randint(1,70)
		num4 = random.randint(1,70)
		num5 = random.randint(1,70)

		mega = random.randint(1,25)
		
		self.field1.setNumber(num1)
		self.field2.setNumber(num2)
		self.field3.setNumber(num3)
		self.field4.setNumber(num4)
		self.field5.setNumber(num5)

		self.megaField.setNumber(mega)
		

# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	MegaMill().mainloop()

# global call to the main() method
main()

import re
import sys
from random import randint

class Roll():
	def __init__(self, str):
		#3d12+4d6-2d2
		self.str = str.replace(" ", "")
		self.dPos = [_.start() for _ in re.finditer("d", str)]
		self.opPos = [_.start() for _ in re.finditer("[+|-]", str)]

		#If calculation can not be done abort
		if len(self.opPos) + 1 != len(self.dPos):
			print("Error: not matching number of dice and operators!", file=sys.stderr)
			return False

		self.dice = []
		self.setDice()
		self.factor = []
		self.setFactor()

	def setDice(self):
		#Prepare the opPos for simpler arithmetic
		self.opPos.append(len(str))
		#Generate the dice values and save them
		for i in range(len(self.opPos)):
			self.dice.append(int(str[self.dPos[i]+1:self.opPos[i]]))
		#reset
		self.opPos.remove(len(str))

	def setFactor(self):
		#Prepare the opPos for simpler arithmetic
		self.opPos.append(-1)
		self.opPos.sort()

		#Generate the factors and save them
		for i in range(len(self.opPos)):
			start = self.opPos[i]+1
			end = self.dPos[i]
			if start == end:
				self.factor.append(1)
			else:
				self.factor.append(int(str[start:end]))
		#reset
		self.opPos.remove(-1)

	def calculateRoll(self):
		#Calculate the result
		_tmp = 0
		for i in range(len(self.dPos)):
			if i == 0:
				for j in range(self.factor[i]):
					_tmp = _tmp + calculateDice(self.dice[i])
			else:
				for j in range(self.factor[i]):
					if str[self.opPos[i-1]] == "+":
						_tmp = _tmp + calculateDice(self.dice[i])
					else:
						_tmp = _tmp - calculateDice(self.dice[i])
		return _tmp

	def printRoll(self, cached=False):
		res1 = self.calculateRoll()
		res2 = self.calculateRoll()
		if cached == True:
			print(f"Cached {str}: (1){res1} (2){res2}")
		else:
			print(f"{str}: (1){res1} (2){res2}")

def calculateDice(diceSize):
	return randint(1, diceSize)

if __name__ == '__main__':
	rolls = {}
	exit = False
	while not exit:
		str = input(">")
		if str == "exit":
			exit = True
		else:
			#We encountered the string allready hence we use the cached object
			if str in rolls.keys():
				rolls[str].printRoll(cached=True)
			#We did not encountered the string and create a new
			else:
				roll = Roll(str)
				if roll != False:
					rolls[str] = roll
					roll.printRoll()

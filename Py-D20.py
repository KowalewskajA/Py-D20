import re
import sys
from random import randint

class Roll():
	def __init__(self, str):
		self.str = str.replace(" ", "")
		self.dPos = [_.start() for _ in re.finditer("d", str)]
		self.opPos = [_.start() for _ in re.finditer("[+|-]", str)]
		#If calculation can not be done abort
		if len(opPos) + 1 != len(dPos):
			print("Error: not matching number of dice and operators!", file=sys.stderr)
			return False

		self.dice = []
		self.factor = []
		self.opPos.append(len(str))

		#Generate the dice values and save them
		for i in range(len(opPos)):
			dice.append(int(str[dPos[i]+1:opPos[i]]))

		#Prepare the opPos for simpler arithmetic
		opPos.remove(len(str))
		opPos.append(-1)
		opPos.sort()

		#Generate the factors and save them
		for i in range(len(opPos)):
			start = opPos[i]+1
			end = dPos[i]
			if start == end:
				factor.append(1)
			else:
				factor.append(int(str[start:end]))

		opPos.remove(-1)

		#Calculate the result
		_tmp = 0
		for i in range(len(dPos)):
			if i == 0:
				_tmp = factor[i] * calculateDice(dice[i])
			else:
				if str[opPos[i-1]] == "+":
					_tmp = _tmp + factor[i] * calculateDice(dice[i])
				else:
					_tmp = _tmp - factor[i] * calculateDice(dice[i])
		#print(f'opPos[]: {opPos}')
		#print(f'dice[]: {dice}')
		#print(f'factor[]: {factor}')
		return _tmp

def processDiceString(str):
	#3d12+4d6-2d2

	#debug
	#print(f'len(str): {len(str)}')
	#print(f'dPos[]: {dPos}')
	#print(f'opPos[]: {opPos}')


def calculateDice(diceSize):
	return randint(1, diceSize)

if __name__ == '__main__':
	exit = False
	while not exit:
		str = input(">")
		if str == "exit":
			exit = True
		else:
			print(str)
			res1 = processDiceString(str)
			if res1 != False:
				res2 = processDiceString(str)
				print(f"{str}: (1){res1} (2){res2}")

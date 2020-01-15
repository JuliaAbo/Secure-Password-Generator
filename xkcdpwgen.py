#!/usr/bin/env python3

import argparse
import random
from random import randrange, sample 
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--caps", type=int, default=0, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-w", "--words", type=int, default=4,  help="include WORDS words in the password (default=4)")
parser.add_argument("-n", "--numbers", type=int, default=0, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", type=int, default=0, help="insert SYMBOLS random symbols in the password (default=0)")
args = parser.parse_args()


def main(numberOfWords= 4, numberOfCaps= 0, numberOfNumbers= 0, numberOfSymbols=0):
	
	dictionary = "corncob_lowercase.txt"
	wordList =  open(dictionary).read().splitlines()
	symbolsList= ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"] 
	numbersList= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	password = list()
	capitalize = []
	counter = 0
	if numberOfWords <= 0 or  numberOfCaps < 0 or  numberOfNumbers < 0 or numberOfSymbols < 0:
		print("You passed in an illegal argument. You must have at least one word and at least zero caps, numbers and symbols.")
	while numberOfWords > 0 or  numberOfCaps > 0 or numberOfSymbols > 0 or numberOfNumbers > 0: 
		wordCount = numberOfWords 
		while  numberOfWords > 0: 
			password.append(random.choice(wordList))
			numberOfWords = numberOfWords -1
		while  numberOfCaps > 0: 
			indexToCap = random.randint(0,  len(password)-1)
			if numberOfCaps > wordCount: 
				numberOfCaps = wordCount
			if not indexToCap in capitalize: 
				password[indexToCap] = password[indexToCap].capitalize()
				capitalize.append(indexToCap)
				indexToCap = random.randint(0, len(password)-1)
				numberOfCaps = numberOfCaps - 1
			else:
				indexToCap = random.randint(0, len(password)-1)
				
		while  numberOfSymbols > 0: 
			symbolChoice = random.choice(symbolsList)
			password.insert(random.randint(0, len(password)), symbolChoice)
			numberOfSymbols = numberOfSymbols - 1
		while  numberOfNumbers > 0:
			numberChoice = random.choice(numbersList)
			password.insert(random.randint(0, len(password)), numberChoice)
			numberOfNumbers = numberOfNumbers - 1  
	print("".join(password)) 

print(main(args.words, args.caps, args.numbers, args.symbols))
if __name__ == "__main":
	main()

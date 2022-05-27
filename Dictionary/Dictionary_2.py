from PyDictionary import PyDictionary
import sys

dictionary=PyDictionary()

while True:
	exit = input("Would you like to exit? Yes or no. ").lower()
	if(exit == "yes"):
		sys.exit()
	else:
		word = input("Enter word: ")
		print (dictionary.meaning(word))


import csv
import random

def main():
	corpus = readTSV("sentences.csv")
	englishLines = englishOnly(corpus)
	sentLst = getSentences(englishLines)
	sample = random.sample(sentLst, 250000)

	return sample




def readTSV(filepath):
	with open(filepath, "r") as tsv:
		lines = [line.strip().split('\t') for line in tsv]
	return lines

def englishOnly(lines):
	english = []
	for line in lines:
		if line[1].lower() == 'eng':
			english.append(line)
	return english
 
def getSentences(lines):
	return [line[2] for line in lines]

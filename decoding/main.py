def main():
	import clean
	samples = clean.main()
	samples = [sent.decode('utf-8') for sent in samples]
	import vocab
	worddict, wordcount = vocab.build_dictionary(samples)
	vocab.save_dictionary(worddict, wordcount, "dictionary.pkl")
	import os, sys
	sys.path.append("C:/Whitney Masters/Big Data/Project/skip-thoughts")
	import skipthoughts
	model = skipthoughts.load_model()
	encoder = skipthoughts.Encoder(model)
	import train
	train.trainer(samples, samples, model)
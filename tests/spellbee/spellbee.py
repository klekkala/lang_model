'''
Name: Spellbee
Description: Spelling Corrector in Python
Version: 1.0

author: Shivam Bansal
author_email = shivam5992@gmail.com

'''

#! /usr/bin/env python2

try:
	from Levenshtein import *
	from .lookups.myWordNet import myWordNet
except ImportError as IE:
	print(str(IE))

class SpellCheck():

	'''
    Main class for spell checking.
    '''

	def __init__(self):
		self.max_error_length = 15
		self.max_suggestions = 10

	def _clean(self, text):
		''' 
		Cleans a text, handles decoding and encodings, html escaping etc.
		Third party package will be used in future versions.
		'''

		return str(text.strip())

	def _get_threshold(self, text):
		'''
		Decides the threshold for error limit in spellings, 
		depends on length of the word.
		'''
		return 7

	def _checkLevdis(self, query, listname, threshold, isDict):
		'''
		Checks the Levenshtein distance between query and db, 
		and returns the possible suggestions
		'''

		maxRatio = 0
		possibles = []
		possible_val = []
		closest = []
		max_val = 0
		stri = ''
		if isDict:
			for each, value in listname:
				each = str(each)
				if len(each) < self.max_error_length:
					if distance(each, query) < threshold:
						possibles.append(each)
						possible_val.append(value)
						max_list = sorted(range(len(possible_val)), key=lambda x: possible_val[x])[-5:]

		for index in max_list:
			closest.append(possibles[index])
		return closest, possibles, maxRatio

	def _stopwordCheck(self, query, threshold):
		from .lookups.stopwords import stopwords
		if query in stopwords:
			return [query]

	def _correct(self, text):
		''' 
		Checks the input string and gives spelling suggestions as output
		
		:param str text: input text with spelling mistakes
		'''

		string = self._clean(text)
		words = string.split()

		suggestions = []
		for ind, query in enumerate(words):
			corrected = False
			query = query.strip()
			query = query.lower()

			
			closest, possibles, maxRatio = self._checkLevdis(query, iter(myWordNet.items()), 2, True)
			suggestions.append(closest)
			corrected = True

		return suggestions
spellbee = SpellCheck()

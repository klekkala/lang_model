import itertools
import operator
import time
import numpy as np

def opt_search(wordind_list, index_list, val_list, key_list, start_index):

	j = start_index
	print j
	possible = {}

	for i in range(len(wordind_list)):
		while wordind_list[i] > index_list[j]:
			j = j+1

		if wordind_list[i] == index_list[j]:
			possible[key_list[j]] = val_list[j]
	print j
	return possible

def convert_index(word):
	counter = 0
	summer = 0
	alphabets = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
	word_list = list(word)
	word_length = len(word)
	for letter in word_list:
		multiply = pow(26, 10-counter)
		counter = counter+1
		summer = summer + multiply*alphabets[letter]
	return summer


def gen_words(word):

	alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	gen = []
## All possible deletions
	for pos in range(len(word)):
		str_word = word[:pos] + word[(pos+1):]
		gen.append(str_word)

## All possible insertions
	for j in range(len(word)+1):
		insert_comb = [[word[:j]], alphabets, [word[j:]]]
		replace_comb = [[word[:j]], alphabets, [word[j+1:]]]

		insert_possible = list(itertools.product(*insert_comb))
		for each in insert_possible:
			str_word = ''.join(each)
			gen.append(str_word)

		replace_possible = list(itertools.product(*replace_comb))
		for each in replace_possible:
			str_word = ''.join(each)
			gen.append(str_word)

	return gen

input_word = 'optmistc'
word_list = gen_words(input_word)
word_list.sort()

#word_list = ['frugal']
index_dict = {}
val_dict = {}
key_list = []
val_list = []
index_list = []
string_slice = {}
wordind_list = []



w, h = 16, 333300
key_np = [[0 for x in range(w)] for y in range(h)]
val_np = [[0 for x in range(w)] for y in range(h)]
index_np = [[0 for x in range(w)] for y in range(h)]

print "Please wait... Creating dictionary..."
infile = open('list_index.txt', 'r')
index_list = np.load(infile)

infile = open('list_val.txt', 'r')
val_list = np.load(infile)

infile = open('list_key.txt', 'r')
key_list = np.load(infile)


for pos in range(len(key_list)):

	if len(key_list[pos]) <= 16:
		key_np[len(key_list[pos])-1].append(key_list[pos])
		val_np[len(key_list[pos])-1].append(val_list[pos])
		index_np[len(key_list[pos])-1].append(index_list[pos])



	key_val = key_list[pos]
	if key_val[:2] not in string_slice:
			string_slice[key_val[:2]] = pos+1

for val in word_list:
	wordind_list.append(convert_index(val))


print "loading dictioary done."
start_time = time.time()
test_string = word_list[0]
#possibilities = opt_search(wordind_list, index_list[len(input_word)-1], val_list[len(input_word)-1], key_list[len(input_word)-1], string_slice[test_string[:2]])
#possibilities.append(opt_search(wordind_list, index_list, val_list, key_list, string_slice[test_string[:2]]))
print key_np[len(input_word)-1]
#print possibilities

print("--- %s seconds ---" % (time.time() - start_time))
#! /usr/bin/env python2
from spellbee.spellbee import spellbee


if __name__ == '__main__':
        test_sentences = open('eval.txt').readlines()
        iter_string = []
        test_sentences = ['So accustomed was I to his invariable success that the very possibility of his failing had ceased to enter into my hed.']
        for sentence in test_sentences:
        	#print(type(sentence))
            suggestions = spellbee._correct(sentence)
            print(suggestions)
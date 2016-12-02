#! /usr/bin/env python3
# -*- coding: utf-8 -*- 


#! /usr/bin/env python3
import sys
sys.path.append('..')
import unittest
import partition_tree
import sampler
import ngram_model
import utilities
import re
import tokenizer
from spellbee.spellbee import spellbee
import itertools


class LanguagemodelTest():
    def test_corpus_sampling_end_to_end(self):
        filename = 'eval.txt'
        self.run_corpus_trigram_sampling_end_to_end(filename)


    def run_corpus_trigram_sampling_end_to_end(self, filename):
        n=3
        poe_corpus = open(filename)
        poe_document = poe_corpus.read()
        poe_document = poe_document.replace('--', ' -- ')
        preprocessor = utilities.DocumentPreProcessor()
        poe_sentences = preprocessor.preprocess(poe_document)
        poe_sentences = [sentence for sentence in poe_sentences if len(sentence.split('n')) > n]
        
        
        #print(poe_sentences)
        print('Processing {0} sentences'.format(len(poe_sentences)))
        poe_model = utilities.SentenceSamplerUtility(poe_sentences, n)
        samples = [poe_model.get_sample() for i in range(len(poe_sentences))]
        T = tokenizer.Tokenizer()
        tokenized_sequences = T.process(samples)
        #print(tokenized_sequences)

        sequence_tree = ngram_model.NGramFrequencyTree()
        ngram_maker = ngram_model.NGramMaker(n)
        prepared_sequences = [ngram_maker.make_ngrams(s) for s in tokenized_sequences]
        test_seq = [sequence_tree.add_ngram_observation(ngram) for sequence in prepared_sequences for ngram in sequence]
        model = ngram_model.MLEModel(n)
        for split_string in prepared_sequences:
            model.fit(split_string)
        #print(test_seq)
        print("000000")
        #test_sentences = open('eval.txt').readlines()
        iter_string = []
        test_sentences = ['So accustomed was I to his invariable success that the very possibility of his failing had ceased to enter into my hed.']
        for sentence in test_sentences:
            print(sentence)
            #suggestions = spellbee._correct(sentence)
            #sug_list = list(itertools.product(*suggestions))
            #print(sug_list)
            

if __name__ == '__main__':
    lang = LanguagemodelTest()
    lang.test_corpus_sampling_end_to_end()

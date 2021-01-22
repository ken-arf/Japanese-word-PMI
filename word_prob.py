import sys
import os
import numpy as np
import pickle
import argparse
import MeCab
from sklearn.feature_extraction.text import CountVectorizer

lemma = False
tagger = MeCab.Tagger()

def extract_word(text):
    global lemma
    text = ''.join(text.split(' '))
    INDEX_CATEGORY = 0
    INDEX_ROOT_FORM = 6
    TARGET_CATEGORIES = ["名詞", "動詞",  "助詞", "助動詞", "形容詞", "副詞", "連体詞", "感動詞"]
    
    words = []
    node = tagger.parseToNode(text)
    while node:
        features = node.feature.split(',')
        if features[INDEX_CATEGORY] in TARGET_CATEGORIES:
            if lemma:
                if features[INDEX_ROOT_FORM] == "*":
                    words.append(node.surface)
                else:
                    words.append(features[INDEX_ROOT_FORM])
            else:
                words.append(node.surface)
        node = node.next
    
    return words

def main():
    global lemma
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='corpus', help='corpus file path', required=True)
    parser.add_argument('-o', dest='output', help='output file path', required=True)
    parser.add_argument('-n', dest='numvocab', help='maximum vocabulary size', required=True)
    parser.add_argument('-lemma', dest='lemma', action='store_true', help='apply lemmatization for text')

    args = parser.parse_args()

    tagger = MeCab.Tagger()
    infile = args.corpus 
    t = []
    with open(infile) as fp:
        for l in fp:
            t.append(l.strip())

    lemma = args.lemma
    n = int(args.numvocab)
    vectorizer = CountVectorizer(analyzer=extract_word, max_features=n)
    X = vectorizer.fit_transform(t)

    pxy = X.transpose().dot(X)
    pxy = pxy / np.sum(pxy) 
    px = np.sum(X, axis=0) 
    px = px / np.sum(px) 

    vocab = vectorizer.get_feature_names()

    pmi={}
    pmi['pxy']=pxy
    pmi['px']=px
    pmi['vocab']=vocab
   
    with open(args.output, 'wb') as fp:
        pickle.dump(pmi, fp)

if __name__ == '__main__':
  main()

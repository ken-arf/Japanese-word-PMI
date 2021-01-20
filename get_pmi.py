import sys
import os
import argparse
import pickle
import numpy as np


def comp_pmi(args, vocab, px, pxy):
    eps = 1e-10
    try:
        ind1 = vocab.index(args.w1)
    except:
        print('{} not found'.format(args.w1))
        exit()
    try:
        ind2 = vocab.index(args.w2)
    except:
        print('{} not found'.format(args.w2))
        exit()

    px1 = px[0,ind1] + 1e-10 
    px2 = px[0,ind2] + 1e-10

    
    if pxy[ind1, ind2] > 0:
        pmi = np.log((pxy[ind1, ind2])/(px1*px2))
    else:
        pmi = np.log(eps)
        
    print('p({}):{}'.format(args.w1, px1))
    print('p({}):{}'.format(args.w2, px2))
    print('p({},{}):{}'.format(args.w1, args.w2, pxy[ind1,ind2]))
    print('PMI:{}, {}:{}'.format(pmi, args.w1, args.w2))

def get_top_words(args, vocab, px, pxy):
    eps = 1e-10
    try:
        ind1 = vocab.index(args.w1)
    except:
        print('{} not found'.format(args.w1))
        exit()
    topn = int(args.top)

    pmis = []
    px1 = px[0, ind1]

    for ind2 in range(px.shape[1]):
        px2 = px[0, ind2]
        pxy_ = pxy[ind1, ind2]
        
        if pxy[ind1, ind2] > 0:
            pmi = np.log((pxy[ind1, ind2])/(px1*px2))
        else:
            pmi = np.log(eps)
        pmis.append(pmi)

    indices = np.argsort(pmis)
    indices = indices[::-1]

    for i in range(topn):
        ind = indices[i]
        print('TOP {}: PMI={}\t{}'.format(i, pmis[ind], vocab[ind]))


def process(args, vocab, px, pxy):
    if args.w1 and args.w2:
        comp_pmi(args, vocab, px, pxy)
    elif args.w1 and args.top:
        get_top_words(args, vocab, px, pxy)
    else:
        print('param error')
        exit(0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='data', help='word prob data file path')
    parser.add_argument('-w1', dest='w1', help='first word')
    parser.add_argument('-w2', dest='w2', help='second word')
    parser.add_argument('-top', dest='top', help='top n words')

    args = parser.parse_args()

    data = args.data

    with open(data, 'rb') as fp:
        d = pickle.load(fp)

    vocab = d['vocab']
    px = d['px']
    pxy = d['pxy']

    process(args, vocab, px, pxy)

if __name__ == '__main__':
  main()


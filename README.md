# Japanse-word-PMI

Calculate word probabilities and word co-occurrence probabilities from the corpus.  
The corpus file must consist of one sentence per line

python word_prob.py -c corpus.txt -n 10000 -lemma

=> prob_data.pkl will be generated


Calculate the PMI between word pairs or between the top n words with the highest word PMI

python get_pmi.py -w1 夏 -w2 海 -d prob_data.pkl

p(夏):0.00011126743494502381  
p(海):7.908266863861197e-05  
p(夏,海):1.554080211954162e-08  
PMI:0.5687938678640507, 夏:海


python get_pmi.py -w1 夏 -top 10 -d prob_data.pkl

TOP 0: PMI=6.148931201400956    夏  
TOP 1: PMI=4.686671090732668    冷房  
TOP 2: PMI=4.617678219245717    食中毒  
TOP 3: PMI=4.5123177035878905   日向  
TOP 4: PMI=4.435356662451762    涼しい  
TOP 5: PMI=4.430079605350919    暑い  
TOP 6: PMI=4.3299961467939365   夜空  
TOP 7: PMI=4.084873688760951    暑  
TOP 8: PMI=4.042314074342156    ひととき  
TOP 9: PMI=3.965022400040509    祭り  



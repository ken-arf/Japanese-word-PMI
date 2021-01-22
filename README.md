# Japanese-word-PMI

Calculate word probabilities and word co-occurrence probabilities from the corpus.  
The corpus file must consist of one sentence per line.  
If two words exist in the same sentence, they are deemed as a co-occurrence.  

コーパスから単語の確率と単語の共起確率を計算します。  
コーパスファイルは、1行に1つの文で構成されている必要があります。  
同じ文内に二つの単語が存在すれば共起としています．　

python word_prob.py -c corpus.txt -n 10000 -lemma

=> prob_data.pkl will be generated


Calculate the PMI between word pairs or get top n words with the highest word PMI

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

Get the most likely adjectives to co-occur with 夏 

python get_pmi.py -d prob_data.pkl -w1 夏 -top 60 | cut -f2 | mecab | grep -P "\t形容詞"

涼しい  形容詞,自立,*,*,形容詞・イ段,基本形,涼しい,スズシイ,スズシイ  
暑い    形容詞,自立,*,*,形容詞・アウオ段,基本形,暑い,アツイ,アツイ 
暑      形容詞,自立,*,*,形容詞・アウオ段,ガル接続,暑い,アツ,アツ  
涼しく  形容詞,自立,*,*,形容詞・イ段,連用テ接続,涼しい,スズシク,スズシク  
冷たい  形容詞,自立,*,*,形容詞・アウオ段,基本形,冷たい,ツメタイ,ツメタイ  

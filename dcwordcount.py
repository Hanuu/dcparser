import codecs
from konlpy.tag import Twitter
import timeit

start = timeit.default_timer()

fp = codecs.open("20180111-203502_100000p.csv", "r", encoding="utf8")
print(fp[0])
twitter = Twitter()
word_dic = {}
lines = fp
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == "Noun": #  명사 확인하기 --- (※3)
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 카운트하기
# 많이 사용된 명사 출력하기 --- (※4)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()

stop = timeit.default_timer()
print (stop - start)

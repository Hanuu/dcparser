from konlpy.tag import Twitter
import timeit

start = timeit.default_timer()

twitter=Twitter()
malist=twitter.pos("비트코인 이더리움 이더 리플 가즈아 슨트", norm=True,stem=True)
print(malist)

malist=twitter.pos("줘못먹보고 흑우흑우 하던데 왜 흑우임?", norm=True,stem=True)
print(malist)

malist=twitter.pos("심상치 않다 심창치않다 거침없다", norm=True,stem=True)
print(malist)

malist=twitter.pos("빗파 13800달러 공매도 비트 1000개 삭제됐다. 떡상 뚫렸다 ㄱㄱㄱ", norm=True,stem=True)
print(malist)

malist=twitter.pos("떡락 가즈아ㅏㅏ", norm=True,stem=True)
print(malist)

malist=twitter.pos("떡상 가즈아ㅏㅏㅏ", norm=True,stem=True)
print(malist)

malist=twitter.pos("떡상이냐 떡락이냐", norm=True,stem=True)
print(malist)

malist=twitter.pos("존버", norm=True,stem=True)
print(malist)

malist=twitter.pos("업비트 업빗 코인원 빗썸 폴로닉스 빗파", norm=True,stem=True)
print(malist)

malist=twitter.pos("빗갤럼새끼들 빗갤러 빗갤", norm=True,stem=True)
print(malist)




stop = timeit.default_timer()
print (stop - start)

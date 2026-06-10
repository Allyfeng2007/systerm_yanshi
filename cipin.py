import jieba

class WordFreq:
    def word_freq(self, text):
        with open("sucai/chinese_stopwords.txt") as f2:
            stop_words = f2.read().split('\n') + ['\n']

        lst = jieba.cut(text.strip())

        freq = {}
        for word in lst:
            if len(word) == 1:
                continue
            if word not in stop_words:
                freq[word] = freq.get(word, 0) + 1
        lst_sort = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return lst_sort



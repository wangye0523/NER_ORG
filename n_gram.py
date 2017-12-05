from word2gm_loader import Word2GM
import numpy as np


class Predictor:
    def __init__(self, p, n=15):
        self.model = Word2GM(p)
        self.ngram = n
        self.vocab = self.model.word2id.keys()
        self.stopwords = self.load_stopwords()
        self.query = None

    def load_stopwords(self):
        w = []
        with open('data/stopwords.txt', 'r') as f:
            for i in f:
                w+=[i.strip()]
        return w

    def get_neightbours(self, w, context):
        c = context.split(' ')
        c = [x for x in c if (x in self.vocab or x == w) and x not in self.stopwords]
        t = int(self.ngram/2)
        ind = [x for x in range(len(c)) if c[x]==w]
        res = []
        for i in ind:
            for j in range(max(0, i-t), min(i+t+1, len(c))):
                if j != i and c[j]:
                    res += [c[j]]
        return res

    def get_context(self, w, context):
        self.query = w
        c = context.split(' ')
        c = [x for x in c if (x in self.vocab or x == w) and x not in self.stopwords]
        return c

    def get_clusters(self, w, context):
        a = self.get_neightbours(w, context)
        res = []
        for i, word in enumerate(a):
            if word != w:
                res += [(word, self.model.find_best_cluster(self.model.word2id[word], [self.model.word2id[x] for x in a if x != w]))]
            else:
                res += [(word, -1)]
        return res

    def get_centroid(self, w, context):
        a = self.get_clusters(w, context)
        tmp = []
        for i in a:
            tmp += []


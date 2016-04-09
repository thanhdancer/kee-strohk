from sklearn.feature_extraction.text import CountVectorizer
from operator import itemgetter, attrgetter, methodcaller
import pandas
import numpy

class ProcessKeystrokeData:
    def __init__(self, filename):
        self.data = pandas.DataFrame.from_csv(filename, sep=', ', index_col=None)
        print self.data
        self.data['char_'] = self.data['char'].apply(self._convert_char)
        self.data1 = self.data[self.data['char'] < 127]
        self.data1 = self.data1[self.data1['char'] > 31]
        self.post = ''.join(self.data1['char_']).lower()
        self.wordlist = self.post.split(' ')

    def _convert_char(self, code):
        special_char = {0: 'NUL',  1: 'SOH',  2: 'STX',  3: 'ETX',  4: 'EOT',  5: 'ENQ',
        6: 'ACK',  7: 'BEL',  8: 'BS',  9: 'HT',  10: 'LF',  11: 'VT',  12: 'FF',
        13: 'CR',  14: 'SO',  15: 'SI',  16: 'DLE',  17: 'DC1',  18: 'DC2',
        19: 'DC3',  20: 'DC4',  21: 'NAK',  22: 'SYN',  23: 'ETB',  24: 'CAN',
        25: 'EM',  26: 'SUB',  27: 'ESC',  28: 'FS',  29: 'GS',  30: 'RS',  31: 'US'}
        if code < 32:
            return special_char[code]
        else:
            return chr(code)

    def export_wordlist(self):
        return list(set(self.wordlist))

    def export_wordcount(self):
        vectorizer = CountVectorizer(analyzer='word', min_df=1e-4, max_df=1.0)
        X = vectorizer.fit_transform(self.wordlist)
        X = X.T.sum(axis=1).T
        X = numpy.asarray(X)[0]
        features = vectorizer.get_feature_names()
        total = len(X)

        decorated = []
        for i in xrange(total):
            decorated.append((X[i], features[i]))

        return sorted(decorated, key=itemgetter(0), reverse=True)

    def export_ngram(self, n=2):
        vectorizer = CountVectorizer(analyzer='char', ngram_range=(n,n), min_df=1e-4, max_df=1.0)
        X = vectorizer.fit_transform(self.wordlist)
        X = X.T.sum(axis=1).T
        X = numpy.asarray(X)[0]
        features = vectorizer.get_feature_names()
        total = len(X)

        decorated = []
        for i in xrange(total):
            decorated.append((X[i], features[i]))

        return sorted(decorated, key=itemgetter(0), reverse=True)

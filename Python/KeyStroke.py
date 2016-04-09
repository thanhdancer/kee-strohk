import pandas
import sys

# read file
words = pandas.DataFrame.from_csv('word_count.txt', index_col=None)
chars = pandas.DataFrame.from_csv('1gram.txt', index_col=None)
bigrams = pandas.DataFrame.from_csv('2gram.txt', index_col=None)
data = pandas.DataFrame.from_csv(sys.argv[1], index_col=None)
number_of_column = 200

#calculate F1:
F1 = data['KeyCode']
F1 = pandas.DataFrame(F1, columns=['KeyCode'])
F1['duration'] = data['KeyUp'] - data['KeyDown']
F1['delay'] = 0
F1['name'] = sys.argv[1].split('.')[0]

#calculate F2, F3:
list2 = data.values.T.tolist()
length = len(list2[0])

for i in xrange(length):
	if i != 0:
		F1.set_value(i,'delay',list2[1][i] - list2[2][i-1])

F1.to_csv('Feature_%s' % sys.argv[1], index=False)

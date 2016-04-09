# read file
chars = pandas.DataFrame.from_csv('1gram.txt', index_col=None)
bigrams = pandas.DataFrame.from_csv('2gram.txt', index_col=None)
data = pandas.DataFrame.from_csv('hien.txt', index_col=None)

#calculate F1:
data1 = data[data['KeyCode']>32]
data1 = data1[data1['KeyCode']<127]

F1 = data1['KeyCode']
F1 = pandas.DataFrame(F1, columns=['KeyCode'])
F1['duration'] = data1['KeyUp'] - data1['KeyDown']
F1 = F1.groupby('KeyCode', as_index=False).mean()
F1['KeyCode'] = F1['KeyCode'].map(chr)
F1.to_csv('F1.txt', index=False)

#calculate F2, F3:
data2 = data[data['KeyCode']>32]
data2 = data2[data2['KeyCode']<127]
data2['KeyCode'] = data2['KeyCode'].map(chr)

list2 = data2.values.T.tolist()
length = len(list2[0])

F2 = bigrams['value']
F2 = pandas.DataFrame(F2, columns=['value'])
F2['Count'] = 0
F2['Sum'] = 0

F3 = bigrams['value']
F3 = pandas.DataFrame(F3, columns=['value'])
F3['Count'] = 0
F3['Sum'] = 0

for i in xrange(length-1):
	str = list2[0][i] + list2[0][i+1]
	str = str.lower()
	if len(F2[F2['value']==str]) != 0:
		index = F2[F2['value']==str].index[0]
		valF2 = list2[1][i+1] - list2[2][i]
		valF3 = list2[1][i+1] - list2[1][i]
		F2.set_value(index,'Count',F2[F2['value']==str]['Count'] + 1)
		F2.set_value(index,'Sum',F2[F2['value']==str]['Sum'] + valF2)
		F3.set_value(index,'Count',F3[F3['value']==str]['Count'] + 1)
		F3.set_value(index,'Sum',F3[F3['value']==str]['Sum'] + valF3)

F2['duration'] = F2['Sum']/F2['Count']
F3['duration'] = F3['Sum']/F3['Count']

F2.__delitem__('Count')
F2.__delitem__('Sum')
F3.__delitem__('Count')
F3.__delitem__('Sum')

F2.to_csv('F2.txt', index=False)
F3.to_csv('F3.txt', index=False)

#calculate F4
data4['KeyCode'] = data['KeyCode'].map(chr)

list4 = data4.values.T.tolist()
length = len(list4[0])

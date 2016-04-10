import pandas
import sys

# read file
words = pandas.DataFrame.from_csv('word_count.txt', index_col=None)
chars = pandas.DataFrame.from_csv('1gram.txt', index_col=None)
bigrams = pandas.DataFrame.from_csv('2gram.txt', index_col=None)
data = pandas.DataFrame.from_csv(sys.argv[1], index_col=None)
raw = pandas.DataFrame.from_csv(sys.argv[1], index_col=None)

#calculate F1:
F1 = data['KeyCode']
F1 = pandas.DataFrame(F1, columns=['KeyCode'])
F1['duration'] = data['KeyUp'] - data['KeyDown']
F1['delay'] = 0
F1['name'] = sys.argv[1].split('.')[0]

#calculate F2, F3:
listHai = data.values.T.tolist()
length = len(listHai[0])

for index1 in xrange(length):
	if index1 != 0:
		F1.set_value(index1,'delay',listHai[1][index1] - listHai[2][index1-1])

# Code from Cong Lua To
backSpaceKeyCode =8
shiftKeyCode = 16
count = 0
flag = False
i = 0
list0 = raw['KeyCode'].values.tolist()
myDict = {}
misWords = [0] * len(list0)

while i < len(list0):
    if list0[i] == backSpaceKeyCode:
        flag = True
        key = i
        count = count +1
        while flag == True and i < len(list0) -1:
            i = i+1
            if list0[i] == backSpaceKeyCode:
                count = count +1
            else:
                myDict[key] = count
                flag = False
                count = 0
    else:
        count = 0
    i = i+1

listValue = myDict.values()
listKey = myDict.keys()
indexOfMiswordArray = 0;
indexOdReplace = 0
list1 = list0
for hihi in range(len(list1)):
    if list0[hihi] == backSpaceKeyCode:
        list1[hihi] = None

# get all delete record
for iDict in range(len(myDict)):
    number = 0
    index = 0
    while number < listValue[iDict] and listKey[iDict] - index >0 :
        index +=1
        if list1[listKey[iDict] - index] != None:
            number+=1
            if listKey[iDict] - index -1 >0 and list1[listKey[iDict] - index - 1] == shiftKeyCode:
                misWords[listKey[iDict] - index - 1] =1
                list1[listKey[iDict] - index - 1]  = None
            misWords[listKey[iDict] - index] = 1
            list1[listKey[iDict] - index] = None


# get all replace record
for iDict in range(len(myDict)):
    number = 0
    index = 0
    while number < listValue[iDict] and listKey[iDict] + index < len(list0) :
        index +=1
        if list1[listKey[iDict] + index] != None:
            number+=1
            misWords[listKey[iDict] + index] = 1;
            if listKey[iDict] + index +1 <len(list0) and list1[listKey[iDict] + index] == shiftKeyCode:
                misWords[listKey[iDict] + index +1] =1;
                list1[listKey[iDict] + index +1] = None
            list1[listKey[iDict] + index ] = None

dataFrame = pandas.DataFrame(misWords, index=None, columns=['misWords'])
F1['misWords'] = dataFrame.as_matrix()
F1['name'] = sys.argv[1].split('.')[0]
F1.to_csv('Feature_%s' % sys.argv[1], index=False)

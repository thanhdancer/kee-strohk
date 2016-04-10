import pandas 
import numpy
raw = pandas.read_csv('hien.txt',index_col = None,header=None)
backSpaceKeyCode =8
shiftKeyCode = 16
count = 0
flag = False
i = 0
list0 = raw[0].values.tolist()
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

DataFrame = pandas.DataFrame(misWords, index=None)
DataFrame.to_csv("featureMistakeWord.txt",index=False)
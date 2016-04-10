import pandas


class FeatureExtraction:
    def __init__(self, data, total_records=26):
        # read file
        self.data = pandas.DataFrame.from_csv(data, index_col=None)
        self.raw = pandas.DataFrame.from_csv(data, index_col=None)
        self.number_of_column = total_records

    def _calcualte_f1(self):
        # calculate F1:

        F1 = self.data['KeyCode']
        F1 = pandas.DataFrame(F1, columns=['KeyCode'])
        F1['duration'] = self.data['KeyUp'] - self.data['KeyDown']
        F1['delay'] = 0

        listHai = self.data.values.T.tolist()
        length = len(listHai[0])

        for index1 in xrange(length):
            if index1 != 0:
                F1.set_value(index1, 'delay', listHai[1][index1] - listHai[2][index1 - 1])

        return F1
        # F1.to_csv('F1.txt', index=False)

    def _calculate_f2_f3(self):
        # calculate F2, F3:
        data2 = self.data[self.data['KeyCode'] > 32]
        data2 = data2[data2['KeyCode'] < 127]
        data2['KeyCode'] = data2['KeyCode'].map(chr)

        list2 = data2.values.T.tolist()
        length = len(list2[0])

        F2 = self.bigrams['value']
        F2 = pandas.DataFrame(F2, columns=['value'])
        F2['Count'] = 0
        F2['Sum'] = 0
        F2 = F2.head(self.number_of_column)

        F3 = self.bigrams['value']
        F3 = pandas.DataFrame(F3, columns=['value'])
        F3['Count'] = 0
        F3['Sum'] = 0
        F3 = F3.head(self.number_of_column)

        for i in xrange(length - 1):
            str = list2[0][i] + list2[0][i + 1]
            str = str.lower()
            if len(F2[F2['value'] == str]) != 0:
                index = F2[F2['value'] == str].index[0]
                valF2 = list2[1][i + 1] - list2[2][i]
                valF3 = list2[1][i + 1] - list2[1][i]
                F2.set_value(index, 'Count', F2[F2['value'] == str]['Count'] + 1)
                F2.set_value(index, 'Sum', F2[F2['value'] == str]['Sum'] + valF2)
                F3.set_value(index, 'Count', F3[F3['value'] == str]['Count'] + 1)
                F3.set_value(index, 'Sum', F3[F3['value'] == str]['Sum'] + valF3)

        F2['duration'] = F2['Sum'] / F2['Count']
        F3['duration'] = F3['Sum'] / F3['Count']

        F2.__delitem__('Count')
        F2.__delitem__('Sum')
        F3.__delitem__('Count')
        F3.__delitem__('Sum')

        F2.set_value(F2[F2['duration'].isnull()].index, 'duration', 0)
        F3.set_value(F3[F3['duration'].isnull()].index, 'duration', 0)

        return F2, F3
        # F2.to_csv('F2.txt', index=False)
        # F3.to_csv('F3.txt', index=False)

    def _calculate_f4(self):
        # calculate F4
        data4 = self.data['KeyCode']
        data4 = pandas.DataFrame(data4, columns=['KeyCode'])
        data4['KeyDown'] = self.data['KeyDown']
        data4['KeyUp'] = self.data['KeyUp']

        F4 = self.words['value']
        F4 = pandas.DataFrame(F4, columns=['value'])
        F4['Count'] = 0
        F4['Sum'] = 0
        F4 = F4.head(self.number_of_column)

        list4 = data4.values.T.tolist()
        length = len(list4[0])
        str = ''
        begin = 0
        finish = 0
        for i in xrange(length):
            if (list4[0][i] >= 65 and list4[0][i] <= 90) or (list4[0][i] >= 97 and list4[0][i] <= 122):
                if str != '':
                    begin = list4[1][i]
                str = str + chr(list4[0][i])
                finish = list4[2][i]
            else:
                str = str.lower()
                if len(F4[F4['value'] == str]) != 0:
                    index = F4[F4['value'] == str].index[0]
                    valF4 = finish - begin
                    F4.set_value(index, 'Count', F4[F4['value'] == str]['Count'] + 1)
                    F4.set_value(index, 'Sum', F4[F4['value'] == str]['Sum'] + valF4)
                str = ''
                begin = 0
                finish = 0

        F4['duration'] = F4['Sum'] / F4['Count']
        F4.__delitem__('Count')
        F4.__delitem__('Sum')
        F4.set_value(F4[F4['duration'].isnull()].index, 'duration', 0)
        return F4
        # F4.to_csv('F4.txt', index=False)

    def _calculate_mis_word(self):
        backSpaceKeyCode = 8
        shiftKeyCode = 16
        count = 0
        flag = False
        i = 0
        list0 = self.raw['KeyCode'].values.tolist()
        myDict = {}
        misWords = [0] * len(list0)

        while i < len(list0):
            if list0[i] == backSpaceKeyCode:
                flag = True
                key = i
                count = count + 1
                while flag == True and i < len(list0) - 1:
                    i = i + 1
                    if list0[i] == backSpaceKeyCode:
                        count = count + 1
                    else:
                        myDict[key] = count
                        flag = False
                        count = 0
            else:
                count = 0
            i += 1

        listValue = myDict.values()
        listKey = myDict.keys()
        indexOfMiswordArray = 0
        indexOdReplace = 0
        list1 = list0
        for hihi in range(len(list1)):
            if list0[hihi] == backSpaceKeyCode:
                list1[hihi] = None

        # get all delete record
        for iDict in range(len(myDict)):
            number = 0
            index = 0
            while number < listValue[iDict] and listKey[iDict] - index > 0:
                index += 1
                if list1[listKey[iDict] - index] != None:
                    number += 1
                    if listKey[iDict] - index - 1 > 0 and list1[listKey[iDict] - index - 1] == shiftKeyCode:
                        misWords[listKey[iDict] - index - 1] = 1
                        list1[listKey[iDict] - index - 1] = None
                    misWords[listKey[iDict] - index] = 1
                    list1[listKey[iDict] - index] = None

        # get all replace record
        for iDict in range(len(myDict)):
            number = 0
            index = 0
            while number < listValue[iDict] and listKey[iDict] + index < len(list0):
                index += 1
                if list1[listKey[iDict] + index] != None:
                    number += 1
                    misWords[listKey[iDict] + index] = 1;
                    if listKey[iDict] + index + 1 < len(list0) and list1[listKey[iDict] + index] == shiftKeyCode:
                        misWords[listKey[iDict] + index + 1] = 1;
                        list1[listKey[iDict] + index + 1] = None
                    list1[listKey[iDict] + index] = None

        return misWords

    def get_features(self):
        feature_frame = self._calcualte_f1()
        mis_words = pandas.DataFrame(self._calculate_mis_word(), index=None, columns=['misWords'])
        print feature_frame
        print mis_words
        feature_frame['misWords'] = mis_words.as_matrix()
        return feature_frame

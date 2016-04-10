from sklearn.ensemble import RandomForestClassifier

import pandas

class Prediction:
    def __init__(self, preprocessed_data):
        self.processed_data = preprocessed_data
        self.top_frequency = self.processed_data['KeyCode'].value_counts().head(20).index.values.tolist()



    def training(self, name, path):
        X = {}
        for character in top_frequency:
            X[character] = self.processed_data[['duration', 'delay']][self.processed_data['KeyCode'] == i].as_matrix()
        
        clf = RandomForestClassifier()
        pass

    def test(self):
        pass

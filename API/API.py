from flask import Flask
from pymongo import MongoClient
from library.feature_extraction import FeatureExtraction
app = Flask(__name__)

@app.route('/user_detection')
def user_detection():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

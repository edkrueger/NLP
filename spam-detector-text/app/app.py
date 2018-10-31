from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pickle

def formatter(s):
    return re.sub(r"\d+", "", s).lower()

def splitter(s):
    return re.compile(r"(?u)\b\w\w+\b").findall(s)

def clean_tokenizer(s):
    return  splitter(formatter(s))

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

	text = list(set(request.form))[0]
	array = [text]
	predicted_label = clf.predict(array)[0]

	return jsonify(predicted_label)

if __name__ == '__main__':
	
	clf = joblib.load("spam_detector.joblib")
	
	app.run()
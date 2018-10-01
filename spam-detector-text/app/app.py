from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

	text = list(set(request.form))[0]
	array = [text]
	predicted_label = clf.predict(array)[0]

	return jsonify(predicted_label)

if __name__ == '__main__':
	clf = joblib.load("spam_detector.pkl")
	app.run()
import flask
import requests

API_URL = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-fake-news-detection"
API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({"inputs": "I like you. I love you"})

##############################################################################################
#
#   FLASK APP
#
##############################################################################################

# The flask app for serving predictions
application = flask.Flask(__name__)

@application.route('/')
def hello():
    return "Welcome to your own Sentiment Analysis Tool"

@application.route('/fakenews', methods=['GET'])
def fakenews():
    data = None

    if flask.request.content_type == 'application/json':
        data = flask.request.get_json()
    else:
        return flask.Response(response='This predictor only supports Json data', status=415, mimetype='text/plain')
    
    model_resp = query({'inputs': data.get('text') or 'Sample text'})[0]
    real_prob, fake_prob = model_resp[0]['score'], model_resp[1]['score']
    
    result = ""
    if real_prob >= fake_prob:
        result = {
            "message": "Real news. Probability: {}%".format(real_prob*100),
            "result": 0
        }
    else:
        result = {
            "message": "Fake news. Probability: {}%".format(fake_prob*100),
            "result": 1
        }
    response = flask.make_response(flask.jsonify(result), 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    application.run()

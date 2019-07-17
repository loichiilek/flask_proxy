from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests
app = Flask(__name__)
CORS(app)

azure_url = "https://52.230.225.60/webhooks/rest/webhook"

@app.route("/proxy", methods=["POST"])

def proxy():
  sender = request.get_json().get('sender')
  message = request.get_json().get('message')
  if sender and message:
    prep_message = {"sender": sender, "message": message}
    header = {"Content-Type": "application/json", "Accept": "application/json"}
    json_data = json.dumps(prep_message)
    response = requests.post(url = azure_url, data = json_data, verify=False, headers=header)

    if response.status_code == 200:
      return jsonify(response.json())

  return jsonify("Error")


if __name__ == '__main__':
  app.run(debug=True)
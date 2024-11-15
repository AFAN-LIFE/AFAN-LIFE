from flask import Flask
from flask import request
from config import apiKey

# 作者：AFAN
# 时间：2023-05-30
# B站：AFAN的费曼生活
# 知识星球（免费答疑）：AFAN的费曼生活
# 知识星球（付费分享）：AFAN的金融科技

app = Flask('app')


def get_chatgpt_response(content):
  import json
  import requests
  URL = "https://api.openai.com/v1/chat/completions"
  header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + apiKey,
  }
  payload_dict = {
    "model": "gpt-3.5-turbo",
    "messages": [{
      "role": "user",
      "content": content
    }],
    "temperature": 0.7
  }
  payload_json = json.dumps(payload_dict)
  response = json.loads(
    requests.post(url=URL, data=payload_json, headers=header).text)
  return response['choices'][0]['message']['content']


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/chaggpt', methods=["POST"])
def getStock():
  print(request.json)
  content = request.json.get('content')
  reply = get_chatgpt_response(content)
  return reply


app.run(host='0.0.0.0', port=8080)

from flask import Flask, stream_with_context, request, Response, jsonify
from random import randint

app = Flask(__name__)

def Temp():
      return randint(0,20)

@app.route("/", methods=['GET', 'POST'])
def hello():
    print('yes')
    return "Hello world!"


if __name__ == '__main__':
    app.run(debug=True)
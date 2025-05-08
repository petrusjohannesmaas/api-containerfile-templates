from flask import Flask
import json

app = Flask(__name__)

x = '{"response": "🎉 Your Python server is running"}'

y = json.loads(x)


@app.route("/")
def index():
    return y


if __name__ == "__main__":
    app.run()
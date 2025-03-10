from flask import Flask
import json

app = Flask(__name__)

x = '{"response": "Your Podman container is running"}'

y = json.loads(x)


@app.route("/")
def hello_world():
    return y


if __name__ == "__main__":
    app.run()

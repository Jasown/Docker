from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return f"ID: {socket.gethostname()} Test"

if __name__ == "__main__":
    app.run(debug=True)

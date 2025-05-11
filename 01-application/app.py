import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def info():
    host   = socket.gethostname()
    ip     = socket.gethostbyname(host)
    author = os.getenv("AUTHOR", "unknown")
    return jsonify(hostname=host, ip=ip, author=author)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)





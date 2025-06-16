from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

BASE_DIR = os.getcwd()  # current working directory

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)

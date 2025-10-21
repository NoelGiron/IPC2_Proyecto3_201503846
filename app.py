from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return{'mensaje': 'API funcionando'}

if __name__ == '__main__':
    app.run(debug=True)
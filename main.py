from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world \n Google pls hire me" 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
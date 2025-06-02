from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend!+ extra part added for check"

if __name__ == '__main__':
    app.run(debug=True)

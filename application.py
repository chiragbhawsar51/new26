from flask import Flask

app = Flask(__name__)
application = app


@app.route('/')
def hello():
    return 'Hello, World! This is my Flask application.'

if __name__ == '__main__':
    app.run('0.0.0.0')

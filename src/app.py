__author__ = 'lw'

from flask import Flask

app = Flask(__name__) # '__main__'

@app.route('/')
def hello_method():
    return "Hello, world!"

if __name__ == '__main__':
    app.run() # select port with app.run(port=4995)
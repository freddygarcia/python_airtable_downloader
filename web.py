from flask import Flask, render_template, request
from generate import createXlsx

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    createXlsx()
    return render_template('index.html', url='https://www.test.com')

if __name__ == '__main__':
    app.run()
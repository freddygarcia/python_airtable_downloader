from flask import Flask, render_template, request
from generate import createXlsx

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    result = createXlsx()
    if result == 200:
        return render_template('index.html', url='https://www.test.com')
    else:
        return render_template('404.html', status = result)

if __name__ == '__main__':
    app.run()
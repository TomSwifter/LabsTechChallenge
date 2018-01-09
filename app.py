from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('/index.html')

@app.route('/ta2453', methods=['GET'])
def index():
    return render_template('/ta2453.html')

if __name__ == '__main__':
    app.run()

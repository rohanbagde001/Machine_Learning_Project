from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():   # index page
    return "Starting Machine Learning Project"

if __name__ == '__main__':
    app.run(debug=True) # run flask app in debug mode
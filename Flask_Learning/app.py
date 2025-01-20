# from  flask import Flask
from flask import Flask, redirect, url_for
#WSGI APP

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Deeksha this side"

@app.route('/hello')
def hello():
    return "hello"


###BUILDING URL DYNAMICALLY
@app.route('/success/<int:score>')
def success(score):
    return "You're passed with marks : " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "You're failed with marks : " + str(score)

@app.route('/results/<int:mark>')
def results(mark):
    result = ""
    if mark < 33:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result, score=mark))


if __name__ == '__main__':
    app.run()
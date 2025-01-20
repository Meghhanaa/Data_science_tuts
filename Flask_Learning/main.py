###INTEGRATE HTML IN FLASK
###HTTP WEB GET AND POST


# from  flask import Flask
from flask import Flask, redirect, url_for, render_template, request
#WSGI APP

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "hello"


###BUILDING URL DYNAMICALLY
@app.route('/success/<int:score>')
def success(score):
    return "HURRAY! You're passed! Your percentage is : " + str(score) + "%"

@app.route('/fail/<int:score>')
def fail(score):
    return "SADLY! You're failed! Your percentage is : " + str(score) + "%"

@app.route('/results/<int:mark>')
def results(mark):
    result = ""
    if mark < 33:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result, score=mark))


##HTML AND FLASK INTEGRATION -> RESULT CHECKER
@app.route('/submit', methods=['POST','GET'])
def submit():
    total = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        datascience = float(request.form['datascience'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        total = (science+datascience+maths+c)/4
    res=""
    if total>=33:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res, score=total))






if __name__ == '__main__':
    app.run()
### Building Url Dynamically 
####Variable Rules And URL Building



### Here for building of dynamic url  redirect and url_for is used.

from flask import Flask,redirect,url_for

### I Create instance of Flask my instance name is app YOU may choose other
###Create an Instance of Flask
app=Flask(__name__)


### /: This route corresponds to the home page of the web application

@app.route('/')
def welcome():
    return "Welcome to my Home Page"


### You may use variable parameter in route    
###You may provide html whole file or small code
####These routes use variable rules to accept an integer value (score) as a parameter.


@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>Congratulations you are Pass</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "Sorry appear again.You scored: "+ str(score)


### This route checks the value of marks and redirects the user to either the /success or /fail route using the url_for function.


@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))
    

###Here I am assign main to my instance in conndition so that it will run my instance 
### starts the Flask development server with debugging enabled

if __name__=='__main__':
    app.run(debug=True)

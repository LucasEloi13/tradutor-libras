from flask import Flask 

app = Flask(__name__)


@app.route('/homepage') 
def homepage(): 
    return 'Hello World'


app.run() 
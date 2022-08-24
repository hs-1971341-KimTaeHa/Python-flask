from flask import Flask
import random
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return str(random.random())
 
@app.route('/Welcome/')
def Welcome():
    return 'Welcome'

@app.route('/read/1/')
def read():
    return 'read 1'

app.run(debug=True)
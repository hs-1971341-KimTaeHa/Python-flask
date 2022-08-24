from flask import Flask
import random
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return str(random.random())
 
@app.route('/Welcome/')
def Welcome():
    return 'Welcome'

@app.route('/read/<id>/')
def read(id):
    return 'read'+id

app.run(debug=True)
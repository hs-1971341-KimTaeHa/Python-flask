from flask import Flask
import random
app = Flask(__name__)

topics = [
    {'id':'1', 'title':'HTML', 'body':'HTML is ...'},
    {'id':'2', 'title':'CSS', 'body':'CSS is ...'},
    {'id':'3', 'title':'Javascript', 'body':'JS is ...'}
]

liTags=''
for topic in topics:
    liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

@app.route('/')
def index():
    return f'''
        <!doctype html>
            <head>
                <meta charset="UTF-8">
                <title>document</title>
            </head>
            <body>
                <h1>WEB</h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Welcome</h2>
                Hi...
            </body>
        </html>
    '''

@app.route('/create/')
def create():
    return 'create'

@app.route('/read/<id>/')
def read(id):
    return 'read'+id

app.run(debug=True)
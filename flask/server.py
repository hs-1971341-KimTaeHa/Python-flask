from flask import Flask
import random
app = Flask(__name__)

topics = [
    {'id':1, 'title':'HTML', 'body':'HTML is ...'},
    {'id':2, 'title':'CSS', 'body':'CSS is ...'},
    {'id':3, 'title':'Javascript', 'body':'JS is ...'}
]



@app.route('/')
def index():
    liTags=''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''
        <!doctype html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>document</title>
            </head>
            <body>
                <h1><a href="/">WEB</a></h1>
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

@app.route('/read/<int:id>/')
def read(id):
    liTags=''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
    return f'''
        <!doctype html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>document</title>
            </head>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>{title}</h2>
                {body}
            </body>
        </html>
    '''

app.run(debug=True)
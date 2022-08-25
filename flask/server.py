from flask import Flask
import random
app = Flask(__name__)

topics = [
    {'id':1, 'title':'HTML', 'body':'HTML is ...'},
    {'id':2, 'title':'CSS', 'body':'CSS is ...'},
    {'id':3, 'title':'Javascript', 'body':'JS is ...'}
]

def template(contents, content):
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
                        {contents}
                    </ol>
                    {content}
                </body>
            </html>
        '''

def getContens():
    liTags=''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContens(), '<h2>Welcome</h2>Hi...' )


@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
    return template(getContens(), f'<h2>{title}</h2>{body}')

@app.route('/create/')
def create():
    return 'create'


app.run(debug=True)
from turtle import title
from flask import Flask, request, redirect
app = Flask(__name__)

nextId = 4

topics = [
    {'id':1, 'title':'HTML', 'body':'HTML is ...'},
    {'id':2, 'title':'CSS', 'body':'CSS is ...'},
    {'id':3, 'title':'Javascript', 'body':'JS is ...'}
]

def template(contents, content, id=None):
    contextUI =''
    if id != None:
        contextUI = f'''
            <a href="/update/{id}">update</a>
            <form action="/delete/{id}/" method="POST">
                <input type="submit" value="delete"/>
            </form>
        '''
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
                    <a href="/create/">create</a>
                    {contextUI}
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
    return template(getContens(), f'<h2>{title}</h2>{body}', id)

@app.route('/create/', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="description" placeholder="description"></textarea></p>
                <input type="submit" value="create"/>
            </form>
        '''
        return template(getContens(), content)

    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        description = request.form['description']
        newTopic = {'id':nextId, 'title':title, 'body':description}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId += 1
        return redirect(url)

@app.route('/update/<int:id>/', methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        title=''
        body=''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
                <form action="/update/{id}/" method="POST">
                    <p><input type="text" name="title" value="{title}"/></p>
                    <p><textarea name="description">{body}</textarea></p>
                    <input type="submit" value="update"/>
                </form>
            '''
        return template(getContens(), content, id)
    elif request.method == 'POST':
        for topic in topics:
            if id == topic['id']:
                topic['title'] = request.form['title']
                topic['body']= request.form['description']
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)
    

@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)    
            break
    return redirect('/')

app.run(debug=True)
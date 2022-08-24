#!python
print("content-type:text/html; charset=UTF-8\n")
print()
import cgi, os

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue('id')
    file = os.listdir('./data')
    description = open('./data/' + pageId,'r').read()
    listStr = ''
    for item in file:
        listStr += '<li><a href="index2.py?id={name}">{name}</a></li>'.format(name=item)
else:
    pageId = 'Welcome'
    description = 'Hello, Web'
    file = os.listdir('./data')
    listStr = ''
    for item in file:
        listStr += '<li><a href="index2.py?id={name}">{name}</a></li>'.format(name=item)

print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1><a href="index2.py">Web</a></h1>
    <ol>
        {filelist}
    </ol>
    <a href="create2.py">create</a>
    <form action="create_process2.py" method="post">
        <p><input type=""text" name="title" placeholder="title"></p>
        <p><textarea name="description" placeholder="description"></textarea></p>
        <input type="submit" value="submit"></input>
    </form>
</body>
</html>
'''.format(title=pageId, description=description, filelist=listStr))
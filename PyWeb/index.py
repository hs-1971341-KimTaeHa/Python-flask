#!python
print("content-type:text/html; charset=UTF-8\n")
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1><a href="index.py?id=WEB">Web</a></h1>
    <ol>
        <li><a href ="index.py?id=HTML">HTML</a></li>
        <li><a href ="index.py?id=CSS">CSS</a></li>
        <li><a href ="index.py?id=Javascript">Javascript</a></li>
    </ol>
    <h2>{title}</h2>
    Web...
</body>
</html>
'''.format(title=pageId))
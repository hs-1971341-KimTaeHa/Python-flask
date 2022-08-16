#!python
print("content-type:text/html; charset=UTF-8\n")
print()
import cgi, os
files = os.listdir('data')

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue('id')
    description = open('./data/' + pageId,'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, Web'

listStr = ''
for item in files:
    listStr += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1><a href="index.py">Web</a></h1>
    <ol>
        {filelist}
    </ol>
    <a href="create.py">create</a>
    <a href="update.py">update</a>
    <form action="update_process.py" method="post">
        <p><input type="hidden" name="pageId" value={form_default_title}></p>
        <p><input type="text" name="title" value={form_default_title}></p>
        <p><textarea name="description">{form_default_description}</textarea></p>
        <input type="submit" value="submit"></input>
    </form>
</body>
</html>
'''.format(title=pageId, description=description, filelist=listStr, form_default_title=pageId, form_default_description=description))
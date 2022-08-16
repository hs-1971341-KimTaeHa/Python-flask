#!python
print("content-type:text/html; charset=UTF-8\n")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue('id')
    description = open('./data/' + pageId,'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_link = '''<form action="delete_process.py" method="post">
                        <input type="hidden" name="pageId" value="{}">
                        <input type="submit" value="delete">
                    </form>'''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, Web'
    update_link = ''
    delete_link = ''


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
    {update_link}
    {delete_link}
    <h2>{title}</h2>
    {description}
</body>
</html>
'''.format(title=pageId, description=description, filelist=view.getList(), update_link=update_link, delete_link=delete_link))
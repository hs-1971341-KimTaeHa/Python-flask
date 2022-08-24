#!python
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os
form = cgi.FieldStorage()


if 'id' in form:
    pageId = form.getvalue("id")
    file = os.listdir('./data')
    description = open('./data/'+pageId, 'r').read()
    listStr = ''
    for item in file:
        listStr += '<li><a href="index2.py?id={name}">{name}</a></li>'.format(name=item)
    update_link = '<a href="update2.py?id={pageId}">update</a>'.format(pageId=pageId)
    delete_link = '''
        <form action="delete_process2.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
    

else:
    pageId = 'Welcome'
    file = os.listdir('./data')
    listStr = ''
    for item in file:
        listStr += '<li><a href="index2.py?id={name}">{name}</a></li>'.format(name=item)
    description = 'Hello, Web'
    update_link = ''
    delete_link = ''

print('''
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Practice</title>
    </head>
    <body>
        <h1><a href="index2.py">Web</a></h1>
        <ol>
            {filelist}
        </ol>
        <a href="create2.py">create</a>
        {update_link}
        {delete_link}
        <h2>{title}</h2>
        {description}
    </body>
    </html>
'''.format(title=pageId, filelist=listStr, description=description,update_link=update_link,delete_link=delete_link))
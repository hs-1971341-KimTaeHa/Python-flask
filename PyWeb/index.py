#!python
print("content-type:text/html; charset=UTF-8\n")
print()
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1><a href="index.html">Web</a></h1>
    <ol>
        <li><a href ="index.py?id=HTML">HTML</a></li>
        <li><a href ="index.py?id=CSS">CSS</a></li>
        <li><a href ="index.py?id=Javascript">Javascript</a></li>
    </ol>
    <h2>{title}</h2>
    Web...
</body>
</html>
'''.format(title='Hello'))
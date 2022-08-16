#!python

import cgi, os
form = cgi.FieldStorage()
title = form.getvalue('pageId')

os.remove('data/'+title)

print("Location: index.py")
print()
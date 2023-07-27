#!python

import cgi,os
form=cgi.FieldStorage()
pageId=form.getvalue("pageId")

os.remove('data/'+pageId)
'''
opened_file=open('data/'+title,'w')
opened_file.write(description)
opened_file.close()'''

#Redirection
print("Location: index.py")
print()
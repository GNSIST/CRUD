#!python
print("content-type: text-html; charset=utf-8\n")
print()
import cgi, os
files= os.listdir('data')
listStr=''
for item in files:
    listStr=listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
form=cgi.FieldStorage()
if 'id' in form:
    pageId=form.getvalue("id")
    description =open('data/'+pageId,'r').read()
else:
    pageId = 'welcome'
    description = 'Hello, web'

print('''<!doctype html>
<html>
<head>
    <title>WEB - 개발왕</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <script src="colors.js"></script>
    

</head>
    <body>
        <h1><a href="index.py=WEB">WEB</a></h1>

        <input id="night_day" type="button" value="night" onclick=" 
        nightDayHandelr(this)
        ">

    <div id="grid">
        <ol>
        {listStr}
        </ol>
        <a href="create.py">create</a> 
        <form action="process_create.py" method="post">
            <p><input type="text"  name="title"  placeholder="title"></p>
            <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
            <p><input type="submit"></p>
        </form> 
        
</body>
</html>'''.format(title=pageId,desc=description,listStr=listStr))
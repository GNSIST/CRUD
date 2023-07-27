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
    description=open('data/'+pageId,'r').read()
    update_link='<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action='''
        <form action="process_delete.py" method="post"> 
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>'''.format(pageId)

    
else:
    pageId='welcome'
    description='Hello, web'
    update_link=''
    delete_action=''
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
        {update_link}
        {delete_action}
        <div id="article">
            <h2>DREAM</h2>
            <h3>{title}</h3>
            <p>{desc}</p>
    </div>
</div>
</body>
</html>'''.format(title=pageId,desc=description,listStr=listStr,update_link=update_link
                  ,delete_action=delete_action))
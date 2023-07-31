from django.shortcuts import render,HttpResponse
import random
topics = [
    {'id':1,'title':'routing', 'body':'Routing is..'},
    {'id':2,'title':'view', 'body':'View is..'},
    {'id':3,'title':'model', 'body':'Model is..'},
]

def HTMLTemplete(aritcleTag):
    global topics
    ol=''
    for topic in topics:
        ol +=f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href='/'>Django</a></h1>
        <ul>
            {ol}
        </ul>
        {aritcleTag}
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplete(article))
  

def read(request,id):
    global topics
    article = ''
    for topic in topics:
        if topic ['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplete(article))

def create(request):
    return HttpResponse('Create')




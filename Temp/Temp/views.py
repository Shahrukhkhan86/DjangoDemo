
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params={'name':'shahrukh'}
    return render(request,'index.html',params)
def ex(request):
    s='''<h2>Navigation bar<br></h2><a href="https://www.javatpoint.com">Click me </a>'''
    return HttpResponse(s)
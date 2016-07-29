from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
from djangoServer.blog.models import Employee, Girl
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# def index(req):
#     # You should put it in html
#     # It will find auto from app's template
#     t = loader.get_template('index.html')
#     # The data that provide to template
#     c = Context({})
#     # Render back by template method
#     return HttpResponse(t.render(c))

# The second way:

# Create a new class


class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def say(self):
        return self.name+self.age


def index(req):
    # usr = {'name':'yyyuuu','age':'23','love':'lol'}
    usr = Person('qiqi','23','girl')
    book_list = ['python','django','js','ruby']
    return render_to_response('index.html',{'usr':usr,'book_list':book_list})


def user_info(req):
    girl = Employee.objects.all();
    print girl
    return render_to_response('login.html',{'girl':girl})

@csrf_exempt
def add(req):
    print req.method
    id = req.POST['name']
    return HttpResponseRedirect("/blog/index")
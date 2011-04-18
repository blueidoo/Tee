# Create your views here.
import datetime
from models import Blog, User
from django.http import HttpResponse

def new(request):
    blog = Blog()
    blog.title = 'This is a brand new blog.'
    blog.content = 'lalalallalalalalala'
    blog.created_at = datetime.datetime.now()

    blog.save()
    
    return HttpResponse('Save OK. <a href="/blog/view/%s/">view</a>'%blog.id)


def view(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)[0]
    print blog.title
    print blog.content
    print blog.created_at
    return HttpResponse('%s\n%s\n%s'%(blog.title, blog.content, blog.created_at))
    
    
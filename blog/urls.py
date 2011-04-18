#__author__ = 'jiangsp'
from django.conf.urls.defaults import patterns,include,url

urlpatterns = patterns('',
    url(r'^new/', 'blog.views.new'),
    url(r'^view/(?P<blog_id>[a-z0-9A-Z]+)/', 'blog.views.view')
)

  
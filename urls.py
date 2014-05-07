from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ilemon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.blog_list', name='blog_list'),
    url(r'^bloglist/$', 'blog.views.blog_list', name='blog_list'),
    url(r'^article/(?P<slug>[-\w]+)/$', 'blog.views.blog_article', name='blog_article'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'blog.views.category', name='blog_category'),
    url(r'^tag/(?P<slug>[-\w]+)/$', 'blog.views.tag', name='blog_tag'),
)



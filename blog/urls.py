from django.conf.urls import url
from django.urls import include

from mysite import settings
from . import views
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^subject/$', views.blog_subject_all, name='blog_subject_all'),
    url(r'^post/$',  views.blog_post_all, name='blog_post_all'),
    url(r'^subject/(?P<url>.+)/$', views.subject_detail, name='subject_detail'),
    url(r'^post/(?P<subject>.+)/$',  views.blog_post_subject, name='blog_post_subject'),
    #url(r'^subject/(?P<url>\.+)/(?P<url_post>.+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/(?P<url_post>.+)/$', views.post_detail, name='post_detail'),

    url(r'^(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'signup/', views.SignUp.as_view(), name='signup'),
]

'''urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]'''

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
    r'(?P<post>[-\w]+)/'
    r'(?P<author>.+)/$',
    views.post_detail,
    name='post_detail'),'''
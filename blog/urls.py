from django.conf.urls import url

#from mysite import settings
from . import views
#if settings.DEBUG:
 #   from django.contrib.staticfiles.urls import staticfiles_urlpatterns
  #  from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^subject/$', views.blog_subject_all, name='blog_subject_all'),
    url(r'^post/$',  views.blog_post_all, name='blog_post_all'),
    url(r'^subject/(?P<pk>\d+)/$', views.subject_detail, name='subject_detail'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),


]

#urlpatterns += staticfiles_urlpatterns()

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
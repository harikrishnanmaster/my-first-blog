
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import  url
from django.views.generic import TemplateView
import myapp

from myapp import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   url(r'^admin/',TemplateView.as_view(template_name = 'login.html')),
   url(r'^login/',myapp.views.login, name = 'login'),



   url(r'^deletepost/',myapp.views.deletepost, name = 'deletepost'),
   url(r'^post/',myapp.views.post, name = 'post'),
   url(r'^newpost/',myapp.views.newpost, name = 'newpost'),
   url(r'^comment/',myapp.views.comment, name = 'comment'),
   url(r'^viewpost/',myapp.views.viewpost, name = 'viewpost'),
   url(r'^commentpost/',myapp.views.commentpost, name = 'commentpost'),
   url(r'^viewcomment/',myapp.views.viewcomment, name = 'viewcomment'),



   url(r'^loggedin/',myapp.views.loggedin, name = 'loggedin'),
   url(r'^account/',myapp.views.account, name = 'account'),
   url(r'^register/',myapp.views.register, name = 'register'),
   url(r'^logout/',myapp.views.logout, name = 'logout'),


 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
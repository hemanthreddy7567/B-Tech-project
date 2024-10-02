"""DomesticNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from DomesticNews.views import index, logout
from manager.views import managerlogin, managerloginaction, viewuserdata, addnews, viewnews, viewdetails, managerhome, \
    newsdelete
from user.views import userlogin, userregister, userlogincheck, userpage, news, userviewdetails, usersearchresult, addnewss, newsdeletes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),

    url(r'^userlogin/', userlogin, name="userlogin"),
    url(r'^userregister/', userregister, name="userregister"),
    url(r'^userlogincheck/', userlogincheck, name="userlogincheck"),
    url(r'^userpage/', userpage, name="userpage"),
    url(r'^news/', news, name="news"),
    url(r'^addnewss/', addnewss, name="addnewss"),
    url(r'^userviewdetails/', userviewdetails, name="userviewdetails"),
    url(r'^usersearchresult/', usersearchresult, name="usersearchresult"),
    #url(r'^downloadnews/', downloadnews, name="downloadnews"),
    url(r'^newsdeletes/', newsdeletes, name="newsdeletes"),
    url(r'^logout/', logout, name="logout"),

    url(r'^managerlogin/', managerlogin, name="managerlogin"),
    url(r'^managerloginaction/', managerloginaction, name="managerloginaction"),
    url(r'^managerhome/', managerhome, name="managerhome"),
    url(r'^viewuserdata/', viewuserdata, name="viewuserdata"),
    url(r'^addnews/', addnews, name="addnews"),
    url(r'^viewnews/', viewnews, name="viewnews"),
    url(r'^viewdetails/', viewdetails, name="viewdetails"),
    url(r'^newsdelete/', newsdelete, name="newsdelete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
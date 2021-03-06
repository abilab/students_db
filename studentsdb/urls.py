"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from students.views import students, groups, journal, contact_admin
from .settings import DEBUG, MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact-admin/$', contact_admin.contact_admin,
        name='contact_admin'),
    # Students Urls
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students.students_edit,
        name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students.students_delete,
        name='students_delete'),
    # Groups Urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', groups.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete,
        name='groups_delete'),
    # Students Attending Urls
    url(r'^journal/$', journal.attending_list, name='students_attending_list')
]

if DEBUG:
    # serve files from media folder
    urlpatterns += [url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': MEDIA_ROOT})]

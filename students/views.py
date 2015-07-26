from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    return render(request, 'students/students_list.html', {})

def students_add(request):
    return HttpResponse('<h1>Add Student Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

def groups_list(request):
    return HttpResponse('<h1>Groups List</h1>')

def groups_add(request):
    return HttpResponse('<h1>Add Group Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s' % gid)

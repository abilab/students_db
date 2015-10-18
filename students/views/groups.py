from django.shortcuts import render
from django.http import HttpResponse
from students.models.student_group import Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def groups_list(request):
    groups = Group.objects.all()
    # paginate groups list
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # if page not integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # if page number is out of range (9999), deliver last page
        groups = paginator.page(paginator.num_pages)
    return render(request, 'students/group_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Add Group Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s' % gid)

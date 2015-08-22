from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': 'МтМ-21',
         'group_leader': 'Ячмонов Олег',
         'group_leader_id': 21},
        {'id': 2,
         'group_name': 'МтМ-22',
         'group_leader': 'Подоба Віталій',
         'group_leader_id': 22},
        {'id': 3,
         'group_name': 'МтМ-23',
         'group_leader': 'Іванов Андрій',
         'group_leader_id': 23}
    )
    return render(request, 'students/group_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Add Group Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s' % gid)

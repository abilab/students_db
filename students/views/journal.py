from django.shortcuts import render
from django.http import HttpResponse


def attending_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'attending_marks': (1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
                             1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
                             0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
                             1)},
        {'id': 2,
         'first_name': u'Дмитро',
         'last_name': u'Іванів',
         'attending_marks': (1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 0, 1, 0, 1, 1, 1,
                             0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
                             1)},
        {'id': 3,
         'first_name': u'Ярослав',
         'last_name': u'Вархол',
         'attending_marks': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
                             0, 0, 1, 1, 1, 0, 1, 1, 0, 1,
                             1)}
    )
    return render(request, 'students/student_attending.html',
                  {'students': students})
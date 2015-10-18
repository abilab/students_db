from django.contrib import admin
from students.models.student_group import Student, Group
from students.models.monthjournal import MonthJournal

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(MonthJournal)

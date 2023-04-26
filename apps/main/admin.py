from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import *
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import Widget


class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff


class StaffAdmin(ImportExportModelAdmin):
    resource_classes = [StaffResource]


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ImportExportModelAdmin):
    resource_classes = [StudentResource]


class SubjectAdmin(admin.ModelAdmin):
    list_filter = ['department', 'year', 'semester']
    list_display = ['subject_code', 'subject_name',
                    'staff', 'department', 'year', 'semester']


class TimeTableAdmin(admin.ModelAdmin):
    change_list_template = 'admin/timetable_change_list.html'
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        values = False
        if request.method == 'POST':
            dept = request.POST.get('department')
            year = request.POST.get('year')
            date = request.POST.get('date')
            values = True
            if dept == 'CSE':
                dept = 'Computer Science and Engineering'
            elif dept == 'ECE':
                dept = 'Electronics and Communication Engineering'
            elif dept == 'EEE':
                dept = 'Electrical and Electronic Engineering'
            elif dept == 'Mech':
                dept = 'Mechanical Engineering'
            elif dept == 'Civil':
                dept = 'Civil Engineering'
            timetable_data = TimeTable.objects.filter(
                period_1__department=dept, period_1__year=year,date=date)
            sub = Subject.objects.filter(department=dept, year=year)
            extra_context.update({
                'timetable': timetable_data,
                'values': values,
                'sub': sub
            })

            return super().changelist_view(request, extra_context=extra_context)
        else:
            return super().changelist_view(request, extra_context=extra_context)


class StudentAttendanceAdmin(admin.ModelAdmin):
    add_form_template = 'admin/attend.html'
    list_filter = ['name__Department', 'name__year', 'date']

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        values = False
        if request.method == 'POST':
            dept = request.POST.get('department')
            year = request.POST.get('year')
            date = request.POST.get('date')
            print(dept,year,date)
            values = True
            if dept == 'CSE':
                dept = 'Computer Science and Engineering'
            elif dept == 'ECE':
                dept = 'Electronics and Communication Engineering'
            elif dept == 'EEE':
                dept = 'Electrical and Electronic Engineering'
            elif dept == 'Mech':
                dept = 'Mechanical Engineering'
            elif dept == 'Civil':
                dept = 'Civil Engineering'

            sub = Subject.objects.filter(department=dept, year=year)
            student = Student.objects.filter(Department=dept, year=year)
            tt = TimeTable.objects.filter(department=dept, year=year,date=date)
            subname = []
            for i in tt:
                subname.append(i.period_1.subject_name)
                subname.append(i.period_2.subject_name)
                subname.append(i.period_3.subject_name)
                subname.append(i.period_4.subject_name)
                subname.append(i.period_5.subject_name)
                subname.append(i.period_6.subject_name)
                subname.append(i.period_7.subject_name)
                subname.append(i.period_8.subject_name)
            extra_context.update({
                "sub": sub,
                "student": student,
                'values': values,
                'subname':subname
            })

            return self.changeform_view(request, None, form_url, extra_context)
        else:
            return self.changeform_view(request, None, form_url, extra_context)



admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(StudentAttendance, StudentAttendanceAdmin)

from django.shortcuts import render
from .models import TimeTable, Department


def frontpage(request):
    return render(request, 'base.html')

def timetable(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    if request.method == 'POST':
        context['values'] = True
        department_id = request.POST.get('department')
        year = request.POST.get('year')
        timetable = TimeTable.objects.filter(department_id=department_id, year=year)
        context['timetable'] = timetable
    return render(request, 'time_table.html', context)

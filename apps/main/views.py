from django.shortcuts import render
from .models import TimeTable

def frontpage(request):
    return render(request, 'base.html')

def timetable(request):
   # departments = Department.objects.all()
    context = {}
    context['departments']={'name':['CSE','ECE','EEE','Mech','Civil']}
    #context['departments']=departments
    if request.method == "POST":
        department = request.POST.get('department')
        year = request.POST.get('year')
        timetable_data = TimeTable.objects.filter(period_1__department=department, period_1__year=year)
        print(timetable_data)
        context['timetable']= timetable_data
    return render(request, 'time_table.html',context)


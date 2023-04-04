from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse


def frontpage(request):
    return render(request, 'base.html')


def submitAttend(request):
    data = json.loads(request.body)
    date = str(data[-1])
    for i in data:
        try:
            print(i)
            name = i["name"]
            stu = Student.objects.get(name=name)
            StudentAttendance.objects.create(name=stu, date=date,
                                            period_1=i['period_1'],p1reason=i['p1reason'],
                                            period_2=i['period_2'],p2reason=i['p2reason'],
                                            period_3=i['period_3'],p3reason=i['p3reason'],
                                            period_4=i['period_4'],p4reason=i['p4reason'],
                                            period_5=i['period_5'],p5reason=i['p5reason'],
                                            period_6=i['period_6'],p6reason=i['p6reason'],
                                            period_7=i['period_7'],p7reason=i['p7reason'],
                                            period_8=i['period_8'],p8reason=i['p8reason'],
                                             reason=i['Reason'])
        except:
            pass
        
    return JsonResponse({'Success': True})

from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random

# Create your views here.
def index(request):
    template = loader.get_template('first/index.html')
    #현재시간을 불러온다.
    now = datetime.now()
    #동적으로 컨트롤러에서 즉, view메소드에서 정리한 변수들을 삽입/수정 가능
    #합쳐서 실제 response로 보내준다. -> templating한다고 한다.
    context = {
        #current_date로 맵핑
        'current_date' : now
    }
    return HttpResponse(template.render(context, request))


def select(request):
   context = {}
   return render(request, 'first/select.html', context)


def result(request):
    # context = {'numbers' :[1,2,3,4,5,6]}
    chosen = int(request.GET['number'])

    results=[]
    if chosen>=1 and chosen<=45:
        results.append(chosen)

    box=[]
    for i in range(0,45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results
    }
    return render(request, 'first/result.html', context)
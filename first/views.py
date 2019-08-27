from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
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
   context = {'number' : 4}
   return render(request, 'select.html', context)


def result(request):
    context = {'numbers' :[1,2,3,4,5,6]}
    return render(request, 'result.html', context)
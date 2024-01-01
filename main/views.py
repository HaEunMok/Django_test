from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Notice

# Create your views here.
@csrf_exempt
def index(request):
    print(request)
    print(type(request))
    print(dir(request))
    print('------------')
    print(request.POST)
    return render(request, 'index.html')

def test(request):
    d= {'name': 'Hong', 'age':10}
    return JsonResponse(d)

def sample(request):
    d = Notice.objects.all()
    #d= {'name': 'Hong', 'age':10}
    #l= [100,200,300]
    return render(request, 'sample.html',{'value':d})
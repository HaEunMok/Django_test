from django.shortcuts import render
from .models import Blog

# Create your views here.
# Create your views here.
def indexB(request):
    context = Blog.objects.all()
    return render(request, 'indexB.html', {'context':context})
# Create your views here.
def indexBdetail(request,pk):
    blog = Blog.objects.get(pk=pk)
    context ={'blog':blog, 
             }
    print(context)
    return render(request, 'indexBdetail.html',context)
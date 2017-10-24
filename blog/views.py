from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def search_result(request):
    return render(request, 'blog/search_result.html', {})

def search_result_2(request):
    return render(request, 'blog/search_result_2.html', {})

def hello(request):
    return HttpResponse('안녕!')


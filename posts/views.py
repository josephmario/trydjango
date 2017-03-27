#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
# Create your views here.

def post_create(request):
    error = ''
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            if title == '':
                error = 'title is requried'
            elif content == '':
                error = 'content is requried'
            elif title == '' and content == '':
                error = 'All fields are requried'
            else:
                Post.objects.create(title=title,content=content)
                return HttpResponseRedirect("/posts/list")
    except Exception as error:
        print(error)
    context = {
        "error": error
    }
    return render(request, 'post_create.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":"Details",
        "instance":instance
    }

    return render(request, 'post_detail.html', context)
def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }
    return render(request, 'index.html', context)

def post_update(request, id=None):
    error = ''
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            if title == '':
                error = 'title is requried'
            elif content == '':
                error = 'content is requried'
            elif title == '' and content == '':
                error = 'All fields are requried'
            else:
                Post.objects.filter(id=id).update(title=title, content=content)
                return HttpResponseRedirect("/posts/list")
    except Exception as error:
        print(error)
    instance = get_object_or_404(Post, id=id)
    context = {
        "error": error,
        "title":"Details",
        "instance":instance
    }
    return render(request, 'post_update.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return HttpResponseRedirect("/posts/list")

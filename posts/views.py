#-*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
# Create your views here.

def post_create(request):
    # error = ''
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            if title == '':
                messages.error(request, 'Title is requried')
                # error = 'Title is requried'
            elif content == '':
                messages.error(request, 'Content is requried')
                # error = 'Content is requried'
            elif title == '' and content == '':
                messages.error(request, 'All fields are requried')
                # error = 'All fields are requried'
            else:
                Post.objects.create(title=title,content=content)
                messages.success(request, 'Successfully Created')
                return HttpResponseRedirect("/posts/list")
    except Exception as error:
        messages.error(request, error)
    return render(request, 'post_create.html', {})

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
    # error = ''
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            if title == '':
                messages.error(request, 'Title is requried')
                # error = 'title is requried'
            elif content == '':
                messages.error(request, 'Content is requried')
                # error = 'content is requried'
            elif title == '' and content == '':
                messages.error(request, 'All fields are requried')
                # error = 'All fields are requried'
            else:
                messages.success(request, 'Successfully Updated')
                Post.objects.filter(id=id).update(title=title, content=content)
                return HttpResponseRedirect("/posts/list")
    except Exception as error:
        messages.error(request, error)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":"Details",
        "instance":instance
    }
    return render(request, 'post_update.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return HttpResponseRedirect("/posts/list")

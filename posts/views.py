from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create Here</h1>")

def post_detail(request, id=None):
    instance =get_object_or_404(Post, id=id)
    # instance = Post.objects.get(id=3)
    # return HttpResponse("<h1>Detail Here</h1>")
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
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, 'index.html', context)
    #return HttpResponse("<h1>List Here</h1>")

def post_update(request):
    return HttpResponse("<h1>Update Here</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete Here</h1>")

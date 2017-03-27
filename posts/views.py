from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print('save')
        return HttpResponseRedirect("/posts/list")
    # if request.method == "POST":
    #     print(request.POST)
    context = {
        "form":form,
    }
    # return HttpResponse("<h1>Create Here</h1>")
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
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":"Details",
        "instance":instance
    }

    return render(request, 'post_update.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return HttpResponseRedirect("/posts/list")

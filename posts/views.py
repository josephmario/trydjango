from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create Here</h1>")

def post_detail(request):
    return HttpResponse("<h1>Detail Here</h1>")

def post_list(request):
    return HttpResponse("<h1>List Here</h1>")

def post_update(request):
    return HttpResponse("<h1>Update Here</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete Here</h1>")

from django.shortcuts import render, HttpResponse

def test(request):
    return HttpResponse('Hello World!')

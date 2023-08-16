from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def introduction(request):
    return render(request, "main/introduction.html")

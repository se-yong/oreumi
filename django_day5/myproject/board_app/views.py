from django.shortcuts import render


def article_list(request):
    return render(request, 'board_app/article_list.html')


def article_create(request):
    return render(request, 'board/article_create.html')
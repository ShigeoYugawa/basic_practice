from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")


def home_view(request):
    """ログアウト後や未ログイン時に表示するページ"""
    return render(request, "home.html")
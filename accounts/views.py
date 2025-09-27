"""
ダミーサンプルビュー
"""

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def dummy_fbv(request) -> HttpResponse:
    """関数ベースビュー"""
    return HttpResponse("Hello Django from FBV!")


class DummyCBV(View):
    """クラスベースビュー"""
    def get(self, request) -> HttpResponse:
        return HttpResponse("Hello Django from CBV!")
    

def registration_view(request):
    """ユーザー登録（サインアップ）"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # フォームのデータから認証 → login
            raw_password = form.cleaned_data.get("password1")
            # USERNAME_FIELD が email なので、username 引数に email を渡す
            user = authenticate(
                request,
                username=user.email, 
                password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("accounts:welcome_view")
            else:
                # 認証失敗時の処理（通常は起こらない想定だが明示しておく）
                form.add_error(None, "ログイン処理に失敗しました。管理者にお問い合わせください。") 
        # form.is_valid() が False の場合もここに落ちる  
    else:
        form = CustomUserCreationForm()
    
    return render(request, "accounts/registration.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"   # ログインフォーム用テンプレート
    redirect_authenticated_user = True     # 既にログインしていたらリダイレクト


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")        # ログアウト後のリダイレクト先


@login_required
def welcome_view(request):
    """ログイン後に表示するページ"""
    return render(request, "accounts/welcome.html")
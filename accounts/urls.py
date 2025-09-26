"""
ダミーサンプルルーティング
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dummy_fbv, DummyCBV, signup_view

app_name = "accounts"

urlpatterns = [
    path("dummy_fbv/", dummy_fbv, name="dummy_fbv"),
    path("dummy_cbv/", DummyCBV.as_view(), name="dummy_cbv"),

    # サインアップ
    path("signup/", signup_view, name="signup"),

    # ログイン（Django標準ビューを利用）
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    ), name="login"),

    # ログアウト（Django標準ビューを利用）
    path("logout/", auth_views.LogoutView.as_view(
        next_page="accounts:login"  # ログアウト後のリダイレクト先
    ), name="logout"),
]
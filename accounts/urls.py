"""
ダミーサンプルルーティング
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dummy_fbv, DummyCBV, registration_view, CustomLoginView, CustomLogoutView, welcome_view


app_name = "accounts"

urlpatterns = [
    path("dummy_fbv/", dummy_fbv, name="dummy_fbv"),
    path("dummy_cbv/", DummyCBV.as_view(), name="dummy_cbv"),

    path("welcome/", welcome_view, name="welcome_view"),

    # サインアップ
    path("register/", registration_view, name="registration"),

    # ログイン（Django標準ビューを利用）
    path("login/", CustomLoginView.as_view(), name="login"),

    # ログアウト（Django標準ビューを利用）
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
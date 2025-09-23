"""
ダミーサンプルルーティング
"""

from django.urls import path
from .views import dummy_fbv, DummyCBV

app_name = "accounts"

urlpatterns = [
    path("dummy_fbv/", dummy_fbv, name="dummy_fbv"),
    path("dummy_cbv/", DummyCBV.as_view(), name="dummy_cbv"),
]
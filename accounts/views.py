"""
ダミーサンプルビュー
"""

from django.http import HttpResponse
from django.views import View


def dummy_fbv(request) -> HttpResponse:
    """関数ベースビュー"""
    return HttpResponse("Hello Django from FBV!")


class DummyCBV(View):
    """クラスベースビュー"""
    def get(self, request) -> HttpResponse:
        return HttpResponse("Hello Django from CBV!")
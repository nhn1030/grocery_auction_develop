from django.urls import path
from . import views

urlpatterns = [
    path('', views.combined_template_view, name='estimate_combine'),
    # 다른 URL 패턴을 추가할 수 있음
]
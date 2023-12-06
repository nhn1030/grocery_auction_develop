from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration', views.registration_view, name='registration'),
    # 다른 URL 패턴들을 추가할 수 있습니다.
]

# views.py
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import Seller, Buyer  # Seller와 Buyer 모델을 가져옵니다.

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user_type = request.POST.get('user_type')  # POST 데이터에서 'seller_type'을 가져옴
            
            if password == confirm_password:
                user = User.objects.create_user(username=username, email=email, password=password)
                
                # 사용자 유형에 따라 Seller 또는 Buyer 모델로 연결
                if user_type == 'seller':
                    seller = Seller.objects.create(user_id=user)
                    seller.save()
                else:
                    buyer = Buyer.objects.create(user_id=user)
                    buyer.save()
                    
                login(request, user)  # 로그인 처리
                return redirect('https://grocery-auction.run.goorm.site/')  # 회원가입 후 홈 페이지로 이동
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('https://grocery-auction.run.goorm.site/')  # 로그인 후 리디렉션할 페이지의 이름 또는 URL로 변경
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('https://grocery-auction.run.goorm.site/')
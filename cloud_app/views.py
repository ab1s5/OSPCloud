from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from rest_framework.status import HTTP_400_BAD_REQUEST
from social_core.exceptions import AuthAlreadyAssociated
from .models import UserInfo, FileDetailInfo
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # name = request.POST.get('name', None)
        name = 'test'
        password = request.POST.get('password', None)
        user = UserInfo.objects.get(name=name)
        if check_password(password, user):
            request.session['name'] = name
            return redirect('../home/')


def sign_up(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        # name = request.POST.get('name', None)
        name = 'aaaa'
        if UserInfo.objects.filter(name=name):
            messages.error(request, "name is already in use")
            return render(request, 'signup.html')
        email = 'ss@aa.ss'
        if UserInfo.objects.filter(email=name):
            messages.error(request, "email is already in use")
            return render(request, 'signup.html')
        image = 'asdf'
        phone_num = '1234'
        user = UserInfo(name=name, email=email, images=image, phone_num=phone_num)
        user.save()
        return redirect('../login/')


def home(request: HttpRequest):
    name = request.session.get('name')
    print("session >>", request.session.get('name'))
    print("user_id >>")
    if check_session(request):
        print("logged in")
    else:
        print("not logged in")
    return render(request, 'home.html', {'name': name})


def check_password(pw, user: UserInfo):
    # return pw == user.password
    return True


def check_session(request: HttpRequest):
    return bool(UserInfo.objects.filter(name=request.session['name']))

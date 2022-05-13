from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from social_core.exceptions import AuthAlreadyAssociated
from .models import UserInfo, FileDetailInfo


def index(request):
    return render(request, 'index.html')


def auth_allowed(backend, uid, user=None, *args, **kwargs):
    print("backend >>", backend)
    print("uid >> ", uid)
    print("user >> ", user)
    print("args >> ", args)
    print("kwargs >> ", kwargs)
    print("id >>", kwargs.get('response').get('sub'))
    UserInfo.objects.create(
        _id=kwargs.get('response').get('sub'),
        name=kwargs.get('response').get('name'),
        email='',
        images=kwargs.get('response').get('picture'),
        phone_num='',
    )
    return HttpResponse("로그인 성공")

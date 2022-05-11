from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from social_core.exceptions import AuthAlreadyAssociated
# Create your views here.


def index(request):
    return render(request, 'index.html')


def auth_allowed( backend, uid, user=None, *args, **kwargs):
    print("backend >>", backend)
    print("uid >> ", uid)
    print("user >> ", user)
    print("args >> ", args)
    print("kwargs >> ", kwargs)
    return HttpResponse("로그인 성공")

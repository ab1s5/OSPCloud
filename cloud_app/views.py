from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


import json
from datetime import timezone

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.



# from cloud.forms import FileUploadForm, UserForm, FileEditForm
from django.template.defaulttags import comment

from .forms import UserForm, FileUploadForm, UserEditForm, FileEditForm, CommentForm
from .models import FileDetailInfo, Comment, UserInfo


# 본인 업로드, 공유받은 파일 리스트 출력
# def main(request):
#     files = FileDetailInfo.objects.order_by('-file_upload')
#     context = {'files': files}
#     return render(request, 'cloud/main.html', context)


#회원정보수정, UserForm(휴대전화번호) 변경 저장 후 메인페이지 이동
# def user_edit(request, pk):
#     user = get_object_or_404(UserInfo, pk=UserInfo.id)
#     if request.method == "POST":
#         form = UserEditForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save()
#             return redirect('main')
#     else:
#         form = UserEditForm()
#     return render(request, 'cloud/user_edit.html', {'form': form})


def user_edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserEditForm(request.user)
    return render(request, 'cloud/user_edit.html', {'form': form})


#파일 업로드, FileUploadForm(파일명, 파일업로드, 게스트, 게시일자)출력 저장 후 메인 or 해당 파일상세페이지 이동
def file_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST)
        if form.is_valid():
            file = form.save(commit=False)
            file.file_upload = timezone.now()
            file.save()
            return redirect('main')
    else:
        form = FileUploadForm()
    return render(request, 'cloud/file_upload.html', {'form': form})


def file_detail(request, pk):
    file = get_object_or_404(FileDetailInfo, pk=pk)
    comments = Comment.objects.filter(file_detail = file.pk)
    comment_form = CommentForm()
    return render(request, 'cloud/file_detail.html', {'file': file, 'comments':comments, 'comment_form': comment_form})


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            user = authenticate(username=name)
            login(request, user)
            return redirect('main')
    else:
        form =UserForm()
    return render(request, 'cloud/sign_up.html', {'form':form})


def file_edit(request, pk):
    file = get_object_or_404(FileDetailInfo, pk=pk)
    if request.method == "POST":
        form = FileEditForm(request.POST, instance=file)
        if form.is_valid():
            file = form.save()
            return redirect('file_detail', pk=file.pk)
    else:
        form = FileEditForm(instance=file)
    return render(request, 'cloud/file_edit.html', {'form': form})


def file_remove(request, pk):
    file = get_object_or_404(FileDetailInfo, pk=pk)
    file.delete()
    return redirect('main')


def add_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        comment.comment_name = request.user
        form.save()
        return redirect('file_detail', pk)


def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    file_pk = comment.file_detail.pk
    comment.delete()
    return redirect('file_detail', pk=file_pk)


def comment_edit(request):
    jsonObject = json.loads(request.body)
    comment = Comment.objects.filter(id=jsonObject.get('id'))
    context = {'result':'no'}
    if comment is not None:
        comment.update(content=jsonObject.get('content'))
        context = {'result':'ok'}
        return JsonResponse(context);
    return JsonResponse(context)


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        print(bool(UserInfo.objects.filter(name='nothing')))
        return render(request, 'cloud/login.html')
    elif request.method == 'POST':
        name = request.POST.get('name', None)
        # name = 'aaaa'
        # password = request.POST.get('password', None)
        if UserInfo.objects.filter(name=name).exists():
            request.session['name'] = name
            return redirect('main')


def sign_up(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'cloud/sign_up.html')
    elif request.method == 'POST':
        name = request.POST.get('name', None)
        # name = 'aaaa'
        if UserInfo.objects.filter(name=name):
            messages.error(request, "name is already in use")
            return render(request, 'cloud/sign_up.html')
        email = request.POST.get('email', None)
        # email = 'ss@aa.ss'
        if UserInfo.objects.filter(email=email):
            messages.error(request, "email is already in use")
            return render(request, 'cloud/sign_up.html')
        phone_num = request.POST.get('phone_num', None)
        # phone_num = '1234'
        user = UserInfo(name=name, email=email, phone_num=phone_num)
        user.save()
        return redirect('login')


def main(request: HttpRequest):
    if check_session(request):
        name = request.session.get('name')
        user = UserInfo.objects.filter(name=request.session.get('name')).get()
        print(user.name)
        print("logged in")
        files = FileDetailInfo.objects.order_by('-file_upload')
        context = {'files': files, 'userinfo': user}
        return render(request, 'cloud/main.html', context)
    else:
        print("not logged in")
    return render(request, 'cloud/logo.html')


def check_password(pw, user: UserInfo):
    # return pw == user.password
    return True


def check_session(request: HttpRequest):
    return bool(UserInfo.objects.filter(name=request.session.get('name')))


def logout(request):
    request.session.flush()
    return redirect('main')

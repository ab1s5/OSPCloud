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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm, FileUploadForm, UserEditForm, FileEditForm, CommentForm
from .models import FileDetailInfo, Comment, UserInfo


def user_edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserEditForm(request.user)
    return render(request, 'cloud/user_edit.html', {'form': form})

def file_upload(request):
    user = UserInfo.objects.filter(name=request.session.get('name')).get()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES, request.session)
        print('aaaaaaa')
        print('id')
        print('bbbbbbb')
        id = 1
        files = FileDetailInfo.objects.all()
        maxid = 0
        for file in files:
            maxid = max(maxid, file.id)
        id = maxid + 1
        print(id)
        file_title = request.POST['file_title']
        guest_name = request.POST['guest_name']
        file_url = request.FILES.get('file_url')
        owner_name = user
        # file_url = request.FILES['file_url']
        print('-----------')
        print(request.FILES)
        print('-----------')
        file = FileDetailInfo(
            id=id,
            file_title=file_title,
            guest_name=guest_name,
            file_url=file_url,
            owner_name=owner_name,
        )
        file.save()
        return redirect('main')
    else:
        form = FileUploadForm()
    return render(request, 'cloud/file_upload.html', {'form': form, 'userinfo': user, })
# def file_upload(request):
#     user = UserInfo.objects.filter(name=request.session.get('name')).get()
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES, request.session)
#         print('aaaaaaa')
#         print('id')
#         print('bbbbbbb')
#         id=1
#         for x in range(1, 100):
#             id+= 1
#             id.insert_one({"id": id})
#         file_title = request.POST['file_title']
#         guest_name = request.POST['guest_name']
#         file_url = request.FILES.get('file_url')
#         owner_name = user
#         # file_url = request.FILES['file_url']
#         print('-----------')
#         print(request.FILES)
#         print('-----------')
#         file = FileDetailInfo(
#             id=id,
#             file_title=file_title,
#             guest_name=guest_name,
#             file_url=file_url,
#             owner_name=owner_name,
#         )
#         file.save()
#         return redirect('main')
#     else:
#         form = FileUploadForm()
#     return render(request, 'cloud/file_upload.html', {'form': form, 'userinfo': user, })


def file_detail(request, pk):
    user = UserInfo.objects.filter(name=request.session.get('name')).get()
    file = get_object_or_404(FileDetailInfo, pk=pk)
    print(user)
    print(file.owner_name)
    guests = file.guest_name.strip().split(",")
    comments = Comment.objects.filter(file_detail=pk)
    comment_form = CommentForm()
    if request.method == "POST":
        file_detail = file
        comment_text = request.POST['body']
        comment_name = user
        comment = Comment(
            file_detail=file_detail,
            comment_text=comment_text,
            comment_name=comment_name,
        )
        comment.save()
        return redirect('file_detail', pk)
    # form = CommentForm(request.POST)
    # if form.is_valid():
    #     form = form.save(commit=False)
    #     comment.comment_name = user
    #     form.save()
    #     return redirect('file_detail', pk)
    context = {'file': file, 'comments':comments,'comment_form':comment_form, 'userinfo':user, 'guests':guests}
    return render(request, 'cloud/file_detail.html', context)


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
    user = UserInfo.objects.filter(name=request.session.get('name')).get()
    file = get_object_or_404(FileDetailInfo, pk=pk)
    if user != file.owner_name:
        messages.error(request, '수정할 수 없습니다')
        return redirect('file_detail', pk=file.id)
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES, request.session)
        # if form.is_valid():
        #     file = form.save()
        #     return redirect('file_detail', pk=file.pk)
        form = FileEditForm(request.POST, request.session)
        file_title = request.POST['file_title']
        guest_name = request.POST['guest_name']
        file_url = request.FILES.get('file_url')
        owner_name = user
        id=file.id
        file = FileDetailInfo(
            id=id,
            file_title=file_title,
            guest_name=guest_name,
            file_url=file_url,
            owner_name=owner_name,
        )
        file.save()
        file_pk = pk
        return redirect('file_detail', file_pk)
    else:
        form = FileUploadForm(instance=file)
    return render(request, 'cloud/file_edit.html', {'form': form, 'userinfo': user, })


def file_remove(request, pk):
    user = UserInfo.objects.filter(name=request.session.get('name')).get()
    file = get_object_or_404(FileDetailInfo, pk=pk)
    if user != file.owner_name:
        messages.error(request, '삭제할 수 없습니다')
        return redirect('file_detail', pk=file.id)
    file.delete()
    return redirect('main')

# @method_decorator(csrf_exempt)
# def add_comment(request, pk):
#     user = UserInfo.objects.filter(name=request.session.get('name')).get()
#     # file = fileDetailInfo.objects.filter(file.id=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.session)
#         comment_text = request.POST.get('comment_text')
#         file_detail = file
#         comment_name = user
#         comment = Comment(
#             file_detail=file_detail,
#             comment_text=comment_text,
#             comment_name=comment_name,
#         )
#         comment.save()
#         file_pk = comment.file_details
#         return redirect('file_detail', pk=file_pk)
# def add_comment(request, pk):
#     user = UserInfo.objects.filter(name=request.session.get('name')).get()
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         form = form.save(commit=False)
#         comment.comment_name = user
#         form.save()
#         return redirect('file_detail', pk)


def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    file_pk = comment.file_detail.pk
    comment.delete()
    return redirect('file_detail', pk=file_pk)


def comment_edit(request, pk):
    user = UserInfo.objects.filter(name=request.session.get('name')).get()
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.session)
        comment_text = request.POST['comment_text']
        comment_name = user
        file_detail = comment.id
        comment = CommentForm(
            comment_text = comment_text,
            comment_name = comment_name,
            file_detail = file_detail,
        )
        comment.save()
        return redirect('file_detail', pk=comment.file_detail)
    else:
        form = CommentForm(instance=comment)
    context = {'comment':comment, 'form':form}
    return render(request, 'cloud/comment_edit.html', context)


# def comment_edit(request):
#     jsonObject = json.loads(request.body)
#     comment = Comment.objects.filter(id=jsonObject.get('id'))
#     context = {'result':'no'}
#     if comment is not None:
#         comment.update(content=jsonObject.get('content'))
#         context = {'result':'ok'}
#         return JsonResponse(context);
#     return JsonResponse(context)


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
        files = FileDetailInfo.objects.filter(owner_name=user.email).order_by('-file_upload')
        print("files >> ", files)
        all_files = FileDetailInfo.objects.all()
        print("all_files >> ", all_files)
        shared_files = []
        for file in all_files:
            guests = file.guest_name.strip().split(",")
            for guest in guests:
                guest = guest.strip()
                if name == guest:
                    shared_files.append(file)
                elif user.email == guest:
                    shared_files.append(file)
        print("shared_files >> ", shared_files)
        context = {'files': files, 'userinfo': user, 'shared_files': shared_files}
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

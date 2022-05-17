from django.forms import forms
from django import forms

from cloud_app.models import FileDetailInfo, UserInfo, Comment


class FileUploadForm(forms.ModelForm):
	class Meta:
		model = FileDetailInfo
		fields = ('file_title', 'guest_name', 'file_url', )
		labels ={
			'file_title': '파일명',
			'guest_name': '공유명단',
			'file_url': '파일선택',
		}


class FileEditForm(forms.ModelForm):
	class Meta:
		model = FileDetailInfo
		fields = ['file_title','guest_name', 'file_url', ]
		labels = {'file_title': '파일명','guest_name': '공유명단', 'file_url': '파일선택', }


class UserEditForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['phone_num', ]


class UserForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['name', 'email', 'phone_num',]
		labels = {'name':'사용자이름', 'email':'이메일', 'phone_num':'휴대폰번호',}


class loginForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['name',]
		labels = {'name': '사용자이름',}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text',]
		labels = {'comment_text': '',}

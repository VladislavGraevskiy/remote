from django import forms
from django.contrib.auth.forms import UserCreationForm

from remote_control.models.user import Userprofile


class UserprofileForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = Userprofile
        fields = [
            'user_type', 'user_type', 'student_number', 'course',
            'first_name', 'last_name', 'email', 'password1', 'password2',
            'username'
        ]

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if student_number and Userprofile.objects.filter(email=student_number).exists():
            raise forms.ValidationError('Пользователь уже зарегестрирован')
        return student_number


class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput,)

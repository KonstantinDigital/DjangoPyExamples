from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Введите код с картинки')


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})

    name_ru = forms.CharField(label='Имя', help_text='Максимум 150 символов',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control form-control-sm', 'placeholder': 'Имя',
                                         'aria-label': "Имя", 'aria-describedby': 'basic-addon1'}))
    surname_ru = forms.CharField(label='Фамилия', help_text='Максимум 150 символов',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control form-control-sm', 'placeholder': 'Фамилия',
                                            'aria-label': "Фамилия", 'aria-describedby': 'basic-addon1'}))
    patronymic_ru = forms.CharField(label='Отчество', help_text='Максимум 150 символов',
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Отчество',
                                               'aria-label': "Отчество", 'aria-describedby': 'basic-addon1'}))
    name_en = forms.CharField(label='Name', help_text='Максимум 150 символов',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name',
                                         'aria-label': 'Name', 'aria-describedby': 'basic-addon2'}))
    surname_en = forms.CharField(label='Surname', help_text='Максимум 150 символов',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control form-control-sm', 'placeholder': 'Surname',
                                            'aria-label': 'Surname', 'aria-describedby': 'basic-addon2'}))
    patronymic_en = forms.CharField(label='Patronymic', help_text='Максимум 150 символов',
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Patronymic',
                                               'aria-label': 'Patronymic', 'aria-describedby': 'basic-addon2'}))
    phone = forms.CharField(label='Номер телефона',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control phone', 'aria-label': 'Номер телефона'}))
    email = forms.EmailField(label='e-mail',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': 'example@email.ru'}))
    organization = forms.CharField(label='Organization',
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Организация',
                                              'aria-describedby': 'basic-addon3'}))
    job_title = forms.CharField(label='Job Title',
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Должность',
                                              'aria-describedby': 'basic-addon3'}))
    public_rinc = forms.ChoiceField(label='Публикация РИНЦ',
                                    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                                    choices=[('1', 'Да'), ('2', 'Нет')],
                                    initial='2')
    public_scopus = forms.ChoiceField(label='Публикация Web of Science или Scopus',
                                    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                                    choices=[('1', 'Да'), ('2', 'Нет')],
                                    initial='2')
    training = forms.ChoiceField(label='Курсы повышения квалификации',
                                      widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                                      choices=[('1', 'Да'), ('2', 'Нет')],
                                      initial='2')
    training_details = forms.CharField(label='Наименование образовательной программы',
                                            required=False,
                                            widget=forms.Textarea(
                                                attrs={'class': 'form-control', 'rows': 5}))
    participation = forms.ChoiceField(label='Участие в конференции',
                                 widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                                 choices=[('1', 'Да'), ('2', 'Нет')],
                                 initial='2')
    username = forms.CharField(label='Логин', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    # USERNAME_FIELD = 'username'
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='Введите код с картинки')

    class Meta:
        model = CustomUser
        fields = ('name_ru', 'surname_ru', 'patronymic_ru', 'name_en', 'surname_en', 'patronymic_en', 'phone', 'email',
                  'organization', 'job_title', 'public_rinc', 'public_scopus',
                  'training', 'training_details', 'participation', 'username', 'password1', 'password2')

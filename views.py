from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import UserRegisterForm, UserLoginForm
from .models import Article, ArticleScopus


# Create your views here.
def index(request):
    context = {
        'title': 'ИнтерАгроМаш'
    }
    return render(request, 'index.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Регистрация прошла успешно')

            user = form.save()
            if user.public_rinc == '1':
                article_rinc_count = request.POST.get('article_rinc_count')
                for i in range(int(article_rinc_count)):
                    article = 'article{}'.format(i + 1)
                    globals()[article] = Article()
                    globals()[article].title = request.POST.get('rinc_title{}'.format(i + 1))
                    writers = request.POST.getlist('rinc_writer{}'.format(i + 1))
                    writer = ''
                    for writ in writers:
                        writer += writ + ', '
                    writer = writer.rstrip(', ')
                    globals()[article].writer = writer

                for i in range(int(article_rinc_count)):
                    article = 'article{}'.format(i + 1)
                    globals()[article].custom_user_id = user.id
                    print(globals()[article].writer)
                    globals()[article].save()

            if user.public_scopus == '1':
                article_scopus_count = request.POST.get('article_scopus_count')
                print(article_scopus_count)
                for i in range(int(article_scopus_count)):
                    article_scopus = 'article_scopus{}'.format(i + 1)
                    globals()[article_scopus] = ArticleScopus()
                    globals()[article_scopus].title = request.POST.get('scopus_title{}'.format(i + 1), '')
                    writers = request.POST.getlist('scopus_writer{}'.format(i + 1))
                    writer = ''
                    for writ in writers:
                        print(writ)
                        writer += writ + ', '
                    writer = writer.rstrip(', ')
                    globals()[article_scopus].writer = writer

                for i in range(int(article_scopus_count)):
                    article_scopus = 'article_scopus{}'.format(i + 1)
                    globals()[article_scopus].custom_user_id = user.id
                    print(globals()[article_scopus].writer)
                    globals()[article_scopus].save()

            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Пароль слишком слаб или выбранный Вами логин уже используется')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'Регистрация'})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'title': 'Авторизация'})


def user_logout(request):
    logout(request)
    return redirect('Login')

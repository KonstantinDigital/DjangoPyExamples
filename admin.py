from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import CustomUser, Article, ArticleScopus
from .forms import UserRegisterForm


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name_ru', 'surname_ru', 'patronymic_ru', 'name_en', 'surname_en', 'patronymic_en', 'phone', 'email',
        'organization', 'job_title', 'public_rinc', 'public_rinc_article', 'public_scopus', 'public_scopus_article',
        'training', 'training_details', 'participation', 'username')
    form = CustomUserAdminForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', 'writer', 'title')
    list_display_links = ('custom_user', 'title')


class ArticleScopusAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', 'writer', 'title')
    list_display_links = ('custom_user', 'title')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleScopus, ArticleScopusAdmin)

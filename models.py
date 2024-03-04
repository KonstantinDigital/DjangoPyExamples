from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name_ru = models.CharField(max_length=20, verbose_name='Имя на русском')
    surname_ru = models.CharField(max_length=20, verbose_name='Фамилия на русском')
    patronymic_ru = models.CharField(max_length=20, verbose_name='Отчество на русском')
    name_en = models.CharField(max_length=20, verbose_name='Имя на английском')
    surname_en = models.CharField(max_length=20, verbose_name='Фамилия на английском')
    patronymic_en = models.CharField(max_length=20, verbose_name='Отчество на английском')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    organization = models.CharField(max_length=50, verbose_name='Организация')
    job_title = models.CharField(max_length=50, verbose_name='Должность', default='')
    public_rinc = models.CharField(max_length=5, verbose_name='Публикация РИНЦ',
                                     choices=(('1', 'Да'), ('2', 'Нет')),
                                     default='2')
    public_scopus = models.CharField(max_length=5, verbose_name='Публикация Web of Science или Scopus',
                                       choices=(('1', 'Да'), ('2', 'Нет')),
                                       default='2')
    training = models.CharField(max_length=5, verbose_name='Курсы повышения квалификации',
                                  choices=(('1', 'Да'), ('2', 'Нет')),
                                  default='2')
    training_details = models.CharField(verbose_name='Наименование образовательной программы',
                                        max_length=191)
    participation = models.CharField(max_length=5, verbose_name='Участие в конференции',
                                       choices=(('1', 'Да'), ('2', 'Нет')),
                                       default='2')

    def public_rinc_article(self):
        if self.public_rinc == '1':
            str_article = ''
            for num, artic in enumerate(self.articles.all()):
                str_article += str(num + 1) + '. ' + str(artic) + '\n'
            return str_article
        else:
            return ''

    def public_scopus_article(self):
        if self.public_scopus == '1':
            str_article = ''
            for num, artic in enumerate(self.articles_scopus.all()):
                str_article += str(num + 1) + '. ' + str(artic) + '\n'
            return str_article
        else:
            return ''


class Article(models.Model):
    custom_user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, verbose_name='Логин',
                                    related_name='articles')
    writer = models.CharField(max_length=50, verbose_name='Автор', default='')
    title = models.CharField(max_length=191, verbose_name='Название', default='')

    def __str__(self):
        return self.writer + ' "' + self.title + '" '

    class Meta:
        verbose_name = 'Статья РИНЦ'
        verbose_name_plural = 'Статьи РИНЦ'


class ArticleScopus(models.Model):
    custom_user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, verbose_name='Логин',
                                    related_name='articles_scopus')
    writer = models.CharField(max_length=50, verbose_name='Автор', default='')
    title = models.CharField(max_length=191, verbose_name='Название', default='')

    def __str__(self):
        return self.writer + ' "' + self.title + '" '

    class Meta:
        verbose_name = 'Статья WOS/Scopus'
        verbose_name_plural = 'Статьи WOS/Scopus'


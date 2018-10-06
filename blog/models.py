from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from django.utils import timezone
from django.utils.text import slugify
from transliterate import translit


class SubjectPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'url': self.url})

    def save(self, *args, **kwargs):
        url = translit(self.title, 'ru', reversed=True)
        self.url = url.replace(" ", "_")
        super(SubjectPost, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='published_date', blank=True, null=True)
    subject = models.ForeignKey('SubjectPost', on_delete=models.CASCADE, related_name='resul')
    text = models.TextField()
    LOAN_STATUS = (
        ('y', 'Опубликовать'),
        ('n', 'Опубликовать позже'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='y', help_text='Публикация?')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_user(self):
        return self.author.user

    def get_subject(self):
        return self.subject.url

    def get_short_text(self):
        return self.text[:900]

    def save(self, *args, **kwargs):
        slug = translit(self.title, 'ru', reversed=True)
        self.slug = slug.replace(" ", "_")
        super(Post, self).save(*args, **kwargs)

    @property
    def get_url_subject(self):
        return self.subject

    @property
    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.slug])
'''class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'''''


class User(AbstractUser):
    # add additional fields in here
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.email


"""class TypesFiles(models.Model):
    tf = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.tf


class PostFile(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    # tf = models.MultipleChoiceField(choices=models.TypeFiles)
    # tf = models.TypeFiles('q', choise=models.TypeFiles.__str__(all()))
    # добавить файл
    tf = models.ManyToManyField(TypesFiles)
    file = models.FileField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text"""
# python manage.py makemigrations blog
# python manage.py migrate blog
# manage.py migrate --run-syncdb - обновить базу
# python manage.py createsuperuser

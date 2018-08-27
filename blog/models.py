from django.db import models
from django.utils import timezone


class SubjectPost(models.Model):
    subject = models.CharField(max_length=200)
    about = models.TextField()

    def __str__(self):
        return self.subject




class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.ForeignKey('SubjectPost', on_delete=models.CASCADE, related_name='resul')
    text = models.TextField()
   # small_text = text[:100]
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_short_text(self):
        return self.text[:130]


# noinspection PyArgumentList,PyCallByClass


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

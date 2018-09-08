# Register your models here.
from django.contrib import admin

from .models import Post, SubjectPost, Profile

admin.site.register(Post)
admin.site.register(SubjectPost)
admin.site.register(Profile)
#admin.site.register(PostFile)
#admin.site.register(TypesFiles)

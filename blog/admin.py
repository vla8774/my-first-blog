# Register your models here.
from django.contrib import admin

from .models import Post, SubjectPost, User

admin.site.register(Post)
admin.site.register(SubjectPost)
admin.site.register(User)
#admin.site.register(PostFile)
#admin.site.register(TypesFiles)

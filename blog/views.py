from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, SubjectPost


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    #posts = SubjectPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


'''def subject_list(request):
    subjects = SubjectPost.objects.all()
    return render(request, 'blog/post_list.html', {'subject': subjects})'''


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def subject_detail(request, pk):
    # subject = SubjectPost.object.filter(pk=pk)
    subject = get_object_or_404(SubjectPost, pk=pk)
    return render(request, 'blog/subject_detail.html', {'subject': subject})


'''def get_result(request, pk):
    posts = get_object_or_404(Post, subject_id=pk)
    return render(request, 'blog/subject_detail.html', {'posts': posts})'''


def blog_subject_all(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = SubjectPost.objects.all()
    # posts = SubjectPost.objects.all()
    return render(request, 'blog/blog_subject_all.html', {'posts': posts})



def blog_post_all(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    # posts = SubjectPost.objects.all()
    get_menu()
    return render(request, 'blog/blog_post_all.html', {'posts': posts})


def get_menu(request, pk):
    posts = SubjectPost.objects.all()
    subject_detail(pk=pk)
    return render(request, 'blog/base_menu.html', {'menu': posts})
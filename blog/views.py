from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Post, SubjectPost
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


def post_list(request):
    data = {}
    get_base_menu(data)
    data['posts'] = Post.objects.filter(status='y', published_date__lte=timezone.now()).order_by('-published_date')[:2]
    return render(request, 'blog/post_list.html', data)


'''def post_list(request):
    object_list = Post.objects.filter(status='y')
    paginator = Paginator(object_list, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post_list.html',
                  {'page': page,
                   'posts': posts})'''


def get_base_menu(data):
    data['subjects'] = SubjectPost.objects.all()


def subject_detail(request, url):
    data = {}
    get_base_menu(data)
    data["subject"] = get_object_or_404(SubjectPost, url=url)
    return render(request, 'blog/subject_detail.html', data)


def post_detail(request, post):
    data = {}
    get_base_menu(data)
    data['post'] = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post_detail.html', data)


def get_subject(sub):
    sub['sub'] = SubjectPost.objects.filter(title='Первая тема')


def blog_subject_all(request):
    data = {}
    get_base_menu(data)
    data['subject'] = SubjectPost.objects.all()
    return render(request, 'blog/blog_subject_all.html', data)


def blog_post_all(request):
    data = {}
    get_base_menu(data)
    data['posts'] = Post.objects.all()
    return render(request, 'blog/blog_post_all.html', data)


def blog_post_subject(request, subject):
    data = {}
    get_base_menu(data)
    data['subject'] = get_object_or_404(SubjectPost, url=subject)
    return render(request, 'blog/blog_post_subject.html', data)


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

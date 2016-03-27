from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def index(request):
    return render(request, 'blog/index.html')


def view_topics(request):
    topics = Topic.objects.filter()
    return render(request, 'blog/topics.html', {'topics': topics})


def thread(request, pk):
    cur_thread = get_object_or_404(Thread, pk=pk)
    comments = cur_thread.comments.all
    form = CommentForm(request.POST)

    print(cur_thread.parent)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.parent = pk
        comment.save()
        cur_thread.comments.add(comment)
        return redirect('blog.views.thread', pk=pk)
    form = CommentForm()
    return render(request, 'blog/thread.html', {'cur_thread': cur_thread, 'comments':comments, 'form': form})

def topic(request, pk):
    cur_topic = get_object_or_404(Topic, pk=pk)
    threads = cur_topic.threads.all
    form = ThreadForm(request.POST)
    if form.is_valid():
        thread = form.save(commit=False)

        try:
            identical = Thread.objects.get(topic=pk, title=thread.title)

        except Thread.DoesNotExist:
            thread.parent = pk
            thread.save()
            thread.parent = pk
            cur_topic.threads.add(thread)
            return redirect('blog.views.topic', pk=pk)
    form = ThreadForm()
    return render(request, 'blog/topic.html', {'cur_topic': cur_topic, 'threads':threads, 'form': form})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('blog.views.post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_list.html', {'posts': posts, 'form' : form})


def home_page(request):
    return render(request, 'blog/home_page.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
   # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post.remove()
    return redirect('blog.views.post_list')


def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_list')
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
               # post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


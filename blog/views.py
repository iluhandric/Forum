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


def ask(request):
    return render(request, 'blog/ask.html')

def search_tag(request, par, pk):
    cur_topic = get_object_or_404(Topic, pk=par)
    tag = Tag.objects.get(pk=pk)
    all_threads = cur_topic.threads.all()
    threads = []
    for thread in all_threads:
        if tag.title in thread.tags:
            threads.append(thread)

    return render(request, 'blog/tag_results.html', {'cur_topic': cur_topic, 'threads':threads, 'cur_tag': tag})

def view_topics(request):
    topics = Topic.objects.filter()
    return render(request, 'blog/topics.html', {'topics': topics})

def tags(request, pk):
    cur_topic = get_object_or_404(Topic, pk=pk)
    tags = Tag.objects.filter(parent=pk).order_by('-uses') #= cur_topic.tags.all
    return render(request, 'blog/tags.html', {'cur_topic': cur_topic, 'tags': tags})

def thread(request, par, pk):
    cur_thread = get_object_or_404(Thread, pk=pk)

    form = CommentForm(request.POST)

    print(cur_thread.parent)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.parent = pk
        comment.time_posted = timezone.now()
        comment.save()
        cur_thread.comments.add(comment)
        return redirect('blog.views.thread', par=par, pk=pk)
    form = CommentForm()
    comments = cur_thread.comments.all().order_by('-time_posted')
    cp = get_object_or_404(Topic, pk=cur_thread.parent)
    return render(request, 'blog/thread.html', {'cur_thread': cur_thread, 'comments':comments, 'form': form, 'cur_parent': cp })


def threads(request, pk):
    cur_topic = get_object_or_404(Topic, pk=pk)
    threads = cur_topic.threads.all
    form = ThreadForm(request.POST)
    if form.is_valid():
        thread = form.save(commit=False)
        try:
            Thread.objects.get(parent=pk, title=thread.title)

        except Thread.DoesNotExist:
            thread.parent = pk
            thread.save()
            tag_object = None
            tag_set = set()
            for tag in str(thread.tags).split(' '):
                tag_set.add(tag)
            for tag in tag_set:
                try:
                    tag_object = Tag.objects.get(parent=pk, title=tag)
                    tag_object.uses += 1
                except Tag.DoesNotExist:
                    tag_object = Tag(parent=pk, title=tag, uses=0)
                    tag_object.uses = 1
                tag_object.save()
                thread.parsed_tags.add(tag_object)
            thread.save()
            thread.parent = pk

            cur_topic.threads.add(thread)
            return redirect('blog.views.threads', pk=pk)
    form = ThreadForm()
    return render(request, 'blog/threads.html', {'cur_topic': cur_topic, 'threads':threads, 'form': form})


def topic(request, pk):
    cur_topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'blog/topic.html', {'cur_topic': cur_topic})

def home_page(request):
     return render(request, 'blog/home_page.html')

#
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     #if request.method == "POST":
#     form = PostForm(request.POST)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.published_date = timezone.now()
#         post.save()
#         return redirect('blog.views.post_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_list.html', {'posts': posts, 'form' : form})
#
#
# def home_page(request):
#     return render(request, 'blog/home_page.html')
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
#
#
# def post_remove(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     post.remove()
#     return redirect('blog.views.post_list')
#
#
# def post_new(request):
#         if request.method == "POST":
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 post.author = request.user
#                 post.published_date = timezone.now()
#                 post.save()
#                 return redirect('blog.views.post_list')
#         else:
#             form = PostForm()
#         return render(request, 'blog/post_edit.html', {'form': form})
#
#
# def post_edit(request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         if request.method == "POST":
#             form = PostForm(request.POST, instance=post)
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 post.author = request.user
#                # post.published_date = timezone.now()
#                 post.save()
#                 return redirect('blog.views.post_list')
#         else:
#             form = PostForm(instance=post)
#         return render(request, 'blog/post_edit.html', {'form': form})


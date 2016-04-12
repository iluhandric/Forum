from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import *
from datetime import *
from .forms import *
from .serializers import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import time
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.views import APIView
from django.forms.models import model_to_dict



from django.core import serializers
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def block_user(request):
    block = BlockUser(request.POST)
    admin = Admin.objects.get()
    user = 0
    if admin.cur_ip == get_client_ip(request):
        user = 1

    if block.is_valid():
        ip = block.cleaned_data['user_ip']
        new_bad = Blocked(address=ip)
        new_bad.save()
        Comment.objects.all().filter(author_ip=ip).delete()
        return redirect('blog.views.block_user')

    block = BlockUser()
    return render(request, 'blog/block_user.html', {'blocka': block, 'user':user})

# def admin_login(request):
#     form = PassForm(request.POST)
#     admin = Admin.objects.get()
#
#     if form.is_valid():
#         if form.cleaned_data['password'] == admin.password:
#             print(admin.password)
#             admin.cur_ip = get_client_ip(request)
#             return redirect('blog.views.home_page')
#     form = PassForm()
#     return render(request, 'blog/admin_login.html', {'form': form})


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
    return render(request, 'blog/index.html')


def ask(request):
    return render(request, 'blog/ask.html')

def search_tag(request, par, pk):
    cur_topic = get_object_or_404(Topic, pk=par)
    tag = Tag.objects.get(pk=pk)
    all_threads = cur_topic.threads.all().order_by('-time_posted')
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


def is_blocked(request):
    user_ip = get_client_ip(request)
    try:
        is_blocked = Blocked.objects.get(address=user_ip)
        return True
    except Blocked.DoesNotExist:
        return False
    except Blocked.MultipleObjectsReturned:
        return True

def image_original(request, img):
    print(img)
    return render(request, 'blog/original.html', {'image': img})

def thread(request, par, pk):
    cur_thread = get_object_or_404(Thread, pk=pk)
    form = CommentForm(request.POST, request.FILES)
    print(cur_thread.parent)
    if form.is_valid() and not is_blocked(request):
        comment = form.save(commit=False)
        comment.parent = pk
        comment.time_posted = timezone.now()
        comment.author_ip = get_client_ip(request)
        comment.save()
        cur_thread.comments.add(comment)
        return redirect('blog.views.thread', par=par, pk=pk)
    form = CommentForm()
    comments = cur_thread.comments.all().order_by('-time_posted')
    cp = get_object_or_404(Topic, pk=cur_thread.parent)
    return render(request, 'blog/thread.html', {'cur_thread': cur_thread, 'comments':comments, 'form': form,
                                                'cur_parent': cp})


def threads(request, pk):
    cur_topic = get_object_or_404(Topic, pk=pk)
    threads = cur_topic.threads.all().order_by('-time_posted')
    form = ThreadForm(request.POST, request.FILES)
    if form.is_valid() and not is_blocked(request):
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
                if tag:
                    try:
                        tag_object = Tag.objects.get(parent=pk, title=tag)
                        tag_object.uses += 1
                    except Tag.DoesNotExist:
                        tag_object = Tag(parent=pk, title=tag, uses=0)
                        tag_object.uses = 1
                    tag_object.save()
                    thread.parsed_tags.add(tag_object)
            thread.time_posted = timezone.now()
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


def comment_remove(request, par, pk, comment_pk):
     comment = get_object_or_404(Comment, pk=comment_pk)
     comment.remove()
     return redirect('blog.views.thread', par=par, pk=pk)


def comment_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def counter(request):
    pk = request.GET["pk"]
    cur_ip = get_client_ip(request)
    cur_thread = Thread.objects.get(pk=pk)
    ip_set = set()
    now = time.time()
    is_new = 1
    count = cur_thread.users.all().count()
    if cur_thread.users:
        for user in cur_thread.users.all():
            if user.ip == cur_ip:
                user.last_request = datetime.now()
                is_new = False
            else:
                if int(timezone.now) - int(user.last_request) > 1000:
                    cur_thread.users.filter(ip=cur_ip).delete()
                    user.delete()
                    cur_thread.save()
                    count -= 1
    if is_new:
        new_user = UserIp(ip=cur_ip, last_request=datetime.now())
        new_user.save()
        cur_thread.users.add(new_user)
        cur_thread.save()
        count += 1
    data = dict()
    data["count"] = count
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['GET', 'POST'])
def get_comments(request):
    if not is_blocked(request):
        thread_pk = request.GET["pk"]
        cur_thread = Thread.objects.get(pk=thread_pk)
        comments = cur_thread.comments.all().order_by('-time_posted')
        data = []
        for com in comments:
            new_obj = model_to_dict(com)
            for field in new_obj:
                if field == 'time_posted':
                    new_obj[field] = new_obj[field].strftime("%Y/%m/%d %H:%M:%S")
                if field and field != 'time_posted':
                    new_obj[field] = str(new_obj[field])

            data.append(new_obj)
    else:
        data = [{'text' : 'YOU ARE BLOCKED AND NOT ALLOWED TO VIEW OR POST ANYTHING', 'time_posted': ''}]
    return Response(json.dumps(data), content_type='application/json')


#
# class CommentList(APIView):
#     def get(self, request, format=None):
#         thread_pk = request.GET["pk"]
#         cur_thread = Thread.objects.get(pk=thread_pk)
#         comments = cur_thread.comments.all().order_by('-time_posted')
#         serializer = CommentSerializer(comments, many=True)
#         return HttpResponse(json.dumps(serializer.data), content_type='application/json')
#
#     def post(self, request, format=None):
#         serializer = CommentSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         comment = self.get_object(pk)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
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


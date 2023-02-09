from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Postlist(ListView): #class방식으로 처리했다.
    model = Post
    ordering = '-pk'   # 최근에 온게 가장 먼저띄겠끔


class PostDetail(DetailView):
    model = Post       




from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class Postlist(ListView): #class방식으로 처리했다.
    model = Post
    ordering = '-pk'   # 최근에 온게 가장 먼저띄겠끔


    def get_context_data(self,**kwargs):
        context = super(Postlist,self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()

class PostDetail(DetailView):
    model = Post 

    def get_context_data(self,**kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()      

    def category_page(request, slug): #slug는 일반적으로 이미 얻은 데이터를 사용하여 유효한  url생성하는 방법
        if slug == 'no category':
            sategory = '미분류'
            post_list = Post.objects.filter(category=None)
        else:
            category= Category.objects.get(slug=slug)
            post_list = Post.objects.filter(category=category)

        return render(
            request,
            'blog/post_list.html',
        {
            'post_list':post_list,
            'categories': Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'category': category,
        }    
        )        

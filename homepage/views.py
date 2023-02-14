from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_post = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'homepage/landing.html',  #함수방식으로  렌더링해서 띄운다.
        {
            'recent_post':recent_post,
        }
    )
def about_me(request):
    return render(
        request,
        'homepage/about_me.html'  #어바웃미 탬플릿이 보여 줘라.
    )
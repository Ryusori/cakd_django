from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),  #어바웃미 함수로 가라
    path('',views.landing),  #뷰의 랜딩 함수 떠라

]

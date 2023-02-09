from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()), #
    path('', views.Postlist.as_view()), 
]

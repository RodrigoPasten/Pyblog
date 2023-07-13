from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('post/<slug:slug>', views.post_page, name="post_page"),
    path('tag/<slug:slug>', views.tag_page, name="tag_page"),
    path('autor/<slug:slug>', views.author_page, name="author_page"),
    path('buscar/', views.search_post, name="search"),
    path('accounts/registro/', views.register_user, name='register'),
    path('posteos', views.all_post, name="all_post")
]

from django.urls import path
from .views import *


urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('article/<int:pk>/',ArticleView.as_view(),name='article'),
    path('add/',CreateArticleView.as_view(),name='add'),
    path('edit/<int:pk>/',EditArticle.as_view(),name='edit')

]

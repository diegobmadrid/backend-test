from django.urls import path
from articlesapp import views

urlpatterns = [
    path('save_article',views.save_article, name='save_article'),
    path('get_articles',views.get_articles, name='get_articles'),
]

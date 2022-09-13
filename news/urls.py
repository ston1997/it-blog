from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    # path('', index),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='cat'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='cat'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),

]

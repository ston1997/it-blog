from django.shortcuts import render
from .models import News, Category
from forms import NewsForm


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'список новостей',
        'categories': categories,
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})

def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
from django.db.models import Count

from .models import News

def news(request):
    salomatlik_list = News.published.filter(category__name='Salomatlik').order_by('-publish_time')[:4]
    sayohat_list = News.published.filter(category__name='Sayohat').order_by('-publish_time')[:4]
    ovqat_list = News.published.filter(category__name='Ovqat').order_by('-publish_time')[:4]
    sungi_yangiliklar2 = News.published.all().order_by('-publish_time')[:5]

    ommabop_yangiliklar = News.objects.annotate(hit_count=Count('hit_count_generic__hits')).order_by('-hit_count_generic__hits')[:3]

    # eng ko'p ishlatilgan katehoriyalar
    categories_news = News.objects.all().values('category__name').annotate(new_item_count=Count('category')).order_by('-new_item_count')[:7]

    context ={
        "salomatlik_list":salomatlik_list,
        "sayohat_list":sayohat_list,
        "ovqat_list":ovqat_list,
        "sungi_yangiliklar2":sungi_yangiliklar2,
        "ommabop_yangiliklar":ommabop_yangiliklar,
        "categories_news":categories_news,
    }
    return context
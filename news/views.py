from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from hitcount.utils import get_hitcount_model

from .models import News, Category, Comment
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from .forms import CommentForm
# Create your views here.

class HomePageView(View):
    def get(self, request):
        # sungi_yangiliklar1 = News.published.all().order_by('-publish_time')[:10]
        # sungi_yangiliklar2 = News.published.all().order_by('-publish_time')[10:20]
        sungi_yangiliklar = News.published.all().order_by('-publish_time')
        sungi_yangiliklar2 = News.published.all().order_by('-publish_time')[:5]

        yangiliklar = News.published.all().order_by('-publish_time')[4:]
        yangiliklar1 = News.published.all().order_by('-publish_time')[8:9]
        yangiliklar2 = News.published.all().order_by('-publish_time')[14:15]
        yangiliklar3 = News.published.all().order_by('-publish_time')[11:12]
        mahalliy1 = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[:1]
        jamiyat1 = News.published.all().filter(category__name='Jamiyat').order_by('-publish_time')[:1]
        mahalliy_yangiliklar = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
        jamiyat_yangiliklar = News.published.all().filter(category__name='Jamiyat').order_by('-publish_time')[1:6]
        jahon1 = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[:1]
        jahon2 = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[1:2]
        jahon_yangiliklari1 = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[2:6]
        jahon_yangiliklari2 = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[6:10]
        ovqat = News.published.all().filter(category__name='Ovqat').order_by('-publish_time')[:2]
        sayohat = News.published.all().filter(category__name='Sayohat').order_by('-publish_time')[:2]
        salomatlik = News.published.all().filter(category__name='Salomatlik').order_by('-publish_time')[:2]
        iqtisodiyot = News.published.all().filter(category__name='Iqtisodiyot').order_by('-publish_time')[:1]
        iqtisodiyot_yangiliklar = News.published.all().filter(category__name='Iqtisodiyot').order_by('-publish_time')[1:5]
        madaniyat = News.published.all().filter(category__name='Madaniyat').order_by('-publish_time')[:1]
        madaniyat_yangiliklar = News.published.all().filter(category__name='Madaniyat').order_by('-publish_time')[1:5]
        sport = News.published.all().filter(category__name='Sport').order_by('-publish_time')[:1]
        sport_yangiliklar = News.published.all().filter(category__name='Sport').order_by('-publish_time')[1:5]

        # eng ko'p qoldirilgan comment bo'yicha saralash
        articles = News.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:6]

        # hit count list
        view_sort1 = News.objects.annotate(hit_count=Count('hit_count_generic__hits')).order_by('-hit_count_generic__hits')[:5]
        view_sort2 = News.objects.annotate(hit_count=Count('hit_count_generic__hits')).order_by('-hit_count_generic__hits')[5:10]
        view_sort3 = News.objects.annotate(hit_count=Count('hit_count_generic__hits')).order_by('-hit_count_generic__hits')[10:15]
        view_sort4 = News.objects.annotate(hit_count=Count('hit_count_generic__hits')).order_by('-hit_count_generic__hits')[15:20]

        muharrir_tanlovi1 = News.published.all().filter(category__name='Muharrir tanlovi').order_by('-publish_time')[:1]
        muharrir_tanlovi2 = News.published.all().filter(category__name='Muharrir tanlovi').order_by('-publish_time')[1:6]
        context = {
            # "sungi_yangiliklar1":sungi_yangiliklar1,
            # "sungi_yangiliklar2":sungi_yangiliklar2,
            "sungi_yangiliklar":sungi_yangiliklar,
            "mahalliy1":mahalliy1,
            "mahalliy_yangiliklar":mahalliy_yangiliklar,
            "jamiyat1":jamiyat1,
            "jamiyat_yangiliklar":jamiyat_yangiliklar,
            "jahon1":jahon1,
            "jahon2":jahon2,
            "jahon_yangiliklari1":jahon_yangiliklari1,
            "jahon_yangiliklari2":jahon_yangiliklari2,
            "ovqat":ovqat,
            "sayohat":sayohat,
            "salomatlik":salomatlik,
            "iqtisodiyot":iqtisodiyot,
            "iqtisodiyot_yangiliklar":iqtisodiyot_yangiliklar,
            "madaniyat":madaniyat,
            "madaniyat_yangiliklar":madaniyat_yangiliklar,
            "sport":sport,
            "sport_yangiliklar":sport_yangiliklar,
            "yangiliklar":yangiliklar,
            "yangiliklar1":yangiliklar1,
            "yangiliklar2":yangiliklar2,
            "yangiliklar3":yangiliklar3,
            "articles":articles,
            "view_sort1":view_sort1,
            "view_sort2":view_sort2,
            "view_sort3":view_sort3,
            "view_sort4":view_sort4,

            "muharrir_tanlovi1":muharrir_tanlovi1,
            "muharrir_tanlovi2":muharrir_tanlovi2,
            "sungi_yangiliklar2":sungi_yangiliklar2,
        }
        return render(request, 'news/home.html', context=context)

class SinglePageView(View):
    def get(self, request, news): # get() requestdagi news pastdan kelyapti
        news = get_object_or_404(News, slug=news, status=News.Status.Published)
        cat = news.category
        newss = News.published.all().filter(category__name=cat).order_by('-publish_time')
        comments = news.comments.filter(activate=True)
        form = CommentForm()
        # view count
        context = {}
        hit_count = get_hitcount_model().objects.get_for_object(news)
        hits = hit_count.hits
        hitcontext = context['hitcount'] = {'pk': hit_count.pk}
        hit_count_response = HitCountMixin.hit_count(self.request, hit_count)
        if hit_count_response.hit_counted:
            hits = hits + 1
            hitcontext['hit_counted'] = hit_count_response.hit_counted
            hitcontext['hit_message'] = hit_count_response.hit_message
            hitcontext['total_hits'] = hits

        context = {
            "news":news,
            "newss":newss,
            "form":form,
            "comments": comments,
        }
        return render(request, 'news/single_page.html', context=context)
    def post(self, request, news):
        news = get_object_or_404(News, slug=news, status=News.Status.Published)
        form = CommentForm(data=request.POST)
        cat = news.category
        newss = News.published.all().filter(category__name=cat).order_by('-publish_time')
        comments = news.comments.filter(activate=True)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
        form = CommentForm()
        context = {
            "news":news,
            "newss":newss,
            "form":form,
            "comments": comments,
        }
        return render(request, 'news/single_page.html', context=context)
HitCountDetailView.hit_count_object = News  # Associate the model with hit counting
hitcount_detail = HitCountDetailView.as_view()
class CategoryPageView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'news/category_page.html', context=context)

class SalomatlikPageView(View):
    def get(self, request):
        salomatlik = News.published.filter(category__name='Salomatlik').order_by('-publish_time')
        category_name = "Salomatlik"
        context = {
            "news_list":salomatlik,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class SayohatPageView(View):
    def get(self, request):
        sayohat = News.published.filter(category__name='Sayohat').order_by('-publish_time')
        category_name = "Sayohat"
        context = {
            "news_list":sayohat,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class OvqatPageView(View):
    def get(self, request):
        ovqat = News.published.filter(category__name='Ovqat').order_by('-publish_time')
        category_name = "Ovqat"
        context = {
            "news_list":ovqat,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class MahalliyPageView(View):
    def get(self, request):
        mahalliy = News.published.filter(category__name='Mahalliy').order_by('-publish_time')
        category_name = "Mahalliy"
        context = {
            "news_list":mahalliy,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class JamiyatPageView(View):
    def get(self, request):
        jamiyat = News.published.filter(category__name='Jamiyat').order_by('-publish_time')
        category_name = "Jamiyat"
        context = {
            "news_list":jamiyat,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class JahonPageView(View):
    def get(self, request):
        jahon = News.published.filter(category__name='Jahon').order_by('-publish_time')
        category_name = "Jahon"
        context = {
            "news_list":jahon,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class MadaniyatPageView(View):
    def get(self, request):
        madaniyat = News.published.filter(category__name='Madaniyat').order_by('-publish_time')
        category_name = "Madaniyat"
        context = {
            "news_list":madaniyat,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class SportPageView(View):
    def get(self, request):
        sport = News.published.filter(category__name='Sport').order_by('-publish_time')
        category_name = "Sport"
        context = {
            "news_list":sport,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)
class IqtisodiyotPageView(View):
    def get(self, request):
        iqtisodiyot = News.published.filter(category__name='Iqtisodiyot').order_by('-publish_time')
        category_name = "Iqtisodiyot"
        context = {
            "news_list":iqtisodiyot,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)

class MuharrirPageView(View):
    def get(self, request):
        muharrir = News.published.filter(category__name='Muharrir tanlovi').order_by('-publish_time')
        category_name = "Muharrir tanlovi"
        context = {
            "news_list":muharrir,
            "category_name":category_name,
        }
        return render(request, 'news/category_page.html', context=context)

# Ko'p izoh qoldirilgan larni listi
class IzohPageView(View):
    def get(self, request):
        articles_list = News.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')
        category_name = "Ko'p izoh qoldirilgan"
        context = {
            "news_list":articles_list,
            "category_name":category_name,
        }
        return render(request, "news/category_page.html", context=context)
class AboutPageView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'news/about.html', context=context)

class Page404View(View):
    def get(self, request):
        context = {

        }
        return render(request, 'news/404.html', context=context)



class SerachView(View):
    def get(self, request):
        news_all = News.published.all()
        search_query = request.GET.get('q')
        # bir nechta filter ishlatishimiz uchun Q() dan foydalanmiz
        news = news_all.filter(
            Q(title__icontains=search_query)|Q(body__icontains=search_query)
        )
        context = {
            'news_list':news,
           }
        return render(request, 'news/search.html', context=context)
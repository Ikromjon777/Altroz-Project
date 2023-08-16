from .views import HomePageView, SinglePageView,  CategoryPageView, AboutPageView, Page404View, \
                    SalomatlikPageView, SayohatPageView, OvqatPageView, MahalliyPageView, \
                    JahonPageView, MadaniyatPageView, SportPageView, SerachView, IqtisodiyotPageView,\
                    JamiyatPageView, MuharrirPageView, IzohPageView

from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/<slug:news>/', SinglePageView.as_view(), name='single_page'),
    path('news/', SinglePageView.as_view(), name='single_page1'),
    path('category/', CategoryPageView.as_view(), name='category_page'),
    path('category/salomatlik/', SalomatlikPageView.as_view(), name='salomatlik_page'),
    path('category/sayohat/', SayohatPageView.as_view(), name='sayohat_page'),
    path('category/ovqat/', OvqatPageView.as_view(), name='ovqat_page'),
    path('category/mahalliy/', MahalliyPageView.as_view(), name='mahalliy_page'),
    path('category/jahon/', JahonPageView.as_view(), name='jahon_page'),
    path('category/madaniyat/', MadaniyatPageView.as_view(), name='madaniyat_page'),
    path('category/iqtisodiyot/', IqtisodiyotPageView.as_view(), name='iqtisodiyot_page'),
    path('category/sport/', SportPageView.as_view(), name='sport_page'),
    path('category/jamiyat/', JamiyatPageView.as_view(), name='jamiyat_page'),
    path('category/muharrir-tanlovi/', MuharrirPageView.as_view(), name='muharrir_page'),
    path('category/comment-sorted/', IzohPageView.as_view(), name='izoh_page'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('404/', Page404View.as_view(), name='404_page'),
    path('search/', SerachView.as_view(), name='search'),
]
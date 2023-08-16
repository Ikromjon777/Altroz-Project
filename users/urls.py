from django.urls import path

from .views import ContactPageView, LoginPageView,SignUpPageView, LogoutView, ProfilePageView,\
                    EditProfilePageView

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfilePageView.as_view(), name='profile_page'),
    path('profile/edit/', EditProfilePageView.as_view(), name='edit_profile'),
]
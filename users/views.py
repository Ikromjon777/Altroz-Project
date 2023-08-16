from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import RegisterForm, LoginForm, EditProfileForm, ContactForm


# Create your views here.

class ContactPageView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            "form":form,
        }
        return render(request, 'news/contact.html', context=context)
    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Biz bilan bog'langaningizdan xursandmiz!")
            return redirect('home')
        else:
            context = {
                "form":form,
            }
            return render(request, 'news/contact.html', context=context)

class LoginPageView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form":form,
        }
        return render(request, 'news/login.html', context=context)
    def post(self, request):
        form = LoginForm(data=request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,
                                password=password)  # username mi username ga, passworddi passwordga teng user topilsa
            if user is not None:
                login(request, user)
                messages.success(request, "Muvaffaqiyatli login qildingiz!")
                return redirect('home')
            else:
                messages.info(request, "username yoki parolda xatolik bor!")
                return render(request, 'news/login.html', context=context)
        else:
            return render(request, 'news/login.html', context=context)
class SignUpPageView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            "form":form,
        }
        return render(request, 'news/signup.html', context=context)
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect('login')
        else:
            context = {
                "form":form,
            }
            return render(request, 'news/signup.html', context=context)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz logout qildingiz!!")
        return redirect('home')

class ProfilePageView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        return render(request, 'news/profile.html', context=context)

class EditProfilePageView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        context = {
            "form":form,
        }
        return render(request, 'news/profile_edit.html', context=context)
    def post(self, request):
        form = EditProfileForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlaringiz muvaffaqiyatli o'zgartirildi!")
            return redirect('profile_page')
        else:
            context = {
                "form": form,
            }
            return render(request, 'news/profile_edit.html', context=context)
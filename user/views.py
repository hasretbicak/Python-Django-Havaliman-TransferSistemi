from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from home.models import UserProfile
from product.models import Category
from user.forms import ProfileUpdateForm, UserUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(pk=current_user.id)
    context = {'category': category,
               'profile': profile,
               }
    return render(request, 'user_profile.html', context)

def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Hesabınız Güncellendi.')
            return redirect('/user')

        else:
            category = Category.objects.all()
            user_form = UserUpdateForm(instance=request.user.userprofile)
            profile_form = ProfileUpdateForm(instance=request.user.userprofile)
            context = {
                'category': category,
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, 'user_update.html', context)
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarıyla değiştirildi')
            return HttpResponseRedirect('change_password')
        else:
            messages.error(request, 'Şifreniz Değiştirilirken Hata Oluştu')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
    context = {'form': form,
               'category': category
               }
    return render(request, 'change_password.html', context)


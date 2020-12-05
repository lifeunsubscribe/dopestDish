from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from reviews.models import Review

def signup_view(request,*args,**kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'profiles/register.html', {'form': form})

@login_required
def profile(request):
    print(request.method)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        reviewList = Review.objects.filter(author=request.user).order_by('-date_posted')
        print(reviewList)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'reviewList':reviewList

    }
    return render(request, 'profiles/profile.html', context)

def deleteReview_view(request,id):
    print(request.method)
    print(id)
    Review.objects.get(id=id).delete()
    return profile(request)

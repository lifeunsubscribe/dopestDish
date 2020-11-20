from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

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
    return render(request, 'profiles/profile.html')
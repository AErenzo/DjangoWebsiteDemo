from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from user_app.forms import UserForm


# Create your views here.
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse('User Account not Active')
        else:
            print(f'Login failed - username: {username}, password: {password}')
            return HttpResponse('Login Failed - Please try again or register if you do not have an account.')
    else:
        return render(request, 'user_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            # set the password as an actual password - django hashes this pw
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm

    return render(request, 'user_app/register.html', {'user_form': user_form,
                                                      'registered': registered})


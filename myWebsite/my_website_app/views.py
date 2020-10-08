from django.shortcuts import render
from my_website_app.forms import UserEnquiriesForm

# Create your views here.


def landing(request):
    return render(request, 'my_website_app/landing.html')


def index(request):
    return render(request, 'my_website_app/index.html')


def contact(request):

    submitted = False

    if request.method == 'POST':

        form = UserEnquiriesForm(request.POST)

        if form.is_valid:
            form.save(commit=True)

            submitted = True
    else:
        form = UserEnquiriesForm()

    return render(request, 'my_website_app/contact.html', {'form': form,
                                                           'submitted': submitted})


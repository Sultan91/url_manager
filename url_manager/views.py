from django.shortcuts import render
from .models import Url
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UrlForm
# Create your views here.


def index(request):
    user_id = None
    user_name = None
    #print(request.user)
    #print(request.user.is_authenticated)
    if request.user.is_authenticated:
        user_id = request.user.id
        user_name = request.user
    if request.method == 'POST' and request.user.is_authenticated:
        form = UrlForm(request.POST, request)
        if form.is_valid():
            url_data = form.save(commit=False)
            url_data.person = request.user
            url_data.save()
    elif request.method == 'GET':
        form = UrlForm()

    if user_id is not None:
        try:
            urls_ = Url.objects.filter(person=request.user)
        except Url.DoesNotExist:
            urls_ = ''
        #print("URLS: ", urls_)
        context = {'urls': urls_,
                   'username': user_name,
                   'form': form}
        return render(request, 'index.html', context=context)
    else:
        context = {'urls': [], 'username': ''}
        return render(request, 'index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def add_url(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        #print(form)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            cd = form.cleaned_data

            return render(request, 'index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()

    return render(request, 'index.html', {'form': form})
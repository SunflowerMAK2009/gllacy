from django.shortcuts import render, redirect
from catalog.models import Product
from .forms import EmailForm, PopupForm, SearchForm

def home_view(request):
    products = Product.objects.all()
    hits = products.filter(hit=True)
    return render(request, 'home/home.html', context={"hits": hits})

def thanks_view(request):
    return render(request, 'home/thanks.html')

def email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["email"])
            return redirect("thanks_url")
        else:
            print(form.errors.as_text())
            # print(form.errors)
            # return render(request, 'home.html', context={'errors': form.errors})
        return redirect("home_url")
def popup_view(request):
    if request.method == 'POST':
        form = PopupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["comment"])
            return redirect("thanks_url")
        else:
            print(form.errors.as_text())
        return redirect("home_url")

def search(request):
    products = Product.objects.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_products = products.filter(name__icontains=form.cleaned_data['search_value'])
            return render(request, 'home/search.html', context={'products': search_products})
        else:
            print(form.errors.as_text())
        return render(request, 'home/search.html')
from . forms import User_form
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main/index.html")

def products(request):
    return render(request, "main/products.html")

def product_unit(request):
    return render(request, "main/product-unit.html")

def contacts(request):
    user_form = User_form()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        topic = request.POST.get("topic")
        comment = request.POST.get("comment")
        return HttpResponse("{0}{1}{2}{3}".format(name, email, topic, comment))
    else:
        return render(request, "main/contacts.html", {"form":user_form})
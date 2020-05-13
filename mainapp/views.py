from json import load
from datetime import datetime

from django.shortcuts import render


def main(request):
    title = "home"
    with open('static/data/products.json') as file:
        products = load(file)
    content = {"title": title, "products": products}
    return render(request, 'mainapp/index.html', content)


def products(request):
    title = 'products'
    links_menu = [
        {"href": "products_all", "name": "все"},
        {"href": "products_home", "name": "дом"},
        {"href": "products_office", "name": "офис"},
        {"href": "products_modern", "name": "модерн"},
        {"href": "products_classic", "name": "классика"},
    ]
    with open('static/data/similar_products.json') as file:
        similar_products = load(file)

    content = {"title": title, "links_menu": links_menu, "similar_products": similar_products}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'about'
    visit_date = datetime.now()
    content = {'title': title, 'visit_date': visit_date}
    return render(request, 'mainapp/contact.html', content)

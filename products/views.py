from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_http_methods, 
    require_POST,
)
import re
from .forms import ProductsForm
from .models import ProductImages, HashTags, Products

# Create your views here.
def home(request):
    
    return render(request, "products/index.html")

@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            products = form.save(commit=False)
            products.owenr = request.user
            products.save()
            for file in request.FILES.getlist('images'):
                pfile = ProductImages.objects.create(image=file)
                products.p_images.add(pfile.pk)
            for hash_tag in list(request.POST.get('hash_tags').replace(" ","").split(',')):
                hash_tag = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', hash_tag)
                if hash_tag == "": continue
                if len(HashTags.objects.filter(tag_name=hash_tag)) == 0:
                    HashTags.objects.create(tag_name=hash_tag)
                hashtag = get_object_or_404(HashTags, tag_name=hash_tag)
                products.p_hashtags.add(hashtag.pk)
            return redirect("products:detail", products.pk)
    else:
        form = ProductsForm()
    context ={
        'form': form,
    }
    return render(request, "products/create.html", context)


def detail(request, product_pk):
    product = get_object_or_404(Products, pk=product_pk)
    context = {
        "product": product,
    }
    return render(request, "products/detail.html", context)
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
    products = Products.objects.all().order_by('-pk')
    context = {
        'products': products,
    }
    return render(request, "products/index.html", context)

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
                ProductImages.objects.create(image=file, i_products=products)
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


@require_http_methods(['GET', 'POST'])
def update(request, product_pk):
    product = get_object_or_404(Products, pk=product_pk)
    if request.user.pk != product.owenr.pk:
        return redirect("products:detail", product_pk)
    
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            for file in request.FILES.getlist('images'):
                ProductImages.objects.create(image=file, i_products=product)
            for hash_tag in list(request.POST.get('hash_tags').replace(" ","").split(',')):
                hash_tag = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', hash_tag)
                if hash_tag == "": continue
                if len(HashTags.objects.filter(tag_name=hash_tag)) == 0:
                    HashTags.objects.create(tag_name=hash_tag)
                hashtag = get_object_or_404(HashTags, tag_name=hash_tag)
                if product.p_hashtags.filter(pk=hashtag.pk).exists():
                    product.p_hashtags.remove(hashtag.pk)
                else:
                    product.p_hashtags.add(hashtag.pk)
            return redirect("products:detail", product.pk)
    else:
        form = ProductsForm(instance=product)
        hashtag = ''
        for tag in product.p_hashtags.all():
            hashtag += tag.tag_name + ', '
        files = product.p_images.all()
    context = {
        "form": form,
        "product": product,
        "hashtag": hashtag,
        "files": files,
    }
    return render(request, "products/update.html", context)


@require_POST
def delete_imag(request, image_pk):
    image = get_object_or_404(ProductImages, pk=image_pk)
    if request.user.pk != image.i_products.owenr.pk:
        return redirect("products:detail", image.i_products.pk)
    else:
        image.delete()
    return redirect("products:update", image.i_products.pk)



@require_POST
def delete(request, product_pk):
    Product = get_object_or_404(Products, pk=product_pk)
    if request.user.pk != Product.owenr.pk:
        return redirect("products:detail", Product.pk)
    else:
        Product.delete()
    return redirect("home")
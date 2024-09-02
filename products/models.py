from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class HashTags(models.Model):
    tag_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.PositiveIntegerField()
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owenr = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="u_products")
    p_hashtags = models.ManyToManyField(HashTags, related_name="h_products")
    like_users = models.ManyToManyField(get_user_model(), related_name="like_products")


class ProductImages(models.Model):
    image = models.ImageField(upload_to="pimages/")
    i_products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="p_images")
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    product = models.ManyToManyField(Products, related_name="p_carts")
    user = models.ManyToManyField(get_user_model(), related_name="u_carts")
    cnt = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

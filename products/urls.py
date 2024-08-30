from django.urls import path
from products import views


app_name="products"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("detail/<int:product_pk>", views.detail, name="detail"),
    
]

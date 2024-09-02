from django.urls import path
from products import views


app_name="products"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("detail/<int:product_pk>/", views.detail, name="detail"),
    path("update/<int:product_pk>/", views.update, name="update"),
    path("delete/<int:product_pk>/", views.delete, name="delete"),
    path("update_view/<int:product_pk>/", views.update_view, name="update_view"),
    path("like_product/<int:product_pk>/", views.like_product, name="like_product"),
    path("delete_imag/<int:image_pk>/", views.delete_imag, name="delete_imag"),
    path("cart-list/", views.cart_list, name="cart_list"),
    path("cart/<int:product_pk>/", views.cart_create, name="cart_create"),
    path("cart-update/", views.cart_update, name="cart_update"),
    path("cart-delete/", views.cart_delete, name="cart_delete"),
    
]
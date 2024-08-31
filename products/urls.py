from django.urls import path
from products import views


app_name="products"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("detail/<int:product_pk>/", views.detail, name="detail"),
    path("update/<int:product_pk>/", views.update, name="update"),
    path("delete_imag/<int:image_pk>/", views.delete_imag, name="delete_imag"),
    
]

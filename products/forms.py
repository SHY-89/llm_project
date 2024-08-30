from .models import Products
from django import forms

class ProductsForm(forms.ModelForm):
    
    class Meta:
        model = Products
        fields = ("title", "content", "price")
        labels = {
            "title": "제목",
            "content": "상세설명",
            "price": "가격",
        }

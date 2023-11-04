from django.views.generic.list import ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"  # Создайте этот шаблон
    context_object_name = "products"
    paginate_by = 10  # Количество товаров на одной странице

    def get_queryset(self):
        return Product.objects.all().order_by("name")

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import generic

from Account.views import user_login
from Product.models import Product, Category


class IndexView(generic.ListView):
    template_name = 'Product/index.html'
    context_object_name = "products"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        current_year = timezone.now().day
        context['product'] = Product.objects.filter(pub_date__day=current_year)
        # And so on for more models
        return context


class ProductDetails(generic.DetailView):
    template_name = 'Product/product_detail.html'
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductDetails, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # And so on for more models
        return context

        # return get_object_or_404(Product, pk=request.session['product_id'])

    # def get_object(self):
    #     return get_object_or_404(Product, pk=self.product_id)


class CategoryPage(generic.DetailView):
    template_name = "Product/category.html"
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryPage, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # And so on for more models
        return context

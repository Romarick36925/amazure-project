from django.views import generic

from Product.models import Category


class IndexView(generic.ListView):
    template_name = 'amazure/base.html'
    model = Category
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.all()
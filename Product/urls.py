from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'Product'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detailview/(?P<pk>\d+)/', views.ProductDetails.as_view(), name='product_details'),
    url(r'^categoryview/(?P<pk>\d+)/', views.CategoryPage.as_view(), name='category_page'),
]

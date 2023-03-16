from django.contrib.auth.decorators import login_required
from django.urls import path

from products.apps import ProductsConfig
from products.views import contacts, ProductView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductUpdateWithVersionView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),

    path('list/', ProductListView.as_view(), name='list'),
    path('create/', login_required(ProductCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(ProductUpdateView.as_view()), name='update'),
    path('update/<str:pk>/version/', login_required(ProductUpdateWithVersionView.as_view()), name='update_with_version'),
    path('delete/<str:pk>/', login_required(ProductDeleteView.as_view()), name='delete'),

]

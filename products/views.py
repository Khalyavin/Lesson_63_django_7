from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from products.forms import ProductForm, VersionForm
from products.models import Product, Version

def contacts(request):
    return render(request, 'products/contacts.html')


class ProductView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'products/index.html'


class ProductListView(LoginRequiredMixin, ListView):
    #    queryset = Product.objects.filter(published=Blog.STATUS_ACTIVE).all()
    model = Product
    form_class = ProductForm
    template_name = 'products/list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list', )
    extra_context = {
        'title': 'Создание некоего продукта'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list', )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
    template_name = 'products/product_with_versions.html'

    def get_success_url(self):
        return reverse('product:detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print(self.request.method)
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)

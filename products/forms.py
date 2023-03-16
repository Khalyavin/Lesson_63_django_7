from django import forms

from products.models import Product, Version
from products.forms_mixins import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_modification(self):
        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        modification = self.cleaned_data['modification']

        for word in forbidden_words:
            if word in modification:
                raise forms.ValidationError(f'Слово {word} запрещено на сайте')

        return modification

class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'title', 'release_date')

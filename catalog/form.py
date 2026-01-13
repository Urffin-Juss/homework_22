from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта",
    "биржа", "дешево", "бесплатно",
    "обман", "полиция", "радар",

]


def contains_forbidden_words(text: str) -> list(str):
    if not text:
        return []
    low = text.lower()
    found = [w for w in FORBIDDEN_WORDS if w in low]
    return found

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

    fields = ("name", "description", "image", "category", "price", "created_at", "updated_at")

    widgets = {
        "description": forms.Textarea(attrs={"rows": 5}),
    }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = field.widget.attrs.get("class", "")
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = (css + " form-check-input").strip()
            else:
                field.widget.attrs["class"] = (css + " form-control").strip()


            field.widget.attrs.setdefault("placeholder", field.label)

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name", "")
        description = cleaned_data.get("description", "")

        bad_in_name = contains_forbidden(name)
        bad_in_desc = contains_forbidden(description)
        bad = sorted(set(bad_in_name + bad_in_desc))

        if bad:
            raise ValidationError(
                f"Нельзя использовать запрещённые слова: {', '.join(bad)}"
            )

        return cleaned_data


    def clean_price(self):
        price = self.cleaned_data.get("price")


        if price is None:
            return price

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price



from django import forms
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта",
    "биржа", "дешево", "бесплатно",
    "обман", "полиция", "радар",

]
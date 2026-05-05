from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


COMMON_NUMBER_ATTRS = {
    "class": "input-field",
    "step": "0.00000000000001",
}


def build_prediction_form(fields):
    form_fields = {}
    for index, field in enumerate(fields, start=1):
        form_fields[f"field{index}"] = forms.FloatField(
            label=field["label"],
            widget=forms.NumberInput(
                attrs={
                    **COMMON_NUMBER_ATTRS,
                    "placeholder": field.get("placeholder", ""),
                }
            ),
        )

    return type("PredictionForm", (forms.Form,), form_fields)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Choose a username"}),
        }

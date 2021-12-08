from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, FirstOrder, SecondOrder
from django import forms
from django.forms.widgets import NumberInput, Widget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


PAYMENT_OPTIONS = (
    ('P', 'PayPal'),
    ('MS', 'MasterCard'),
    ('S', 'Swift')
)


class PaymentForm(forms.Form):
    card_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "card_name",
            "placeholder": "Name",

        })
    )
    card_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'card_number',
                'placeholder': 'Card_number',
            }
        )
    )


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, widget=(forms.TextInput(
        attrs={
            'placeholder': 'Your Name',
            'class': 'form-control',
            'name': 'name',
            'id': 'name'
        }
    )), required=True)
    email = forms.EmailField(max_length=100, widget=(forms.EmailInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
        }
    )), required=True)
    subject = forms.CharField(max_length=200, widget=(forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'name': 'subject',
            'ide': 'subject',
            'placeholder': 'Subject'
        }
    )))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'name': 'message',
            'rows': '5',
            'placeholder': 'Enter your message'
        }
    ))


COMPLEXITY_CHOICES = (
    ('HG', 'High School'),
    ('CL', 'College'),
    ('UG', 'Undergraduate'),
    ('MS', 'Masters'),
    ('PHD', 'PhD')
)

TYPE_OF_WORK = (
    ('AE', 'Admission Essay'),
    ('Bio', 'Biographies'),
    ('BP', 'Business Plan'),
    ('BR', 'Book Review')
)
DEADLINE = (
    ('14D', '14 Days'),
    ('10D', '10 Days'),
    ('7D', '7 Days'),
    ('6D', '6 Days'),
    ('5D', '5 Days'),
    ('4D', '4 Days'),
    ('3D', '3 Days'),
    ('2D', '2 Days'),
    ('1D', '1 Days'),
    ('20H', '20 Hours'),
    ('16H', '16 Hours'),
    ('12H', '12 Hours'),
    ('8H', '8 Hours'),
    ('6H', '6 Hours'),
    ('5H', '5 Hours'),
    ('3H', '3 Hours'),
    ('2H', '2 Hours'),
)


class FormOrderOne(forms.ModelForm):
    class Meta:
        model = FirstOrder
        fields = '__all__'
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class FormOrderTwo(forms.ModelForm):
    class Meta:
        model = SecondOrder
        fields = '__all__'
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

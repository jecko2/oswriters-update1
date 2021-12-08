from django.urls import path
from .views import (
        SignUpForm,
        home,
        ViewFormOrder,
        ContactUsFormView,
        ViewFormOrder2,
        )
urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpForm.as_view(), name="signup"),
    path('place-order/', ViewFormOrder.as_view(), name='place-order'),
    path('contact-us/', ContactUsFormView.as_view(), name='contact-us'),
    path('place-order/commit/', ViewFormOrder2.as_view(), name='commit'),
]

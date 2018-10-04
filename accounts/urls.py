from django.conf.urls import url

from .views import (
    AccountHomeView,
    AccountEmailActivateView
)

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^email/confirm/(?P<key>[0-9a-zA-Z]+)/$', AccountEmailActivateView.as_view(), name='email-activate')
]

# account/email/confirm/kedasfsad/ -> activation view

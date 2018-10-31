from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GoToTransaction, name='Home'),
    #url(r'^$', views.payment, name='Home'),
    #  url(r'^GoToTransaction$', views.GoToTransaction, name='GoToTransaction'),
    url(r'^GoToTransaction/$', views.GoToTransaction, name='GoToTransaction'),
    # url(r'^failure/$', views.TransactionFailure, name='failure'),
    # url(r'^cancellation/$', views.TransactionCancellation, name='success'),
    #url(r'^$', views.payment, name="payment"),
    #url(r'^success/$', views.payment_success, name="payment_success"),
    #url(r'^failure/$', views.payment_failure, name="payment_failure"),
    url(r'^success/$', views.success, name="success"),
    url(r'^Failure/$', views.failure, name="failure"),
]
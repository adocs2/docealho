from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sobre$', views.AboutView.as_view(), name='sobre'),
    url(r'^blog$', views.BlogView.as_view(), name='blog'),
    url(r'^leiamais(?P<pk>[0-9]+)$', views.ReadMoreView.as_view(), name='leiamais'),
    url(r'^contato$', views.emailView, name='contato/'),
]

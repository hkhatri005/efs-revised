from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as efs_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'efs'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/<int:pk>/view/', views.customer_view, name='customer_view'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/myedit/', views.investment_myedit, name='investment_myedit'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('investment/<int:pk>/mylist/', views.investment_mylist, name='investment_mylist'),
    url(r'^mutualfund_list/$', views.mutualfund_list, name='mutualfund_list'),
    url(r'^mutualfund/(?P<pk>\d+)/delete/$', views.mutualfund_delete, name='mutualfund_delete'),
    url(r'^mutualfund/(?P<pk>\d+)/edit/$', views.mutualfund_edit, name='mutualfund_edit'),
    url(r'^mutualfund/create/$', views.mutualfund_new, name='mutualfund_new'),
    url(r'^mutualfund/(?P<pk>\d+)/mylist/$', views.mutualfund_mylist, name='mutualfund_mylist'),
    path('mutualfund/<int:pk>/myedit/', views.mutualfund_myedit, name='mutualfund_myedit'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('stock/<int:pk>/mylist/', views.stock_mylist, name='stock_mylist'),
    path('stock/<int:pk>/myedit/', views.stock_myedit, name='stock_myedit'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    path('customer/<int:pk>/personal_portfolio/', views.personal_portfolio, name='personal_portfolio'),



]
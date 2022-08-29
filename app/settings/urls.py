from django.contrib import admin
from django.urls import path, include
from currency import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]

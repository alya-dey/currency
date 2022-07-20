from django.contrib import admin
from django.urls import path
from currency.views import contacts_responses, rate_list, index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('contacts-responses/', contacts_responses),
    path('rate/list/', rate_list),
]

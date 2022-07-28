from django.contrib import admin
from django.urls import path
from currency.views import contacts_responses, rate_list, index, rate_create, source_list, \
    rate_update, rate_details, rate_delete, source_create, source_update, source_delete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('contacts-responses/', contacts_responses),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:rate_id>', rate_update),
    path('rate/details/<int:rate_id>', rate_details),
    path('rate/delete/<int:rate_id>', rate_delete),
    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:source_id>', source_update),
    path('source/delete/<int:source_id>', source_delete),

]

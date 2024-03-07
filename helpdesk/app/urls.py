from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:id>', views.ticket, name='ticket'),
    path('edit-ticket/<int:id>', views.editticket, name='editticket'),
]
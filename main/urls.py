from django.urls import path
from . import views
from main.views import show_main, create_additional_entry, show_xml

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-additional-entry', create_additional_entry, name='create_additional_entry'),
    path('xml/', show_xml, name='show_xml'),
]
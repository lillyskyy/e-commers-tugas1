from django.urls import path
from . import views
from main.views import show_main, create_additional_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, add_additional_entry_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_additional
from main.views import delete_additional

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-additional-entry', create_additional_entry, name='create_additional_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-additional/<uuid:id>', edit_additional, name='edit_additional'),
    path('delete-additional/<uuid:id>', views.delete_additional, name='delete_additional'),
    path('create-additional-entry-ajax', add_additional_entry_ajax, name='add_additional_entry_ajax'),
]
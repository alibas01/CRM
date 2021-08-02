from django.urls import path
from .views import *

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='home'),
    path('<int:pk>/', lead_detail, name='detail'),
    path('<int:pk>/update', lead_update, name='update'),
    path('create/', lead_create, name='create')
]
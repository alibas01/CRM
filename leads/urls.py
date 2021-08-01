from django.urls import path
from .views import *

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='home'),
    path('<pk>/', lead_detail, name='detail')
]
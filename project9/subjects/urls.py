from django.urls import path
from .views import get_all, get_by_index

urlpatterns = [
    path('all/', get_all),
    path('<int:sub_id>', get_by_index)
]

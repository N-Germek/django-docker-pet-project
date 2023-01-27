from django.urls import path
from .views import PetsList, PetDetail


urlpatterns = [
    path('', PetsList.as_view(), name='pets_list'),
    path('<int:pk>/', PetDetail.as_view(), name='pets_detail'),
]

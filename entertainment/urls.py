from django.urls import path
from .views import (
    CreateEntertainment, ListEntertainment, UpdateEntertainment,
    FinishEntertainment, DetailEntertainment,DeleteEntertainment
)

app_name = "entertainment"

urlpatterns = [
    path('', ListEntertainment.as_view(), name= 'home_entertainment'),
    path('create/', CreateEntertainment.as_view(), name='create_entertainment'),
    path('update/<int:pk>/', UpdateEntertainment.as_view(), name='update_entertainment'),
    path('finsh/<int:pk>/', FinishEntertainment.as_view(), name='finish_entertainment'),
    path('detail/<int:pk>/', DetailEntertainment.as_view(), name='detail_entertainment'),
    path('delete/<int:pk>/', DeleteEntertainment.as_view(), name='delete_entertainment'),
]
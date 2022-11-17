from django.urls import path
from .views import (
        CreateUser, LoginUser, LogoutUser, UpdateUser, DeleteUser, HomeUser
    )

app_name = "accounts"

urlpatterns = [
    path('', HomeUser.as_view(), name= 'home_user'),
    path('create/', CreateUser.as_view(), name='create_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
    path('update/', UpdateUser.as_view(), name='update_user'),
    path('delete/', DeleteUser.as_view(), name='delete_user'),
]
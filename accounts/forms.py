from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CreationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('name', 'email',)

class ChangeUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('name', 'email',)
        
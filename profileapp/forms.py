from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Mate:
        model = Profile
        field = ['image', 'nickname', 'message']


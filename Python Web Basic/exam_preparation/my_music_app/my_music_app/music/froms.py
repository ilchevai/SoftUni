from django import forms

from my_music_app.music.models import Profile, Album


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'age': forms.NumberInput()
        }


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'artist': forms.TextInput(),
            'genre': forms.Select(),
            'descriptions': forms.TextInput(),
            'image_url': forms.URLInput(),
            'price': forms.NumberInput()
        }


class AlbumDeleteForm(AlbumModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attr = {
                'readonly': 'readonly'
            }



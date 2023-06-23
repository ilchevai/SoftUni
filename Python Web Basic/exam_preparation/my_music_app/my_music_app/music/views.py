from django.shortcuts import render, redirect

from my_music_app.music.froms import ProfileModelForm, AlbumModelForm, AlbumDeleteForm
from my_music_app.music.models import Profile, Album


# Create your views here.
def index(request):
    profile = Profile.objects.first()
    album = Album.objects.all().order_by('id')

    if profile:
        template_name = 'home-with-profile.html'
    else:
        template_name = 'home-no-profile.html'

    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileModelForm()
    context = {
        'form': form,
        'profile': profile,
        'albums': album
    }

    return render(request, template_name, context)


def add_album(request):
    albums = Album.objects.all()

    if request.method == 'POST':
        form = AlbumModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AlbumModelForm()

    context = {
        'form': form,
        'albums': albums
    }

    return render(request, template_name='add-album.html', context=context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, template_name='album-details.html', context=context)


def edit_album(request, pk):

    album = Album.objects.filter(pk=pk).get()
    form = AlbumModelForm(instance=album)

    if request.method == 'POST':
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'edit_form': form,
        'album': album
    }

    return render(request, template_name='edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumDeleteForm(instance=album)

    if request.method == 'POST':
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect('home page')

    context = {
        'form': form,
        'album': album
    }
    return render(request, template_name='delete-album.html', context=context)


def details_profile(request):
    profile = Profile.objects.first()
    all_albums = len(Album.objects.all())

    context = {
        'profile': profile,
        'all_albums': all_albums
    }
    return render(request, template_name='profile-details.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        return redirect('home page')
    context = {
        'profile': profile
    }

    return render(request, template_name='profile-delete.html', context=context)

from django.shortcuts import render


# Create your views here.

def add_photos(request):
    return render(request, template_name='photos/photo-add-page.html')


def details_photo(request):
    return render(request, template_name='photos/photo-details-page.html')


def edit_photo(request):
    return render(request, template_name='photos/photo-edit-page.html')




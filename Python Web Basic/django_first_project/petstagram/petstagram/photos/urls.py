from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photos, name='add-photos'),
    path('photos/<int:pk>/', include([
        path('', views.details_photo, name='pet-photo'),
        path('edit/', views.edit_photo, name='photo-edit'),
    ])),
]

from django.urls import path

from my_music_app.music import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('album/add/', views.add_album, name='add album'),
    path('album/details/<int:pk>/', views.details_album, name='details album'),
    path('album/edit/<int:pk>/', views.edit_album, name='edit album'),
    path('album/delete/<int:pk>/', views.delete_album, name='delete album'),
    path('profile/details/ ', views.details_profile, name='details profile'),
    path('profile/delete/ ', views.delete_profile, name='delete profile'),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name = 'home'),
    path('display-artists', views.indexArtist, name = 'index-artist'),
    path('upload-artist/', views.uploadArtist, name = 'create-artist'),
    path('update-artist/<int:artist_id>', views.update_Artist),
    path('delete-artist/<int:artist_id>', views.delete_Artist),
    path('display-artworks', views.indexArtwork, name = 'index-artworks'),
    path('upload-artwork/', views.uploadArtwork, name = 'create-artworks'),
    path('update-artwork/<int:artwork_id>', views.update_Artwork),
    path('delete-artwork/<int:artwork_id>', views.delete_Artwork)
]


from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Artist, Artwork
from django.http import HttpResponse
from .forms import CreateArtist, CreateArtwork

# HOME PAGE FUNCTIONS
def index(request):
    return render(request, 'index.html')


# ARTIST VIEW FUNCTIONS
def indexArtist(request):
    artists = Artist.objects.all()
    return render(request, 'artist/display-artists.html', {'artists': artists})

def uploadArtist(request):
    upload = CreateArtist()
    if request.method == 'POST':
        upload = CreateArtist(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index-artist')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index-artist'}}">reload</a>""")
    else:
        return render(request, 'artist/upload_form_artists.html', {'upload_form':upload})

def update_Artist(request, artist_id):
    artist_id = int(artist_id)
    try:
        artist_sel = Artist.objects.get(id = artist_id)
    except Artist.DoesNotExist:
        return redirect('index-artist')
    artist_form = CreateArtist(request.POST or None, instance = artist_sel)
    if artist_form.is_valid():
       artist_form.save()
       return redirect('index-artist')
    return render(request, 'artist/upload_form_artists.html', {'upload_form':artist_form})

def delete_Artist(request, artist_id):
    artist_id = int(artist_id)
    try:
        artist_sel = Artist.objects.get(id = artist_id)
    except Artist.DoesNotExist:
        return redirect('index-artist')
    artist_sel.delete()
    return redirect('index-artist')

# ARTWORK VIEW FUNCTIONS
def indexArtwork(request):
    artworks = Artwork.objects.all()
    return render(request, 'artworks/display-artworks.html', {'artworks': artworks})

def uploadArtwork(request):
    upload = CreateArtwork()
    if request.method == 'POST':
        upload = CreateArtwork(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index-artworks')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index-artworks'}}">reload</a>""")
    else:
        return render(request, 'artworks/upload_form_artworks.html', {'upload_form':upload})

def update_Artwork(request, artwork_id):
    artwork_id = int(artwork_id)
    try:
        artwork_sel = Artwork.objects.get(id = artwork_id)
    except Artwork.DoesNotExist:
        return redirect('index-artworks')
    artwork_form = CreateArtwork(request.POST or None, request.FILES or None, instance=artwork_sel)
    if artwork_form.is_valid():
       artwork_form.save()
       return redirect('index-artworks')
    return render(request, 'artworks/upload_form_artworks.html', {'upload_form':artwork_form})

def delete_Artwork(request, artwork_id):
    artwork_id = int(artwork_id)
    try:
        artwork_sel = Artwork.objects.get(id = artwork_id)
    except Artwork.DoesNotExist:
        return redirect('index-artworks')
    artwork_sel.delete()
    return redirect('index-artworks')

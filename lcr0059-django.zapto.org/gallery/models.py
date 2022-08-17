from django.db import models

"""Data model #1: Artist
Data fields:
first_name (charfield, max length 40)
last_name (charfield, max length 40)
location (charfield, max length 40)  -- (town/city the artist lives in)
primary_media (charfield, max length 40)  -- (main types of work the artist produces, such as painting, sculpture)"""

class Artist(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    location = models.CharField(max_length = 40)
    primary_media = models.CharField(max_length = 40)
    def __str__(self):
        return self.first_name + " " + self.last_name

"""Data model #2: Artwork
Data fields:
artwork_name (charfield, max length 40)
media_type (charfield, max length 40) -- examples: painting, sculpture
completion_date (date)
price
note
Also allow one image of each artwork to be uploaded"""

class Artwork(models.Model):
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    media_type = models.CharField(max_length=40)
    completion_date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='media')

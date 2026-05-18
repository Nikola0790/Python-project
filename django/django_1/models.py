from django.db import models

GENRE_OPTIONS = ((-1, 'not defined'), (0, "rock"), (1, 'metal'), (2, 'pop'), (3, 'hip-hop'), (4, 'electronic'), (5, 'reggae'), (6, 'other'))
class Band(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRE_OPTIONS, default=-1)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    SCALE = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))

    album_title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    rating = models.IntegerField(choices=SCALE, default=0)

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)

class Article(models.Model):
    STATUS_CHOICES = (
        ('in writing', 'in writing'),
        ('pending editor approval', 'pending editor approval'),
        ('published', 'published'),
    )
    
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, 
        choices=STATUS_CHOICES, 
        default='in writing'
    )
    publish_date = models.DateField(null=True, blank=True)
    removal_date = models.DateField(null=True, blank=True)

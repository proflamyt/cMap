from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import PolygonField
from django.conf import settings
from django.db.models.fields import URLField
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=30)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null=True, blank=True)

class Novel(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, blank=True)
    map = URLField(null=True, blank=True)
    def get_absolute_url(self):    
        return reverse('index', args=[str(self.id)])
    def get_map_url(self):    
        return reverse('store', args=[str(self.id)])


class Maptype(models.Model):
    name = models.CharField(max_length=30)
    novel = models.ForeignKey(Novel,on_delete=models.CASCADE, null=True, blank=True)
    def get_absolute_url(self):    
        return reverse('points', args=[str(self.novel_id), str(self.id)])
    class Meta:
        unique_together = (('name', 'novel'),)
    def __str__(self) -> str:
        return self.name


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = models.PointField()
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null=True, blank=True)
    type  = models.ForeignKey(Maptype,blank=True,null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    novel = models.ForeignKey(Novel,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Return string representation."""
        return self.name





class Area(models.Model):
    name = models.CharField(max_length=255)
    location = PolygonField()
    description = models.TextField()
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,null=True, blank=True)
    novel = models.ForeignKey(Novel,on_delete=models.CASCADE, null=True, blank=True)
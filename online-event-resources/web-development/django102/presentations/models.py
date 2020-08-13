from django.db import models
from django.urls import reverse

class Speaker(models.Model):
    name = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.title

class Presentation(models.Model):
    title = models.CharField(max_length=40, blank=False)
    abstract = models.TextField(blank=False)
    track = models.ForeignKey(Track, on_delete=models.PROTECT)
    speaker = models.ForeignKey(Speaker, on_delete=models.PROTECT)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

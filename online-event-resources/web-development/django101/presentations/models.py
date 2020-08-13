from django.db import models

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(blank=False, max_length=100)
    def __str__(self):
        return self.name

class Presentation(models.Model):
    title = models.CharField(blank=False, max_length=100)
    abstract = models.TextField(blank=False)
    speaker = models.ForeignKey(Speaker, models.PROTECT)
    def __str__(self):
        return self.title
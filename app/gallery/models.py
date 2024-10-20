from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()
    public_id = models.CharField(max_length=255, default='', null=True)

    def __str__(self):
        return self.title

from django.db import models

class Staff(models.Model):
    role = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    bibliography = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

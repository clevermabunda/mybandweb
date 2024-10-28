from django.db import models

# Create your models here.
class Band(models.Model):
    band_name = models.CharField(max_length=50)
    number_of_members = models.IntegerField()
    year_formed = models.DateField()
    genre = models.CharField(max_length=50)
    about_the_band = models.CharField(max_length=10000, null=True)

    def __str__(self) -> str:
        return self.band_name
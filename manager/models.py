from django.db import models

# Create your models here.
class uploadmodel(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    description = models.CharField(max_length=600)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    class Meta:
        db_table='uploadnews'


class viewdetailsmodel(models.Model):
    #category = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    #file = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review = models.CharField(max_length=200)

    class Meta:
        db_table='viewdetailsmodel'

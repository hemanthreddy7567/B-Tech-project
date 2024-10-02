from django.db import models

# Create your models here.

class users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique='True')
    password = models.CharField(max_length=40)
    conformpassword = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.email
    class Meta:
        db_table='userregister'




class viewdetailsmodel(models.Model):
    #category = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review = models.CharField(max_length=200)

    class Meta:
        db_table='userviewdetailsmodel'

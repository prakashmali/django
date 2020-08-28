from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.restaurant_name



class Dises(models.Model):
    res_id=models.CharField(max_length=10)
    dises_name=models.CharField(max_length=20)
    dises_price=models.FloatField()

    def __str__(self):
        return self.dises_name


class Transaction(models.Model):
    res_id=models.CharField(max_length=10)
    dises=models.CharField(max_length=20)
    date=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.res_id


from django.db import models

# Create your models here.
class Cart(models.Model):
    prod_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.prod_id
    
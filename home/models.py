from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField()
    photo=models.ImageField(null=True)

    def __str__(self):
        return self.name
    
	


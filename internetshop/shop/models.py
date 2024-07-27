from django.db import models

# Create your models here.
class Product(models.Model):
    name =  models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)
    brandMark = models.CharField(max_length=128, null=True, blank=True)
    coloring = models.CharField(max_length=128, null=True, blank=True)



    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    author = models.CharField(max_length=256)
    rating = models.IntegerField()
    text = models.TextField()
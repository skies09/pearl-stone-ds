from django.db import models

category_choices = (
    ('Rings','Rings'),
    ('Necklaces', 'Necklaces'),
    ('Bracelets','Bracelets'),
    ('Earrings','Earrings'),
    ('Collections','Collections'),
)
# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=254, choices=category_choices, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name




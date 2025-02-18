from django.db import models


class Filler(models.Model):
    FILLER_CHOICES = [
        ("chocolate", "шоколадные"),
        ("sugar_sprinkles", "сахарные присыпки"),
        ("fruits", "фрукты"),
        ("syrups", "сиропы"),
        ("jams", "джемы")
    ]
    name = models.CharField(max_length=20, choices=FILLER_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    hit = models.BooleanField(default=False)
    fat = models.IntegerField(null=False, blank=False, )
    fillers = models.ManyToManyField(Filler, related_name="products", blank=True, null=True)
    def __str__(self):
        return self.name

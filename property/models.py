from django.db import models

from agent.models import Agent


class Property(models.Model):
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    class SaleStatus(models.TextChoices):
        RENT = "RENT", "For Rent"
        SALE = "SALE", "For Sale"
        OPEN_HOUSE = "OH", "Open House"

    @property
    def display_price(self):
        return "$ %s" % round(self.price)

    agent = models.ForeignKey(Agent, models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(choices=SaleStatus.choices, max_length=4)
    thumbnail = models.ImageField(upload_to="property_images")

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, models.CASCADE)
    image = models.ImageField(upload_to=f"property_images")

    def __str__(self):
        return self.property.title


class HouseFeature(models.Model):
    property = models.OneToOneField(Property, models.CASCADE)
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    map_location = models.CharField(max_length=100, blank=True)
    video_url = models.URLField(max_length=200, blank=True)
    floor_plan = models.ImageField(upload_to="floor_plans", blank=True)

    def __str__(self):
        return self.property.title


class Amenities(models.Model):
    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    property = models.ForeignKey(Property, models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

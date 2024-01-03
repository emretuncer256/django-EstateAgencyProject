from django.contrib import admin

from .models import (
    Property,
    Amenities,
    HouseFeature,
    PropertyImage
)


class AmenitiesInline(admin.TabularInline):
    model = Amenities
    extra = 2


class HouseFeatureInline(admin.StackedInline):
    model = HouseFeature


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [AmenitiesInline, HouseFeatureInline, PropertyImageInline]


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    ...


@admin.register(HouseFeature)
class HouseFeatureAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    ...

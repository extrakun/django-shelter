from django.contrib import admin
import animals.models as models

#
# from .models import AnimalType, Tag, Animal

# admin.site.register(AnimalType)
# admin.site.register(Tag)
# admin.site.register(Animal)

# Register your models here.
admin.site.register(models.AnimalType)
admin.site.register(models.Tag)
admin.site.register(models.Animal)
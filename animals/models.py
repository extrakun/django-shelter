from django.db import models

# Create your models here.
class AnimalType(models.Model):
    name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(blank=False, max_length=255, null=False)
    age = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE, related_name='animals')
    tags = models.ManyToManyField(Tag, related_name='animals')
    microchip = models.CharField(blank=False, max_length=255, null=False)
    
    def __str__(self):
        return self.name
        

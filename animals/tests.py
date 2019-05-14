from django.test import TestCase
from .models import AnimalType, Tag, Animal

# Create your tests here.
class AnimalTypeTest(TestCase):
    
    def testCanCreateAnimalType(self):
        a = AnimalType(name="Dog")
        # save a (the animal) and give it a unique id
        a.save()
        
        # Test if we can retrieve the animal type from the DB
        b = AnimalType.objects.all().get(pk=a.id)
        self.assertEquals(a.name, b.name)
        self.assertEquals(a.id, b.id)
        

class TagTest(TestCase):
    def testCanCreateTag(self):
        t = Tag(name="#hyperactive")
        t.save()
        
        t2 = Tag.objects.all().get(pk=t.id)
        self.assertEquals(t.name, t2.name)
        self.assertEquals(t.id, t2.id)
        
class AnimalTest(TestCase):
    def testCanCreateAnimal(self):
        at = AnimalType(name="Dog")
        # save a (the animal) and give it a unique id
        at.save()
        
        t = Tag(name="#hyperactive")
        t.save()
        
        a = Animal(name="Biscuit", age=1, weight=40, animal_type=at)
        a.save()
        a.tags.add(t)
        
        a2 = Animal.objects.all().get(pk=a.id)
        self.assertEquals(a.name, a2.name)
        self.assertEquals(a.age, a2.age)
        self.assertEquals(a.animal_type.name, a2.animal_type.name)
        self.assertEquals(a2.tags.count(), 1)
        self.assertEquals(a2.tags.all()[0].name, '#hyperactive')
        
    def testAnimalCanHaveManyTags(self):
        at = AnimalType(name="Dog")
        # save a (the animal) and give it a unique id
        at.save()
        
        t = Tag(name="#hyperactive")
        t.save()
        
        t2 = Tag(name="#greedy")
        t2.save()
        
        a = Animal(name="Biscuit", age=1, weight=40, animal_type=at)
        a.save()
        a.tags.add(t)
        a.tags.add(t2)
        
        a2 = Animal.objects.all().get(pk=a.id)
        self.assertEquals(a2.tags.count(), 2)
        self.assertEquals(a2.tags.all()[0].name, '#hyperactive')
        self.assertEquals(a2.tags.all()[1].name, '#greedy')
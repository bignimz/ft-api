from django.conf import settings
from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    is_alive = models.BooleanField(default=True)
    date_of_death = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    biographical_information = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    TYPE_CHOICES = [
        ('Parent', 'Parent'),
        ('Spouse', 'Spouse'),
        ('Child', 'Child'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='relationships')
    related_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')

class FamilyTree(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(FamilyMember, related_name='trees')

    def __str__(self):
        return self.name

from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import CharField, TextField

class BlogManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        if len(data['title']) < 2:
            errors['title'] = 'Show title must be at least 2 characters'
        if len(data['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters'
        if len(data['description']) < 5 and len(data['description']) != 0:
            errors['description'] = 'Show description must be at least 10 characters'
        return errors

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
    
    def __repr__(self) -> str:
        return f'id: {self.id} - Nombre: {self.name}'

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    #network = models.ForeignKey(Network, related_name="shows", on_delete = models.CASCADE)
    network = CharField(max_length=255)
    description = TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

    def __repr__(self) -> str:
        return f'id: {self.id} - Título: {self.title} - Release Date: {self.release_date}'



#from tv_app.models import Show, Network
from django.db import models
from django.urls import reverse

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="Name")
    main_field = models.CharField(max_length=200, help_text="Main text")
    add_field = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])

import uuid 

class CurrentNote(models.Model):
    note = models.ForeignKey('Note', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        ordering = ["note"]

    def __str__(self):
        return '%s' % (self.id,self.note.name)

    
class RegisterToken(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=6)

    def __str__(self):
        return self.token

class User(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        permissions = [
            ("user_delete", "Can delete users | by Mark"),
        ]

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    field = models.CharField(max_length=6)



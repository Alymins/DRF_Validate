from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    phone = models.CharField(max_length=14)
    active = models.BooleanField()
    
    def __str__(self):
        return self.name
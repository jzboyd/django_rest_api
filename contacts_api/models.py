from django.db import models

# Create your models here.

## Contacts Model 
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.IntegerField()
    phone_number = models.IntegerField()
    postal_code= models.IntegerField()

    def __str__(self):
        return self.name
        return self.email
        return self.postal_code
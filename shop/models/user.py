from django.db import  models

class User(models.Model):
    name = models.CharField(max_length= 50)
    active =  models.BooleanField(default=True)
    email = models.CharField(max_length= 100 , unique= True)
    password = models.CharField(max_length= 500)
    phone = models.CharField(max_length= 10)

    def __str__(self):
        return self.name

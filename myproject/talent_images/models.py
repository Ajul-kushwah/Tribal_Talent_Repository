from django.db import models
from django.contrib.auth.models import User


class UserImages(models.Model):
    user=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default="Image :")
    image=models.ImageField(upload_to="user_talent_images",default="")
    desc = models.TextField(default="###########")

    def __str__(self):
        return str(self.user)

class CompanyImages(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100 ,default="Image :")
    image = models.ImageField(upload_to="company_images", default="")
    desc = models.TextField(default="###########")

    def __str__(self):
        return str(self.user)



class Skill(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100, default="")
    other_skill = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.user)

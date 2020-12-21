from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class TribalYouth(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=30, default="")

    father_name = models.CharField(max_length=50, default="",blank=True,null=True)

    email = models.EmailField(default="")
    your_mobile_no=models.CharField(max_length=10,default="",blank=True, null=True)
    father_mobile_no=models.CharField(max_length=10,default="",blank=True,null=True)
    website = models.URLField(default="", blank=True, null=True)

    category = models.CharField(max_length=50,default="")

    gender=models.CharField(max_length=10,default="")
    age=models.IntegerField(default=0)

    highqualification=models.CharField(max_length=50,default="")

    language=models.CharField(max_length=50,default="hindi")
    experience=models.CharField(max_length=20)
    talent_category=models.CharField(max_length=50,default="")
    talent_name=models.CharField(max_length=50,default="")

    caption = RichTextField(blank=True, null=True)

    area=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    city_pincode=models.IntegerField(default=0)
    state=models.CharField(max_length=50,default="")
    country=models.CharField(max_length=50,default="")

    image = models.ImageField(upload_to="media/accounts/images", default="media/accounts/images/admin.png")
    cover_photo = models.ImageField(upload_to="cover_photo", default="cover_photo/subscribe-bg.png",blank=True,null=True)

    talent_description=models.TextField(max_length=1000,default="",blank=True,null=True)
    about_you=models.TextField(max_length=1000,default="",blank=True,null=True)

    join_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.firstname+"     "+self.username


class Company(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    company_name = models.CharField(max_length=100)
    company_username = models.CharField(max_length=100,default="")
    company_trending_name = models.CharField(max_length=100, default="")

    company_type=models.CharField(max_length=100,default='')
    class_of_company=models.CharField(max_length=100,default="")
    category = models.CharField(max_length=100,default="")

    company_desc=models.TextField(default='',blank=True,null=True)

    registration_no=models.CharField(max_length=50,default="")

    establishment_year=models.CharField(max_length=100,default="")
    company_status=models.CharField(max_length=100,default="Active")
    no_of_employee=models.IntegerField(default=0)

    country=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    city_pincode=models.CharField(max_length=100,default="")

    company_email = models.EmailField(default="")
    landline_no = models.CharField(max_length=100, default="",blank=True, null=True)
    fax_no = models.CharField(max_length=100, default="",blank=True, null=True)
    website=models.CharField(max_length=1000,default="",blank=True, null=True)

    images=models.ImageField(upload_to="company_user",default="media/admin.png",null=True)
    cover_photo = models.ImageField(upload_to="cover_photo", default="media/cover_photo/subscribe-bg.png", blank=True,
                                    null=True)

    def __str__(self):
        return self.company_username


class Token(models.Model):
    token = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200 , blank=True , null=True)
    image = models.ImageField(upload_to="my_post" , null=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    liked = models.ManyToManyField(User,default=None,blank=True , related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE , related_name='author')

    def __str__(self):
        return str(self.title)

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES , default='Like',max_length=10)

    def __str__(self):
        return str(self.post)


class Following(models.Model):
    """ Following of the user """
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed")
    follower = models.ManyToManyField(User, related_name="follower")

    @classmethod
    def follow(cls, user, another_account):
        obj,create = cls.objects.get_or_create(user = user)
        obj.followed.add(another_account)

    @classmethod
    def unfollow(cls, user, another_account):
        obj = cls.objects.get(user = user)
        obj.followed.remove(another_account)

    def __str__(self):
        return str(self.user)

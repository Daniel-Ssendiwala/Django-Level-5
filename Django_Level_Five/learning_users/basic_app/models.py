from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # borrow from djangos inbuilt user model
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional attributes
    GENDER =(
            ('M','Male'),
            ('F','Female'),
            )
    gender = models.CharField(max_length = 1,default = 'M',choices = GENDER)
    portfolio_site = models.URLField(blank =True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
# Create your models here.
from django.db.models.signals import post_save
from phone_field import PhoneField


class UserProfile(models.Model):
    # user = models.OneToOneField(User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=False)
    country = CountryField(blank_label="Select a Country", blank=False)
    phoneNumber = PhoneField(blank=True)
    profileImage = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profile'


def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.created(user=kwargs['instance'])

    post_save.connect(createProfile, sender=User)

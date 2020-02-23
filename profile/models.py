from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    home_address = models.TextField(max_length=500, blank=True)
    home_postal_code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
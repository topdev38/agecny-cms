from django.db import models
from django.conf import settings

class Subscriber(models.Model):
    email = models.EmailField(max_length=254, unique=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=254, null=True, blank=True)
    text = models.TextField()

class Team_member(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    linkedin_profile = models.URLField(max_length=254, null=True, blank=True)
    facebook_profile = models.URLField(max_length=254, null=True, blank=True)
    twitter_profile = models.URLField(max_length=254, null=True, blank=True)
    photo = models.ImageField(upload_to="member/", default='..{}img/customer/customer-1.png'.format(settings.STATIC_URL))

class Customer(models.Model):
    RATING = (
        (5, 'Perfect'),
        (4, 'Very good'),
        (3, 'Good'),
        (2, 'Bad'),
        (1, 'Very Bad'),
    )
    customer_name = models.CharField(max_length=30)
    customer_link = models.URLField(max_length=254, null=True, blank=True)
    rating = models.IntegerField(default=5, choices=RATING)
    quote = models.TextField()
    photo = models.ImageField(upload_to="customer/", default='..{}img/customer/customer-1.png'.format(settings.STATIC_URL))
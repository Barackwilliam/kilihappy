from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Service(models.Model):
    Title =  models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True) 

    def __str__(self):
        return self. Title




class Team(models.Model):
    Full_name =  models.CharField(max_length=100)
    image = CloudinaryField('image', blank=True, null=True) 
    designation = models.TextField()
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self. Full_name
   


class Step_for_booking(models.Model):
    Title =  models.CharField(max_length=100)
    image = CloudinaryField('image', blank=True, null=True) 
    description = models.TextField()
    def __str__(self):
        return self. Title
   


class Package(models.Model):
    number_of_people =  models.IntegerField()
    number_of_day =  models.IntegerField()
    image = CloudinaryField('image', blank=True, null=True) 
    description = models.TextField()
    location =  models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self. location

class User_Testimonial(models.Model):
    Full_name =  models.CharField(max_length=100)
    image = CloudinaryField('image', blank=True, null=True) 
    description = models.TextField()
    country =  models.CharField(max_length=100)
    def __str__(self):
        return self. Full_name
   

class Destination(models.Model):
    Offer_in_percent =  models.IntegerField(blank=True,null=True)
    image = CloudinaryField('image', blank=True, null=True) 
    location =  models.CharField(max_length=100)
    def __str__(self):
        return self. location
   


class Gallery(models.Model):
    Title =  models.CharField(max_length=100)
    image =CloudinaryField('image', blank=True, null=True) 
    def __str__(self):
        return self. Title



class About_This_Organization(models.Model):
    title = models.CharField(max_length=200, default="Welcome to  Kilihappy Tanzania Advantures")
    content = models.TextField(default="Kilihappy Tanzania Adventures was founded in 2025 by a group of passionate Tanzanians who were eager to share the richness of our country with the world. From a small team of nature lovers and adventurers, we have grown into a trusted partner for tourists looking for authentic and unforgettable experiences in Tanzania.")
    mission = models.TextField(blank=True, default="To provide unique and high-quality tourism experiences, both locally and internationally, in a safe, sustainable, and environmentally friendly manner while prioritizing customer service and community development.")
    vision = models.TextField(blank=True, default="To become the leading tourism company in East Africa, recognized globally for excellence, innovation, and social responsibility.")
    image = CloudinaryField('image', blank=True, null=True) 
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


from django.db import models

class Booking_Report(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    destination = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.destination}"



from django.db import models

class Contact_Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
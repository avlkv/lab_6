from django.db import models


class Event(models.Model):
    name_event = models.CharField(max_length=100)
    date_event = models.DateTimeField('date realized')

    def __str__(self):
        return self.name_event


class User(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=30)
    age_user = models.IntegerField(default=0)
    field = models.ImageField(blank=True, null=True, upload_to='./static/photo'),

    def __str__(self):
        return self.name_user


class Customers(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)

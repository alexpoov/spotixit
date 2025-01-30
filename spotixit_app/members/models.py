from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)

# after changes:
# py manage.py makemigrations members # to make migrations
# py manage.py migrate # to apply migrations
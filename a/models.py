from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=50, unique=True)
    detail = models.TextField()
    is_available = models.BooleanField(default=True)

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    membership_type = models.CharField(max_length=20, choices=[('6 months', '6 months'), ('1 year', '1 year'), ('2 years', '2 years')])

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    fine = models.IntegerField()



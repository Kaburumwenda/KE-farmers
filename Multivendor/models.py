from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Condition(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

        
class MultivendorProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Processing', 'Processing'),
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Closed', 'Closed'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default='80100-Nairobi,kenya')
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    businessname = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    discount=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    description = models.TextField(max_length=555)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

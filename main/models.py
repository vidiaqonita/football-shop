# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('new', 'New'),
        ('apparel', 'Apparel'),
        ('kids', 'Kids'),
        ('brands', 'Brands'),
        ('footwear', 'Footwear'),
        ('equipment', 'Equipment'),
        ('sale', 'Sale')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description=models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='new')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

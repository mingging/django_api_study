from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=True)
    
    class Meta:
        db_table = "api_user_user"


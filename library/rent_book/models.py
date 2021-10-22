from django.db import models

# Create your models here.

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    major = models.CharField(max_length=128, null=False)
    grade = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = "students"


class Book(models.Model):
    isbn = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = "rent_book_book"

# class Rent(models.Model):
#     pass
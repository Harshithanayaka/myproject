from django.db import models

class plans(models.Model):
    id=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pprize=models.IntegerField()

class postpaid(models.Model):
    id=models.IntegerField(primary_key=True)
    pstname=models.CharField(max_length=20)
    pstprize=models.IntegerField()

class dongle(models.Model):
    id=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20)
    dprize=models.IntegerField()

class userdetails(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    mobile=models.IntegerField()
    def __str__(self):
        return self.title



# Create your models here.

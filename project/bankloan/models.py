from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
class customer_detail(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=70)
    credit_score=models.IntegerField()
    occupation=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    income=models.IntegerField()
    loan_type=models.CharField(max_length=20)   

class payment(models.Model):
    holder_name=models.CharField(max_length=45)
    acc_number=models.CharField(max_length=16)
    bank_name=models.CharField(max_length=25)
    ifsc_number=models.CharField(max_length=11)

